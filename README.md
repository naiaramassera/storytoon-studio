StoryToon Studio — MVP Inicial
Pacote inicial de um app para criar séries animadas com personagens consistentes, vozes fixas e episódios montados automaticamente.

O que vem neste pacote
backend/com FastAPI
frontend/com Next.js 14 + Tailwind
docker-compose.ymlcom Postgres + Redis
estrutura para episódios, personagens, cenas e empregos
prompts-base para roteiro, cena e voz
Visão do MVP
A usuária:

cria uma série
cadastra personagens
cola uma.
escolha a tolerância alvo
gera a estrutura do episódio
depois renderiza o episódio
Pilha
Frontend: Next.js, React, Tailwind
Backend: FastAPI, SQLAlchemy, Pydantic
Banco: PostgreSQL
Fila: Redis
Trabalhadores: Aipo
Montagem: FFmpeg
Como rodar localmente
1) Infra
docker compose up -d postgres redis
2) Backend
cd backend
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
3) Trabalhador
Em outro terminal:

cd backend
source .venv/bin/activate
celery -A app.workers.tasks.celery_app worker --loglevel=info
4) Frontend
cd frontend
npm install
npm run dev
URLs
Frontend: http://localhost:3000
Documentação do backend: http://localhost:8000/docs
Próximas integrações reais
substituir os stubs em:

backend/app/services/script_engine.py
backend/app/services/audio_engine.py
backend/app/services/video_engine.py
backend/app/services/consistency.py
backend/app/services/assembler.py
Fluxo técnico
POST /seriescria série
POST /characterscria personagem
POST /episodescria episódio
POST /episodes/{id}/build-outlinegera atos, cenas e diálogos
POST /episodes/{id}/renderdesproporcionar o aipo
trabalhador gera áudio, vídeo, validação e montagem
Observação importante
O sistema entrega o episódio final apenas para o usuário, mas trabalha internamente em cenas para preservar consistência e estabilidade.
