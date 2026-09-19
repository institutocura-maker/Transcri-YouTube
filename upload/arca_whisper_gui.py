cat << 'EOF' > arca_whisper_gui.py
import os
import sys
import glob
import site
import time
import queue
import ctypes
import threading
from datetime import timedelta
import customtkinter as ctk
from customtkinter import filedialog

# -------------------------------------------------------------
# AUTO-CORREÇÃO DE BIBLIOTECAS CUDA (libcublas.so.12 / cuDNN)
# -------------------------------------------------------------
def carregar_bibliotecas_cuda_locais():
    for base in site.getsitepackages():
        arquivos = glob.glob(os.path.join(base, "nvidia", "**", "libcublas.so.12*"), recursive=True)
        for arq in arquivos:
            try:
                ctypes.CDLL(arq, mode=ctypes.RTLD_GLOBAL)
            except Exception:
                pass

carregar_bibliotecas_cuda_locais()

from faster_whisper import WhisperModel

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

ARQUIVO_LOG_SISTEMA = "arca_transcricoes.log"

class ArcaWhisperApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Arca do Conhecimento — Transcritor Neural (Off-Grid)")
        self.geometry("1020x820")
        self.minsize(850, 650)

        self.caminho_arquivo = None
        self.modelo_whisper = None
        self.modelo_atual_nome = None
        self.transcrevendo = False
        self.texto_completo_buffer = []

        self.fila_mensagens = queue.Queue()

        self._construir_interface()
        self.after(100, self._processar_fila_gui)

    def _construir_interface(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)

        # 1. CABEÇALHO COM SELEÇÃO DO MODELO
        frame_header = ctk.CTkFrame(self, corner_radius=10)
        frame_header.grid(row=0, column=0, padx=20, pady=(15, 10), sticky="ew")

        label_titulo = ctk.CTkLabel(
            frame_header, 
            text="ARCA DO CONHECIMENTO : TRANSCRIÇÃO NEURAL", 
            font=ctk.CTkFont(size=18, weight="bold")
        )
        label_titulo.pack(side="left", padx=15, pady=10)

        # Seletor do modelo
        frame_modelo_box = ctk.CTkFrame(frame_header, fg_color="transparent")
        frame_modelo_box.pack(side="right", padx=15, pady=5)

        lbl_combo = ctk.CTkLabel(frame_modelo_box, text="Modelo:", font=ctk.CTkFont(size=12, weight="bold"))
        lbl_combo.pack(side="left", padx=5)

        self.combo_modelo = ctk.CTkComboBox(
            frame_modelo_box,
            values=["medium", "large-v3", "small"],
            width=120,
            state="readonly"
        )
        self.combo_modelo.set("medium")
        self.combo_modelo.pack(side="left", padx=5)

        # 2. SELEÇÃO DE ARQUIVO
        frame_arquivo = ctk.CTkFrame(self, corner_radius=10)
        frame_arquivo.grid(row=1, column=0, padx=20, pady=5, sticky="ew")
        frame_arquivo.grid_columnconfigure(1, weight=1)

        btn_selecionar = ctk.CTkButton(
            frame_arquivo, 
            text="Selecionar Mídia", 
            command=self._selecionar_arquivo,
            width=180
        )
        btn_selecionar.grid(row=0, column=0, padx=10, pady=10)

        self.entry_caminho = ctk.CTkEntry(
            frame_arquivo, 
            placeholder_text="Escolha um arquivo de áudio ou vídeo...", 
            state="readonly"
        )
        self.entry_caminho.grid(row=0, column=1, padx=(0, 10), pady=10, sticky="ew")

        # 3. GLOSSÁRIO ESTRUTURADO (PROMPT EM PROSA)
        frame_prompt = ctk.CTkFrame(self, corner_radius=10)
        frame_prompt.grid(row=2, column=0, padx=20, pady=5, sticky="ew")

        label_prompt = ctk.CTkLabel(
            frame_prompt, 
            text="Contexto Semântico & Gramatical (initial_prompt) — Define Vocabulário e Pontuação:",
            font=ctk.CTkFont(size=13, weight="bold")
        )
        label_prompt.pack(anchor="w", padx=15, pady=(8, 2))

        glossario_prosa = (
            "Esta é uma preleção filosófica sobre as Revelações Cósmicas com Jan Val Ellam. "
            "O discurso aborda com clareza o drama de Javé (Brahma), a anomalia primordial e a dor de Sophia (Pistis Sophia). "
            "Analisa a atuação lúcida de Lúcifer e Mikael perante a quarentena do planeta Shen (Terra). "
            "São citados conceitos como os Elohim, Shivaya, a Trimúrti, o projeto dos Engenheiros Siderais, "
            "a presença Anunnaki, Kumaras, Watchers e o genoma cósmico humano de 22 delegações. "
            "O diálogo é reflexivo, estruturado com rigor gramatical, pontos finais, interrogações e vírgulas bem definidas."
        )

        self.txt_prompt = ctk.CTkTextbox(frame_prompt, height=80, wrap="word", font=("Consolas", 11))
        self.txt_prompt.pack(fill="x", padx=10, pady=(0, 10))
        self.txt_prompt.insert("1.0", glossario_prosa)

        # 4. ÁREA DE SAÍDA / LOGS
        frame_saida = ctk.CTkFrame(self, corner_radius=10)
        frame_saida.grid(row=3, column=0, padx=20, pady=5, sticky="nsew")
        frame_saida.grid_columnconfigure(0, weight=1)
        frame_saida.grid_rowconfigure(0, weight=1)

        self.txt_log = ctk.CTkTextbox(frame_saida, wrap="word", font=("Ubuntu Mono", 12))
        self.txt_log.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # 5. CONTROLES E BOTÕES
        frame_acoes = ctk.CTkFrame(self, corner_radius=10)
        frame_acoes.grid(row=4, column=0, padx=20, pady=(5, 15), sticky="ew")

        self.btn_iniciar = ctk.CTkButton(
            frame_acoes, 
            text="Iniciar Transcrição", 
            command=self._iniciar_thread_transcricao,
            height=40,
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="#2563EB",
            hover_color="#1D4ED8"
        )
        self.btn_iniciar.pack(side="left", padx=10, pady=10)

        # CHECKBOX: INCLUIR OU NÃO TIMESTAMPS
        self.chk_timestamps = ctk.CTkCheckBox(
            frame_acoes,
            text="Incluir Timestamps",
            font=ctk.CTkFont(size=12, weight="bold")
        )
        self.chk_timestamps.select()  # Vem marcado por padrão
        self.chk_timestamps.pack(side="left", padx=10, pady=10)

        self.btn_salvar = ctk.CTkButton(
            frame_acoes, 
            text="Salvar em Markdown", 
            command=self._salvar_arquivo_md,
            state="disabled",
            height=40
        )
        self.btn_salvar.pack(side="left", padx=5, pady=10)

        self.btn_copiar_log = ctk.CTkButton(
            frame_acoes, 
            text="Copiar Log", 
            command=self._copiar_log_para_clipboard,
            height=40,
            fg_color="#475569",
            hover_color="#334155"
        )
        self.btn_copiar_log.pack(side="left", padx=5, pady=10)

        self.lbl_status = ctk.CTkLabel(frame_acoes, text="Status: Pronto.")
        self.lbl_status.pack(side="right", padx=15, pady=10)

    # -------------------------------------------------------------
    # LOGS E INTERFACE THREAD-SAFE
    # -------------------------------------------------------------
    def _gravar_log(self, mensagem):
        print(mensagem)
        try:
            with open(ARQUIVO_LOG_SISTEMA, "a", encoding="utf-8") as f:
                f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {mensagem}\n")
        except Exception:
            pass

    def _enviar_para_gui(self, tipo, conteudo):
        self.fila_mensagens.put((tipo, conteudo))
        if tipo == "LOG":
            self._gravar_log(conteudo)

    def _copiar_log_para_clipboard(self):
        conteudo = self.txt_log.get("1.0", "end").strip()
        if conteudo:
            self.clipboard_clear()
            self.clipboard_append(conteudo)
            self._enviar_para_gui("STATUS", "Log copiado!")

    def _processar_fila_gui(self):
        try:
            while not self.fila_mensagens.empty():
                tipo, conteudo = self.fila_mensagens.get_nowait()
                if tipo == "LOG":
                    self.txt_log.insert("end", conteudo + "\n")
                    self.txt_log.see("end")
                elif tipo == "STATUS":
                    self.lbl_status.configure(text=f"Status: {conteudo}")
                elif tipo == "CONCLUIDO":
                    self.transcrevendo = False
                    self.btn_iniciar.configure(state="normal", text="Iniciar Transcrição")
                    self.btn_salvar.configure(state="normal")
                    self.combo_modelo.configure(state="readonly")
                    self.chk_timestamps.configure(state="normal")
                elif tipo == "ERRO":
                    self.transcrevendo = False
                    self.btn_iniciar.configure(state="normal", text="Iniciar Transcrição")
                    self.combo_modelo.configure(state="readonly")
                    self.chk_timestamps.configure(state="normal")
        except Exception:
            pass

        self.after(100, self._processar_fila_gui)

    def _formatar_tempo(self, segundos):
        return str(timedelta(seconds=int(segundos)))

    def _selecionar_arquivo(self):
        tipos = [
            ("Mídias de Áudio e Vídeo", "*.mp3 *.wav *.m4a *.mp4 *.mkv *.webm *.flac *.aac *.ogg"),
            ("Todos os Arquivos", "*.*")
        ]
        caminho = filedialog.askopenfilename(title="Escolha o arquivo de mídia", filetypes=tipos)
        if caminho:
            self.caminho_arquivo = caminho
            self.entry_caminho.configure(state="normal")
            self.entry_caminho.delete(0, "end")
            self.entry_caminho.insert(0, caminho)
            self.entry_caminho.configure(state="readonly")
            self._enviar_para_gui("LOG", f"📂 Arquivo carregado: {os.path.basename(caminho)}")

    def _iniciar_thread_transcricao(self):
        if not self.caminho_arquivo:
            self._enviar_para_gui("LOG", "⚠️ Selecione um arquivo de mídia primeiro!")
            return

        if self.transcrevendo:
            return

        prompt_customizado = self.txt_prompt.get("1.0", "end").strip()
        caminho = self.caminho_arquivo
        modelo_escolhido = self.combo_modelo.get()
        usar_timestamps = self.chk_timestamps.get() == 1

        self.transcrevendo = True
        self.btn_iniciar.configure(state="disabled", text="Processando...")
        self.combo_modelo.configure(state="disabled")
        self.chk_timestamps.configure(state="disabled")
        self.btn_salvar.configure(state="disabled")
        self.txt_log.delete("1.0", "end")
        self.texto_completo_buffer.clear()

        worker = threading.Thread(
            target=self._executar_transcricao_cuda, 
            args=(caminho, prompt_customizado, modelo_escolhido, usar_timestamps),
            daemon=True
        )
        worker.start()

    def _executar_transcricao_cuda(self, caminho_arquivo, prompt_customizado, modelo_nome, usar_timestamps):
        inicio_cronometro = time.time()

        try:
            if self.modelo_whisper is None or self.modelo_atual_nome != modelo_nome:
                self._enviar_para_gui("STATUS", f"Alocando modelo '{modelo_nome}' na RTX 3060...")
                self._enviar_para_gui("LOG", f"⏳ Carregando motor neural [{modelo_nome}] na VRAM via CUDA...")
                
                self.modelo_whisper = None
                self.modelo_whisper = WhisperModel(modelo_nome, device="cuda", compute_type="float16")
                self.modelo_atual_nome = modelo_nome
                self._enviar_para_gui("LOG", f" Modelo [{modelo_nome}] alocado na memória gráfica!\n")

            modo_str = "COM minutagem" if usar_timestamps else "TEXTO LIMPO (Sem minutagem)"
            self._enviar_para_gui("STATUS", f"Transcrevendo com [{modelo_nome}]...")
            self._enviar_para_gui("LOG", "=" * 60)
            self._enviar_para_gui("LOG", f"🚀 Arquivo: {os.path.basename(caminho_arquivo)}")
            self._enviar_para_gui("LOG", f"⚙️ Configuração: {modelo_nome} | Modo: {modo_str}")
            self._enviar_para_gui("LOG", "=" * 60 + "\n")

            segmentos, info = self.modelo_whisper.transcribe(
                caminho_arquivo,
                language="pt",
                initial_prompt=prompt_customizado,
                vad_filter=True,
                condition_on_previous_text=False,
                beam_size=5
            )

            self._enviar_para_gui("LOG", f"⏱️ Duração do áudio: {self._formatar_tempo(info.duration)}")
            self._enviar_para_gui("LOG", f"🌐 Idioma: {info.language} | Processando...\n")

            # Varredura dos segmentos
            paragrafo_temp = []
            for seg in segmentos:
                frase = seg.text.strip()
                if not frase:
                    continue

                if usar_timestamps:
                    tempo_str = f"[{self._formatar_tempo(seg.start)} -> {self._formatar_tempo(seg.end)}]"
                    linha = f"{tempo_str} {frase}"
                    self.texto_completo_buffer.append(linha)
                    self._enviar_para_gui("LOG", linha)
                else:
                    # Agrupa de forma orgânica criando parágrafos naturais
                    paragrafo_temp.append(frase)
                    if len(paragrafo_temp) >= 3 or frase.endswith(('.', '?', '!')):
                        bloco = " ".join(paragrafo_temp)
                        self.texto_completo_buffer.append(bloco)
                        self._enviar_para_gui("LOG", bloco + "\n")
                        paragrafo_temp = []

            # Se sobrou alguma frase no buffer sem timestamps
            if paragrafo_temp:
                bloco = " ".join(paragrafo_temp)
                self.texto_completo_buffer.append(bloco)
                self._enviar_para_gui("LOG", bloco)

            tempo_total = round(time.time() - inicio_cronometro, 2)
            self._enviar_para_gui("LOG", "\n" + "=" * 60)
            self._enviar_para_gui("LOG", f" Transcrição concluída em {tempo_total}s!")
            self._enviar_para_gui("LOG", "=" * 60)

            self._enviar_para_gui("STATUS", f"Pronto ({tempo_total}s)")
            self._enviar_para_gui("CONCLUIDO", True)

        except Exception as e:
            msg_erro = f"❌ Falha: {str(e)}"
            self._enviar_para_gui("LOG", f"\n{msg_erro}")
            self._enviar_para_gui("STATUS", "Erro.")
            self._enviar_para_gui("ERRO", str(e))

    def _salvar_arquivo_md(self):
        if not self.texto_completo_buffer:
            return

        usar_timestamps = self.chk_timestamps.get() == 1
        nome_padrao = os.path.splitext(os.path.basename(self.caminho_arquivo))[0] + ".md"
        destino = filedialog.asksaveasfilename(
            title="Salvar Transcrição Markdown",
            initialfile=nome_padrao,
            defaultextension=".md",
            filetypes=[("Markdown", "*.md"), ("Arquivo de Texto", "*.txt")]
        )

        if destino:
            modo_desc = "Com Timestamps" if usar_timestamps else "Texto Corrido (Sem Timestamps)"
            separador_linhas = "\n" if usar_timestamps else "\n\n"

            cabecalho = [
                f"# Transcrição: {os.path.basename(self.caminho_arquivo)}\n",
                f"- **Data:** {time.strftime('%Y-%m-%d %H:%M:%S')}",
                f"- **Arquivo:** `{self.caminho_arquivo}`",
                f"- **Formato:** {modo_desc}",
                f"- **Motor:** faster-whisper ({self.modelo_atual_nome} / FP16 CUDA)",
                "\n---\n",
                f"## Conteúdo ({modo_desc}):\n\n"
            ]
            conteudo = "\n".join(cabecalho) + separador_linhas.join(self.texto_completo_buffer)

            with open(destino, "w", encoding="utf-8") as f:
                f.write(conteudo)

            self._enviar_para_gui("LOG", f"💾 Arquivo salvo em: {destino}")

if __name__ == "__main__":
    app = ArcaWhisperApp()
    app.mainloop()
EOF