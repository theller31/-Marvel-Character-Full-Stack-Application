
# M7 Project: Marvel Character Manager (Full-Stack)

## Overview

This is a full-stack application built to interact with a pre-existing Flask + MySQL backend to manage Marvel characters. The project consists of a React frontend styled with React Bootstrap and a backend written in Flask with a MySQL database. This simulates a real-world scenario where the frontend is built to consume an already existing backend API.

---

## Backend Setup

### Provided Files
- `server.py`
- `requirements.txt`
- `marvel_characters.sql`

### Setup Instructions

1. **Folder Structure**
   - Project folder: `m7project`
   - Backend folder: `m7project/backend`

2. **Virtual Environment**
   ```bash
   cd m7project/backend
   python -m venv venv
   source venv/bin/activate  # Use `venv\Scripts\activate` on Windows
   pip install -r requirements.txt
   ```

3. **Update Database Credentials**
   In `server.py`, update the following:
   ```python
   app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:YOUR_PASSWORD@localhost/marvel'
   root_engine = create_engine("mysql+mysqlconnector://root:YOUR_PASSWORD@localhost")
   ```

4. **Run Backend Server**
   ```bash
   python server.py
   ```

5. **Load Marvel Characters**
   - Open MySQL Workbench.
   - Load and run `marvel_characters.sql` inside the `marvel` schema.

6. **Test the API**
   - Open browser at: `http://127.0.0.1:5000/characters`
   - You should see a JSON list of 10 Marvel characters.

---

## Frontend Setup

### React + React Bootstrap

1. **Create Frontend Project**
   - Inside `m7project`, run:
   ```bash
   npx create-react-app frontend
   cd frontend
   npm install react-router-dom axios react-bootstrap bootstrap
   ```

2. **Start Project**
   ```bash
   npm start
   ```

### Features Implemented
- 🧭 Navbar with mobile responsive support
- 🏠 Home page (separate from characters list)
- ⚠️ 404 page for undefined routes
- 📄 View All Characters
- 🔍 View Individual Character
- ➕ Create New Character
- 📝 Edit Character (with prefilled form)
- ❌ Delete Character
- ✅ Form validation & error handling
- ⏳ Loading and error UI states
- 📱 Mobile responsive design

---

## Folder Structure

```
m7project/
├── backend/
│   ├── server.py
│   ├── requirements.txt
│   └── marvel_characters.sql
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── App.tsx
│   │   └── index.tsx
└── README.md
```

---

## Technologies Used

### Backend:
- Python
- Flask
- Flask-SQLAlchemy
- MySQL

### Frontend:
- React
- TypeScript
- React Router DOM
- Axios
- React Bootstrap

---

## How to Use

- Navigate to the frontend and start the React app.
- View the list of Marvel characters.
- Use the interface to view, add, edit, or delete characters.
- Ensure backend is running locally at `http://127.0.0.1:5000`.

---

## Author

This project is a submission for Module 7 of the Coding Temple Bootcamp.
