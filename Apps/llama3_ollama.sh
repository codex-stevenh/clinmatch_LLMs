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

docker run -d --gpus=all -v ollama_docker_1:/root/.ollama -p 0.0.0.0:11436:11434 --name ollama_duplicate ollama/ollama
docker exec -it ollama_duplicate ollama run llama3:8b
