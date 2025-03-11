import { Link } from "react-router-dom";
import { Navigation } from "../components/Navigation";
import { CloseSession } from "../components/CloseSession";

import { refreshAccessToken, checkTokenValidity } from "../service/AuthService";
import React, { useState, useEffect } from "react";

export function PrincipalPage() {
  useEffect(() => {
    const verifyUser = async () => {
        const user = await checkTokenValidity();
    };
    verifyUser();
}, []);


  return (
    <div><CloseSession />
      <h1>Laboratorios Louis Pasteur</h1>
      <Navigation />
      
    </div>
  )
}