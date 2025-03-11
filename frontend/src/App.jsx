import { HashRouter, Routes, Route, Navigate } from "react-router-dom";
import { PrincipalPage } from "./pages/PrincipalPage";
import { XlabPage } from "./pages/XlabPage";
import { LoginPage } from "./pages/LoginPage";
import { PrivateRoute } from './components/PrivateRoute';

function App() {
  return (
    
    <HashRouter>
      <Routes>
        <Route path="/" element={<LoginPage />} />
        <Route path="/principalPage" 
        element={
          <PrivateRoute> 
            <PrincipalPage /> 
          </PrivateRoute>
          }/>
        <Route path="/xlabPage" 
        element={
          <PrivateRoute>
            <XlabPage />
          </PrivateRoute>
        }/>
      </Routes>
    </HashRouter>
  );
}

export default App;