import { useNavigate } from "react-router-dom";
import { Button } from "flowbite-react";
import { logout } from "../service/AuthService";

export function CloseSession() {
    const navigate = useNavigate();
    
    const handleLogout = async () => {
        await logout();
        //navigate("/");  // Aquí usamos navigate después del logout
    };

    return (
        <div>
            <Button
                onClick={handleLogout}
                className="bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg"
            >
                Cerrar sesión
            </Button>
        </div>
    )
}