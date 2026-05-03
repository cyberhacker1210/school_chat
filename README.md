# school_chat — Real-Time Chat & Class Schedule Web App

A Django web application built for school use, combining a real-time group chat and a class schedule viewer. Messages are stored in a database and refreshed every 500ms via AJAX polling. The app also includes a timetable that automatically displays the correct week (odd/even) for each student group.

## Tech Stack

| Technology | Usage |
|---|---|
| Python 3 | Main language |
| Django 4.2 | Web framework |
| Django Channels | WebSocket support (ASGI) |
| SQLite | Database (via Django ORM) |
| jQuery / AJAX | Real-time message polling |
| HTML / CSS | Frontend templates |

## Features

**Chat module (`/chat`)**
- Enter a username and join a shared room
- Messages sent via AJAX POST, stored in the database (`Message` model)
- Messages fetched every 500ms via AJAX GET — no page reload needed
- Auto-scroll to latest message if already at the bottom
- Timestamps formatted in French locale (`fr-FR`)

**Planning module (`/blog`)**
- Displays the weekly class schedule as a timetable grid
- Automatically detects odd/even week number to show the right schedule
- Separate views for group 1 and group 2 (`/planning-g1`, `/planning-g2`)
- Days ordered Monday → Sunday, hours from 8h30 to 15h30

## Project Structure

```
school_chat-master/
└── site_leo/
    ├── manage.py
    ├── db.sqlite3
    ├── chat/                        # Chat module
    │   ├── models.py                # Room and Message models
    │   ├── views.py                 # home, room, send, getMessages
    │   ├── consumers.py             # Django Channels WebSocket consumer
    │   ├── routing.py               # WebSocket URL routing (ws/chat/)
    │   └── urls.py
    ├── blog/                        # Planning module
    │   ├── models.py                # Planning and Classe models
    │   ├── views.py                 # index, planning_g1 (odd/even week logic)
    │   └── templates/blog/
    │       └── planning.html        # Timetable grid template
    └── site_leo/                    # Django project config
        ├── settings.py
        ├── urls.py
        ├── asgi.py                  # ASGI entry point (Channels)
        ├── routing.py               # ProtocolTypeRouter
        └── templates/chat/
            ├── home.html            # Username entry form
            └── room.html            # Chat room with AJAX polling
```

## Data Models

**Chat**
- `Room` — a chat room identified by name
- `Message` — stores message content, author username, room reference, and timestamp

**Planning**
- `Planning` — one slot: day (`jour`), time (`heure`), subject (`matiere`), week type (`semaine`: 0/1/2), group (`groupe`)
- `Classe` — a class linked to a planning entry

## Getting Started

**Prerequisites:** Python 3.8+, pip

```bash
git clone https://github.com/cyberhacker1210/school_chat
cd school_chat/site_leo

pip install django channels
```

```bash
python manage.py migrate
python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000)

### Available routes

| URL | Description |
|---|---|
| `/` | Home / index |
| `/chat/` | Chat — username entry |
| `/<room>/` | Chat room |
| `/send` | POST — save a message |
| `/getMessages/<room>/` | GET — fetch messages as JSON |
| `/blog/` | Class schedule (group 2) |
| `/blog/planning-g1/` | Class schedule (group 1) |
| `/admin/` | Django admin |

### Load schedule data

Schedule entries must be added via the Django admin panel or a data fixture. Each `Planning` entry needs: `jour`, `heure`, `matiere`, `semaine` (0 = all weeks, 1 = odd, 2 = even), `groupe` (1 or 2).

```bash
python manage.py createsuperuser
# then go to /admin to add Planning entries
```

## Notes

- The WebSocket consumer (`consumers.py`) is wired up but the chat currently uses AJAX polling rather than WebSocket push — the Channels infrastructure is in place for a future upgrade.
- `DEBUG = True` and `ALLOWED_HOSTS = []` — do not deploy as-is to production.
- The `SECRET_KEY` in `settings.py` is the default insecure one — replace it before any deployment.

## Author

**cyberhacker1210** — [GitHub](https://github.com/cyberhacker1210)
