import { useState } from "react";
import axios from 'axios'

function LoginPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(null)

  const handleSubmit = async (e) => {
    e.preventDefault();
    //console.log("Login attempt:", { username, password });
    // Later, call the API here
    const formData = new URLSearchParams()
  formData.append("username", username)
  formData.append("password", password)
    try {
        const response = await axios.post("http://127.0.0.1:8000/auth/login", formData, {
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
          },
        })
    
        const { access_token } = response.data
        localStorage.setItem("token", access_token)
        console.log("Logged in successfully!")
      } catch (err) {
        console.error(err)
        setError("Invalid username or password")
      }
  };

  return (
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
  );
}

export default LoginPage;
