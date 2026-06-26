# NYC Apartment Search Workflow

A local, single-user NYC apartment-search app. Scrapes StreetEasy listings,
enriches them with HPD and public Openigloo data, and applies deterministic
app-side filtering.

## Stack

- **Backend:** Python, FastAPI, SQLAlchemy, SQLite. Managed with [uv](https://docs.astral.sh/uv/).
- **Frontend:** React + TypeScript (Vite).

## Setup

### Backend

```sh
cd backend
uv sync
cp ../.env.example ../.env   # then edit .env
uv run uvicorn app.main:app --reload   # http://127.0.0.1:8000
```

Health check: `GET /health` → `{"status": "ok"}`. Interactive API docs at
`http://127.0.0.1:8000/docs`.

### Frontend

Scaffolded with Vite's `react-ts` template (React 19, TypeScript, ESLint).

```sh
cd frontend
npm install
npm run dev      # start the dev server (http://127.0.0.1:5173)
```

Other scripts: `npm run build`, `npm run preview`, `npm run lint`.

## Privacy

Per AGENTS.md, this app never stores credentials, raw HTML, downloaded images,
review text, or paywalled content. The `.gitignore` enforces this.
