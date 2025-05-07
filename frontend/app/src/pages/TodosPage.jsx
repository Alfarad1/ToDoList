import React, { useEffect, useState } from "react";
import api from "../axiosConfig";

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
    <>
    <div className="maincontainer">
        <div className="addtodo">
          <h2>Add a Todo:</h2>
          <form action="">
          <input type="text" 
          placeholder="Todo's title"
          />
          <textarea class='BigText'type="text" 
          placeholder="Todo's desctiption"
          />
          <button type="submit" id='newTodoSubmit'>Submit</button>
          </form>
        </div>
        <div class="listitems">
          <h2>Your Todo's:</h2>
          {error && <p style={{ color: "red" }}>{error}</p>}
          <ul>
            {todos.map((todo) => (
              <li key={todo.id}>
                <strong>{todo.title}</strong> <br /> {todo.description}
              </li>
            ))}
          </ul>
        </div>
      </div>
    </>
  );
};

export default TodosPage;
