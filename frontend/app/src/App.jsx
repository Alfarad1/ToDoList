import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Link } from 'react-router-dom';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';
import TodosPage from './pages/TodosPage';
import './App.css';

const handleLogout = () => {
  localStorage.removeItem("token");
  window.location.href = "/login";
};

function App() {
  return (
    <Router>
      <nav class="navbar">
        <Link to="/">Todos</Link>{" "}
        <a id='UserName'>UserName</a>
        {/* <Link class="Login" to="/login">Login</Link>{" "} */}
        <Link class="Login" to='/login'><button class="btn">Login</button></Link>
        <button class="btn Logout" onClick={handleLogout}>Logout</button>
      </nav>

      <Routes>
        <Route path="/" element={<TodosPage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<RegisterPage />} />
      </Routes>
    </Router>
  );
}

export default App;