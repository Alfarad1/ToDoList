import { useState } from "react";
import api from "../axiosConfig";
import { useNavigate } from "react-router-dom";

function LoginPage({ onLoginSuccess }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(null)
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    //console.log("Login attempt:", { username, password });
    // Later, call the API here
    const formData = new URLSearchParams()
    formData.append("username", username)
    formData.append("password", password)
    if (username === '' || password === ''){
      setError("Fill in the username and password fields!");
    }
    else {
      try {
        const response = await api.post("http://127.0.0.1:8000/auth/login", formData, {
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
          },
        })
        localStorage.setItem("access_token", response.data.access_token)
        localStorage.setItem("refresh_token", response.data.refresh_token)
        localStorage.setItem("username", username)
        onLoginSuccess();
        console.log("Logged in successfully!")
        navigate("/");
      } catch (err) {
        console.error(err)
        setError("Invalid username or password")
      }
    }
  };

  return (
    <>
    <div className="loginpage container">
      <p>Log in:</p>
      <form onSubmit={handleSubmit} className="flex flex-col gap-4 w-80 mx-auto mt-10">
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          className="border p-2 rounded"
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="border p-2 rounded"
        />
        <button type="submit" className="bg-blue-500 text-white p-2 rounded">
          Login
        </button>
        {error && <p className="text-red-500">{error}</p>}
      </form>
      <p>If you don't have an account, please register at <a href="/register">Sign Up</a>!</p>
      </div>
    </>
  );
}

export default LoginPage;
