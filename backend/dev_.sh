PORT="${PORT:-8080}"
export OPENAI_API_BASE_URL=https://api.61798.cn/v1
export OPEANI_API_KEY=sk-kNiRHEfXlkhO9lmU7c17F6Ff2dCd49B794793d29E281DcAa
export ENABLE_OLLAMA_API=False
export RAG_EMBEDDING_ENGINE=""  # 表示使用SentenceTransformer
export RAG_EMBEDDING_MODEL=shibing624/text2vec-base-multilingual
export CHUNK_SIZE=1000
export RAG_WEB_SEARCH_ENGINE=searchpro # 搜索工具，eg：bing，searchpro，serper，jina,...
export ZHIPUAI_API_KEY=43a979ed9fe883767b975a782df5607d.LGik6haZSamTSWAv
export OFFLINE_MODE=True
uvicorn open_webui.main:app --port $PORT --host 0.0.0.0 --forwarded-allow-ips '*' --reload