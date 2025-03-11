import { useNavigate } from "react-router-dom";  

import { Button, Card, Checkbox, Label, TextInput } from "flowbite-react";
import "./ui/Login.css";
import React, { useState, useEffect } from "react";

import { login } from "../service/AuthService"; 

export function LoginPage() {
  const navigate = useNavigate();
  const [userLogin, setUserLogin] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const labNit = 2;

  useEffect(() => {
    // Limpiar los campos al montar o cuando se navega a esta página
    setUserLogin("");
    setPassword("");
    setError("");
    
    // Forzar un reenfoque al campo de usuario
    const userLoginInput = document.getElementById('userLogin');
    if (userLoginInput) {
      userLoginInput.focus();
    }
  }, []);
  
  const handleLogin = async (e) => {
    e.preventDefault();
    const isSuccess = await login(userLogin, password, labNit);
    if (isSuccess) {
      sessionStorage.setItem('userLogin', userLogin);
      navigate("/principalPage");
    } else {
      setError("Credenciales incorrectas");
      //await event_register('Login', 'Ingreso a sessionLogin: cc y pass', false, String(usrIdentification), '', 'APPUSERS', '');
    }
  };

  return (
    <div className="flex justify-center items-center h-screen bg-gradient-to-br from-gray-100 to-gray-300">

      <Card className="max-w-md w-full shadow-lg rounded-lg relative">

        <div className="div-login">
          <h2 className="text-3xl font-extrabold text-center mb-6 text-gray-800">
            Iniciar Sesión
          </h2>
          <form className="flex flex-col gap-4" onSubmit={handleLogin}>
            <div>
              <Label htmlFor="userLogin" value="Usuario" className="text-gray-700" />
              <TextInput
                id="userLogin"
                type="text"
                placeholder="Ingresa tu usuario"
                value={userLogin}
                onChange={(e) => setUserLogin(e.target.value)}
                required
                className="bg-gray-50 border border-gray-300 rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500"
              />
            </div>
            <div>
              <Label htmlFor="password" value="Contraseña" className="text-gray-700" />
              <TextInput
                id="password"
                type="password"
                placeholder="Ingresa tu contraseña"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
                className="bg-gray-50 border border-gray-300 rounded-lg shadow-sm focus:ring-blue-500 focus:border-blue-500"
              />
            </div>
    
            <Button
              type="submit"
              className="w-full bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg py-2.5 shadow-md"
            >
              Iniciar Sesión
            </Button>
          </form>

        </div>
      </Card>
    </div>
  )

}