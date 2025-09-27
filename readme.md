
# ToDo-Python-Django

A simple but fully functional To-Do app built with **Python** and **Django**.  
Allows users to create, read, update, and delete to-do items via a web interface.  

---

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

---

## Live Demo (Deployed App)
**Experience the application instantly! Click the link below to interact with the live, deployed version of the To-Do application.**


🔗  **[Live Demo Link](https://todo-slbw.onrender.com/)**

---
## Features

- Add new to-do items  
- Mark items as completed / not completed  
- Edit existing to-do items  
- Delete to-do items  
- Simple web interface (forms + templates)  
- Persist data using Django’s ORM  

---
## Tech Stack

| Component            | Used Technology            |
|----------------------|-----------------------------|
| Backend              | Python, Django             |
| Templates / Frontend | Django Templates, HTML, CSS |
| Database             | SQLite (default) |
| License              | MIT                         |

---

## Getting Started

- ### Prerequisites

    - Python 3.x installed  
    - `pip` (Python package manager)  
    - Virtual environment tool (`venv` or `virtualenv`)  

---

- ### Installation

    1. **Clone the repository**  
        ```bash
        git clone https://github.com/ft-mammoo/ToDo-Python-Django.git
        cd ToDo-Python-Django
        ```
    2. **Create virtual environment**
        ```bash
        python3 -m venv venv
        ```
    3. **Activate virtual environment**
        ```bash
        source venv/bin/activate    # On macOS / Linux
        ```
        **OR**
        ```bash
        venv\Scripts\activate       # On Windows
        ```
    4. **Install dependencies**
        ```bash
        pip install -r requirements.txt
        ```
    5. **Apply Django migrations**
        ```bash
        python manage.py migrate
        ```
---



- ### Run Locally

    ```bash
    python manage.py runserver
    ```
    **Then open your browser and navigate to http://127.0.0.1:8000/**
---


## Contributing

****Contributions are always welcome!*** *Here’s how you can help:**

- **Raise issues for bugs or feature requests**

- **Submit pull requests (fork → changes → PR)**

- **Suggest improvements in UI, backend logic, or structure**

- **Add tests, better error handling, or documentation**

****Please adhere to code style and provide descriptive commit message****
---