FROM python:3.9-slim

WORKDIR /usr/src/streamlitapp

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "streamlit_chat_llama.py", "--server.port=8501", "--server.address=0.0.0.0"]

##################################################
# docker build -t codex_chatassistant_app:v0 .
# docker run -d -t --name chat_assistant_app -p 0.0.0.0:8501:8501 codex_chatassistant_app:v0