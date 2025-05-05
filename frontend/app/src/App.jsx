import { BrowserRouter as Router, Routes, Route, Link, useNavigate } from 'react-router-dom';
import { useEffect, useState } from 'react';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';
import TodosPage from './pages/TodosPage';
import './App.css';

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(!!localStorage.getItem("access_token"));
  const [username, setUsername] = useState(localStorage.getItem("username") || "");

  const navigate = useNavigate();

  useEffect(() => {
    const storedUser = localStorage.getItem("username");
    if (storedUser) {
      setUsername(storedUser);
      setIsLoggedIn(true);
    }
  }, []);

  const handleLogout = () => {
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
    localStorage.removeItem("username");
    setIsLoggedIn(false);
    setUsername("");
    navigate("/login");
  };

  return (
    <>
      <nav className="navbar">
        <Link to="/">Todos</Link>
        <div className="navbar-left">
          {isLoggedIn && <span id='UserName'>Hello {username}!</span>}
          {!isLoggedIn && (
            <Link to="/login">
              <button className="btn">Login</button>
            </Link>
          )}
          {isLoggedIn && (
            <button className="btn" onClick={handleLogout}>Logout</button>
          )}
        </div>
      </nav>

      <Routes>
        <Route path="/" element={<TodosPage />} />
        <Route path="/login" element={<LoginPage onLoginSuccess={() => {
          setIsLoggedIn(true);
          setUsername(localStorage.getItem("username"));
        }} />} />
        <Route path="/register" element={<RegisterPage />} />
      </Routes>
    </>
  );
}

export default function AppWithRouter() {
  return (
    <Router>
      <App />
    </Router>
  );
}
