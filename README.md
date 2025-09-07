# 🧠 Sprint Assistant

**Sprint Assistant** is a lightweight service that helps Scrum teams automate **daily standups**, collect **blocker analytics**, and generate **retrospective documents** in Google Docs — with calendar invites included.

---

## 🚀 Features

✅ Collects structured daily standup reports:

- `DONE`: What was completed yesterday  
- `WORKING_ON`: What you're working on today  
- `BLOCKED_BY`: Any blockers (optional)  

✅ Automatic analysis:

- Detects repeated blockers  
- Flags blockers that persist over multiple days  
- Detects missing standups from active team members  

✅ Generates:

- Retrospective document from a **Google Docs template**  
- Google Calendar meeting with a link to the generated doc  

---

## ⚙️ Tech Stack

- Python 3.11  
- FastAPI  
- Tortoise ORM  
- PostgreSQL (or SQLite for local development)  
- Google Drive API  
- Google Calendar API  
- GitHub Actions (for scheduled tasks)

---

## 🛠️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/sprint-assistant.git
cd sprint-assistant
```

### 2. Create a `.env` file

```ini
DATABASE_URL=sqlite://db.sqlite3
GOOGLE_CREDENTIALS_JSON=/path/to/service-account.json
RETRO_TEMPLATE_FOLDER_ID=your_drive_folder_id
CALENDAR_ID=your_calendar_id@group.calendar.google.com
```

### 3. Run the app using Docker

```bash
docker-compose up --build
```

### 4. Access the API docs

[http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧪 Running Tests

```bash
pytest
```

---

## 📁 Project Structure

```
app/
├── api/               # FastAPI routes
├── models/            # Database models
├── schemas/           # Pydantic validation schemas
├── services/          # Business logic (Google API, blockers, retro)
├── core/              # Configuration & startup
├── templates/         # Local templates (optional fallback)
scripts/               # CLI tools (for cron jobs or GitHub Actions)
tests/                 # Unit tests
```

---

## 📅 Roadmap

- [ ] Submit daily standup reports (DONE, WORKING_ON, BLOCKED_BY)  
- [ ] Detect long-standing or repeated blockers  
- [ ] Generate retrospective documents in Google Docs  
- [ ] Create Google Calendar events for retrospectives  
- [ ] (Optional) Telegram bot for daily standup input

---

# FastAPI Starter

Minimal FastAPI project scaffold with Docker and `.env` support.

## 🧱 Project Structure
```text
app/
  api/
    routes.py        # API router (GET /health)
  core/
    config.py        # .env loader + settings
  models/            # your ORM / domain models
  schemas/           # Pydantic schemas
  services/          # business logic / integrations
main.py              # FastAPI app entrypoint
requirements.txt
Dockerfile
docker-compose.yml
.env.example
```

## 🔧 Local Setup

```bash
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

- App will be available at http://127.0.0.1:8000
- Health check: http://127.0.0.1:8000/health
- Interactive docs: http://127.0.0.1:8000/docs

## 🐳 Docker (Dev)

```bash
docker compose up --build
```

- Hot-reloads via bind mount.
- Change ports or env in `docker-compose.yml`.

## 📝 Environment Variables

`app/core/config.py` loads `.env` (via `python-dotenv`) and exposes strongly-typed settings:

- `ENV` — current environment name (`development` by default)
- `HOST` — server host (default `0.0.0.0`)
- `PORT` — server port (default `8000`)
- `RELOAD` — enable auto-reload in dev (`true` by default)

Add your own variables to `.env` and access them through the `Settings` class.

## 👤 Author

**Viktor Kuznietsov*  
[GitHub](https://github.com/desaga)

---

## 📄 License

MIT
