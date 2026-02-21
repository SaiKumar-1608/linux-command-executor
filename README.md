# Linux Command Executor
A secure, full-stack web application that allows users to execute selected Linux commands from a browser-based terminal interface.
This project demonstrates:
 - Secure backend command execution
 - Controlled command whitelisting
 - Multi-line command handling
 - Command history tracking
 - Frontend directory simulation
 - API logging & monitoring
 - Cloud deployment (Render + Vercel)

## Overview
The Linux Command Executor provides a real-terminal-like experience inside a browser while maintaining strict backend security controls.

Users can:
  - Execute safe Linux commands
  - Run multiple commands line-by-line
  - View execution time
  - Navigate command history
  - View recent command history via API
The system is designed with security-first architecture to prevent arbitrary command execution.

## Architecture
```
Frontend (Vercel)
    │
    │ HTTP Requests
    ▼
Backend API (FastAPI - Render)
    │
    │ Secure Execution Layer
    ▼
System Shell (Whitelisted Commands Only)
```

## Tech Stack

- Frontend
  - HTML5
  - CSS3
  - Vanilla JavaScript
  - Deployed on Vercel

- Backend
  - FastAPI
  - Uvicorn
  - Pydantic
  - Loguru (Logging)
  - Python Subprocess (Secure Mode)
  - Deployed on Render

## Features

- Real Terminal Experience
  - Command prompt styling
  - Multi-line input support
  - Execution time display
  - Scrollable terminal
  - Smooth animations

- Command History
  - Arrow Up / Down navigation
  - Stores previously executed commands
  - Mimics real shell behavior

- Multi-Line Execution
Users can enter:
```
pwd
ls
whoami
```
Each command executes sequentially and displays output independently.

## Security Design

Security is the core of this project.

### Whitelisted Commands Only

Allowed commands example:
  - pwd
  - ls
  - ls -l
  - whoami
  - date
  - uptime
  - echo

Blocked:
  - rm
  - sudo
  - shutdown
  - cd (handled frontend)
  - Any unknown command
  
### No Shell Injection

Commands are validated before execution.
No raw shell=True injection allowed.

### CORS Protection

Configured to allow frontend domain access.

## Project Structure
```
linux-command-executor/
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   └── routes.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   └── schemas.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   └── validator.py
│   │   ├── utils/
│   │   │   ├── __init__.py
│   │   │   └── logger.py
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── main.py
│   ├── logs/
│   │   └── execution.log
│   ├── .env
│   ├── requirements.txt
│   └── runtime.txt
│
├── .gitignore
└── README.md

```

### Installation
1. Clone Repository:
```
git clone https://github.com/SaiKumar-1608/linux-command-executor.git
cd linux-command-executor
```
2. Backend Setup:
```
cd backend
python -m venv .venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate  # Mac/Linux

pip install -r requirements.txt
uvicorn app.main:app --reload
```
Backend runs at:
```
http://localhost:8000
```
3. Frontend Setup:

Simply open:
```
frontend/index.html
```
Or deploy to Vercel.

## Deployment

### Backend (Render)
- Web Service
- Root Directory: backend
- Build Command:
```
pip install -r requirements.txt
```
- Start Command:
```
uvicorn app.main:app --host 0.0.0.0 --port 10000
```
- Python Version: 3.11.9

### Frontend (Vercel)

- Import repository
- Root Directory: frontend
- No build command needed
- Set API URL to Render backend

## Learning Outcomes

This project demonstrates:

- Secure backend architecture
- REST API design
- CORS management
- Full-stack integration
- Deployment troubleshooting
- Production debugging
- Real-time command execution control
- Frontend state management

## Conclusion
The Linux Command Executor project demonstrates practical full-stack engineering with a strong focus on security, system design, and real-world deployment. Instead of simply building a browser-based terminal, the system implements a controlled execution architecture that validates and whitelists commands to prevent shell injection risks while maintaining a realistic user experience.

Technically, the project showcases secure API development with FastAPI, controlled subprocess execution, frontend terminal simulation with state management, CORS configuration, and successful cloud deployment using Render and Vercel. The deployment process involved production-level debugging, Python version management, environment configuration, and cross-origin handling.

Overall, this project highlights the ability to design secure systems, maintain clear frontend-backend separation, troubleshoot real-world deployment issues, and deliver a production-ready application beyond local development.



