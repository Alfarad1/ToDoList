import { useState } from "react";
import api from "../axiosConfig";

function RegisterPage() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [email, setEmail] = useState("");
    const [name, setName] = useState("");
    const [error, setError] = useState(null)

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const response = await api.post("http://127.0.0.1:8000/users",
                {
                    username,
                    password,
                    email,
                    name
                }
            )
            
            
          } catch (err) {
            console.error(err)
            setError(response)
            
          }
        };
        return (
            <div>
        <form onSubmit={handleSubmit} className="">
          <input
            type="text"
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <input
            type="email"
            placeholder="E-mail"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          <input
            type="text"
            placeholder="Name (Optional)"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
          <button type="submit" className="bg-blue-500 text-white p-2 rounded">
            Login
          </button>
          {error && <p className="text-red-500">{error}</p>}
        </form>
        </div>
  );
}
  
export default RegisterPage;