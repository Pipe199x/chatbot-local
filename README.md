# 🧠 Chat de Recuperación (LLaMA 3 + Flask)

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-green)
![LLaMA](https://img.shields.io/badge/Model-LLaMA%203-orange)


Este es un chatbot local que utiliza el modelo **LLaMA 3** a través de [Ollama](https://ollama.com/) y una interfaz web construida con **Flask**. Permite tener conversaciones en español o inglés de manera local, sin enviar datos a la nube.

---

## 📦 Requisitos

* Python 3.9 o superior
* Git
* [Ollama](https://ollama.com/) instalado y funcionando localmente

---

## ⚙️ Instalación paso a paso

1. **Clona este repositorio**:

```bash
git clone https://github.com/Pipe199x/chatbot-local.git
cd chatbot-local
```

2. **Crea y activa un entorno virtual**:

```bash
python -m venv venv

# En Windows:
venv\Scripts\activate

# En Mac/Linux:
source venv/bin/activate
```

3. **Instala las dependencias**:

```bash
pip install -r requirements.txt
```

4. **Instala y ejecuta Ollama**

Descarga Ollama desde: [https://ollama.com/download](https://ollama.com/download)

Luego ejecuta el modelo LLaMA 3 (esto descargará \~4.7GB):

```bash
ollama run llama3
```

5. **Ejecuta la app**:

```bash
python app.py
```

Abre tu navegador en `http://localhost:5000`.

---

## 🖥️ Estructura del Proyecto

```
chatbot-local/
├── app.py                 # Backend Flask
├── chat_history.jsonl     # Historial de conversaciones (ignorado por Git)
├── requirements.txt       # Librerías requeridas
├── templates/
│   └── index.html         # Interfaz web
├── .gitignore
└── README.md
```

---

## 🧠 Modelo utilizado

Este proyecto usa el modelo `llama3` ejecutado localmente con **Ollama**. No se requiere conexión a internet para procesar preguntas una vez descargado el modelo.

---

## ✨ Créditos

* Desarrollado por **Pipe199x**
* Avatares proporcionados por [Flaticon](https://www.flaticon.com/)
