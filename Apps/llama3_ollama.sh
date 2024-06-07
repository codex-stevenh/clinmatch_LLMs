export OLLAMA_HOST=0.0.0.0

./ollama serve
./ollama run llama3:8b

# curl http://192.168.0.107:11434/api/chat -d '{
#   "model": "llama3:8b",
#   "messages": [
#     { "role": "user", "content": "Where should I visit this weekend in HK?" }
#   ]
# }'

# curl http://192.168.0.107:11434/api/generate -d '{
#   "model": "llama3:8b",
#   "prompt":"Where should I visit this weekend in HK?"
# }'