import { useNavigate } from "react-router-dom";
import { Button } from "flowbite-react";
import { refreshAccessToken } from "../service/AuthService"; // Importa la función de refresh

export function Navigation() {
    const navigate = useNavigate();
    
    const handleNavigation = async () => {
        // Primero refrescamos el token
        const newToken = await refreshAccessToken();
        
        // Solo navegamos si el token fue refrescado correctamente
        if (newToken) {
            navigate("/XlabPage");
        } else {
            // Si hay error al refrescar, puedes mostrar un mensaje o redirigir al login
            console.error("No se pudo refrescar el token");
            // Opcional: redirigir al login
            // navigate("/");
        }
    };

    return (
        <div>
            <Button 
                onClick={handleNavigation}
                className="bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg"
            >
                Xlab
            </Button>
        </div>
    )
}