import { loginUser, get_User, get_Refresh } from "../api/queries.api"
import { Navigate } from 'react-router-dom';
import { useNavigate } from "react-router-dom";


//Solicitamos token al backend
export const login = async (user_Login, password, labNit) => {
  try {
    console.log(user_Login, password, labNit);
    const response = await loginUser(user_Login, password, labNit);
    console.log("Access Token recibido en login:", response.data);

    if (response.data.access && response.data.refresh) {

      setTokens(response.data.access, response.data.refresh);
      return true;
    }
  } catch (error) {
    console.error('Error al iniciar sesión:', error);
    return false;
  }
};

// Función para refrescar el token
export const refreshAccessToken = async () => {
  console.log("refreshAccessToken")
  const refreshToken = getRefreshToken();
  if (!refreshToken) {
    console.error("No hay token de refresco");
    logout();
    return null;
  }

  try {
    const response = await get_Refresh(refreshToken);
    
    const newAccessToken = response.data.access;
    setTokens(newAccessToken, refreshToken);

    return newAccessToken;
  } catch (error) {
    console.error("Error al refrescar el token:", error);
    logout();
    return null;
  }
};

// Guardar los tokens en localStorage
export const setTokens = (accessToken, refreshToken) => {
  // Verifica si el token tiene espacios o caracteres extraños
  if (!accessToken || !refreshToken) {
    console.error("Tokens no válidos");
    return;
  }
  localStorage.setItem('token', accessToken.trim());
  localStorage.setItem('refreshToken', refreshToken.trim());
};

// Obtener el token de acceso desde el localStorage
export const getAccessToken = () => {
  const token = localStorage.getItem('token');
  //console.log("Token obtenido de localStorage:", token);
  return token ? token.trim() : null;
};// Obtener el token de refresco desde el localStorage
export const getRefreshToken = () => localStorage.getItem('refreshToken');




//Checkeamos token
export const checkTokenValidity = async () => {
  try {
      console.log("checkTokenValidity");
      const user = await getUser();   //Buscamos el usuario logeado en base de datos
      
      // Return false if user is undefined
      if (user === undefined) {
          console.error("Usuario no definido. Cerrando sesión...");
          alert("Su sesión a finalizado por favor ingrese de nuevo");
          logout();
          return false;
      }
      
      return user !== null; // Si `getUser` devuelve datos, el token es válido
  } catch (error) {
      console.error("Token inválido o expirado. Cerrando sesión...");
      logout(); // Llama a la función logout automáticamente
      return false; // Devuelve `false` para indicar token inválido
  }
};

// Eliminar los tokens (cerrar sesión)
export const logout = async () => {
  //const usrLogin = sessionStorage.getItem('usrLogin');
  
  //await event_register('Logout', 'Salir de interfaz de usuario', true, String(usrLogin), '', '', '');
  localStorage.removeItem('token');
  localStorage.removeItem('refreshToken');
  window.location.hash = '/';
};

export const getUser = async () => {
  let token = getAccessToken();
  if (!token) {
    console.error("Token no encontrado");
    return null;
  }

  try {
    const response = await get_User(token);

    return response.data;
  }  catch (error) {
    logout();
  }
};
