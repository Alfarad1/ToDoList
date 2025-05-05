import React, { useEffect, useState } from "react";
import api from "../axiosConfig";
// import './App.css';

const TodosPage = () => {
  const [todos, setTodos] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchTodos = async () => {
      const token = localStorage.getItem("access_token");

      if (!token) {
        setError("No token found. Please log in.");
        return;
      }

      try {
        const response = await api.get("http://127.0.0.1:8000/todos", {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });

        setTodos(response.data);
      } catch (err) {
        console.error(err);
        setError(err.response?.data?.detail || "Failed to fetch todos");
      }
    };

    fetchTodos();
  }, []);

  return (
    <div>
      <h2>Your Todos</h2>
      {error && <p style={{ color: "red" }}>{error}</p>}
      <ul>
        {todos.map((todo) => (
          <li key={todo.id}>
            <strong>{todo.title}</strong> — {todo.description}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TodosPage;
