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

## 👤 Author

**Viktor Kuznietsov*  
[GitHub](https://github.com/desaga)

---

## 📄 License

MIT
