# RAG Virtual Assistant

Asistente virtual que combina una arquitectura **RAG** (Retrieval-Augmented Generation) con herramientas de **Text-to-SQL** para consultar documentación técnica de vehículos.

Permite resolver dos tipos de preguntas sobre el dominio automotriz:
- Consultas sobre manuales técnicos y guías de usuario (RAG sobre PDFs)
- Consultas estructuradas sobre datos de vehículos, averías, piezas y mantenimiento (Text-to-SQL)

El agente decide de forma autónoma qué herramienta usar según la pregunta — o si necesita combinar ambas.

---

## 🏗️ Arquitectura

```
Usuario
   │
   ▼
┌─────────────────────┐
│   API (FastAPI)      │  ← expone el asistente vía REST
└──────────┬───────────┘
           │
           ▼
┌─────────────────────┐
│  Agente (LangGraph)  │  ← decide qué herramienta usar
└──────────┬───────────┘
           │
     ┌─────┴─────┐
     ▼           ▼
┌─────────┐  ┌──────────┐
│   SQL   │  │   RAG    │
│  Tool   │  │  Tool    │
└────┬────┘  └────┬─────┘
     │            │
     ▼            ▼
┌─────────┐  ┌──────────┐
│PostgreSQL│  │  Chroma  │
└─────────┘  └──────────┘
```

- **Agente:** orquesta el flujo y decide entre SQL, RAG o ambos
- **SQL Tool:** convierte preguntas en lenguaje natural a queries SQL sobre la base de datos de vehículos
- **RAG Tool:** recupera fragmentos relevantes de los manuales técnicos (PDF → chunks → embeddings → Chroma)
- **API:** capa REST que expone el asistente
- **Frontend:** UI explicativa que muestra qué herramienta usó el agente y por qué

> El proyecto incluye observabilidad (LangSmith) y evaluación de calidad del RAG (RAGAS) desde las primeras fases.

---

## 🛠️ Tecnologías

- **Framework agente:** LangGraph
- **Backend:** FastAPI
- **VectorDB:** Chroma (local) → pgvector en RDS (AWS)
- **Base de datos:** PostgreSQL / SQLite (local) → RDS (AWS)
- **LLM:** Anthropic API
- **Observabilidad:** LangSmith
- **Evaluación RAG:** RAGAS
- **Contenedores:** Docker + Docker Compose
- **CI/CD:** GitHub Actions
- **Cloud:** AWS

---

## 📍 Estado del proyecto

**En desarrollo activo.**

- [x] **Fase 0** — Entorno y estructura del repositorio
- [ ] Fase 1 — Agente base con LangGraph
- [ ] Fase 2 — Herramienta SQL (Text-to-SQL)
- [ ] Fase 3 — Herramienta RAG básica
- [ ] Fase 4 — API REST + UI explicativa
- [ ] Fase 5 — RAG avanzado (búsqueda híbrida, query rewriting, reranking)
- [ ] Fase 6 — Migración a AWS

---

## 🚀 Instalación

Requisitos: [uv](https://docs.astral.sh/uv/) y [Docker](https://www.docker.com/) instalados.

```bash
# 1. Clonar el repositorio
git clone https://github.com/DavidRuizCa/rag-virtual-assistant.git
cd rag-virtual-assistant

# 2. Instalar dependencias y crear el entorno virtual
uv sync

# 3. Configurar variables de entorno
cp .env.example .env
# Edita .env con tus claves reales (Anthropic, LangSmith, credenciales de Postgres)

# 4. Levantar los servicios (PostgreSQL)
docker compose up -d
```