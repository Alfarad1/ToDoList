# 📝 Веб-приложение "Список дел"

Фуллстек **Веб-приложение "Список дел"**, бэкенд выполнен на **FastAPI** (Python), фронтенд на **React + Vite**. Данное веб-приложение реализованно в качестве пет-проекта.

---

## 🚀 Особенности

### ✅ Бэкенд (FastAPI)
- JWT авторизация с **access и refresh токенами**
- Ролевой доступ
- CRUD операции:
  - Пользователи (admin only)
  - Списки дел (для пользователя)
  - Пункты (задачи внутри списка дел)
- PostgreSQL БД с SQLAlchemy ORM
- Alembic миграции
- Инъекция зависимостей для авторизации

### 🌐 Фронтенд (React + Vite)
- Страницы регистрации, входа и просмотра списков дел
- Работа с токенами
- Создание и управление списками дел и пунктами с помощью форм
- Отзывчивый интерфейс

---

## 🛠️ Стек

- **Бэкенд:** FastAPI, SQLAlchemy, Alembic, PostgreSQL
- **Авторизация:** OAuth2 with Password Flow + JWT (access & refresh tokens)
- **Фронтенд:** React, Vite, Axios
- **Инструменты разработки:** Docker, uvicorn, npm

---

# 📝 Todo List App

A full-stack **Todo List App** built with **FastAPI** (Python) on the backend and **React + Vite** on the frontend. Designed as a pet project to explore modern web development, authentication systems, and REST API design.

---

## 🚀 Features

### ✅ Backend (FastAPI)
- JWT authentication with **access & refresh tokens**
- Role-based access (user / admin)
- CRUD operations for:
  - Users (admin only)
  - Todos (per user)
  - Tasks (sub-items of todos)
- PostgreSQL database with SQLAlchemy ORM
- Alembic migrations
- Dependency-injected security and authorization

### 🌐 Frontend (React + Vite)
- Login/logout functionality
- Auth token handling (with refresh flow)
- Form-driven creation & editing of todos/tasks
- Responsive UI (using [your styling solution, e.g., Tailwind, plain CSS])

---

## 🛠️ Tech Stack

- **Backend:** FastAPI, SQLAlchemy, Alembic, PostgreSQL
- **Auth:** OAuth2 with Password Flow + JWT (access & refresh tokens)
- **Frontend:** React, Vite, Axios
- **Dev Tools:** Docker (optional), uvicorn, npm
