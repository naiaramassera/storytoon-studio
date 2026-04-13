# StoryToon Studio — Starter MVP

Pacote inicial de um app para criar séries animadas com personagens consistentes, vozes fixas e episódios montados automaticamente.

## O que vem neste pacote
- `backend/` com FastAPI
- `frontend/` com Next.js 14 + Tailwind
- `docker-compose.yml` com Postgres + Redis
- estrutura para episódios, personagens, cenas e jobs
- prompts-base para roteiro, cena e voz

## Visão do MVP
A usuária:
1. cria uma série
2. cadastra personagens
3. cola uma história
4. escolhe a duração alvo
5. gera a estrutura do episódio
6. depois renderiza o episódio

## Stack
- Frontend: Next.js, React, Tailwind
- Backend: FastAPI, SQLAlchemy, Pydantic
- Banco: PostgreSQL
- Fila: Redis
- Workers: Celery
- Montagem: FFmpeg

## Como rodar localmente

### 1) Infra
```bash
docker compose up -d postgres redis
```

### 2) Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### 3) Worker
Em outro terminal:
```bash
cd backend
source .venv/bin/activate
celery -A app.workers.tasks.celery_app worker --loglevel=info
```

### 4) Frontend
```bash
cd frontend
npm install
npm run dev
```

## URLs
- Frontend: http://localhost:3000
- Backend docs: http://localhost:8000/docs

## Próximas integrações reais
Substituir os stubs em:
- `backend/app/services/script_engine.py`
- `backend/app/services/audio_engine.py`
- `backend/app/services/video_engine.py`
- `backend/app/services/consistency.py`
- `backend/app/services/assembler.py`

## Fluxo técnico
1. `POST /series` cria série
2. `POST /characters` cria personagem
3. `POST /episodes` cria episódio
4. `POST /episodes/{id}/build-outline` gera atos, cenas e diálogos
5. `POST /episodes/{id}/render` dispara pipeline Celery
6. worker gera áudio, vídeo, validação e montagem

## Observação importante
O sistema entrega episódio final único para a usuária, mas internamente trabalha em cenas para preservar consistência e estabilidade.
