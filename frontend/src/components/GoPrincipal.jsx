import { Link } from "react-router-dom";

export function GoPrincipal() {

    return (
        <div>
            <Link to="/principalPage">
                <h1>Ir al inicio</h1>
            </Link>
        </div>
    )
}