import { GoPrincipal } from "../components/GoPrincipal"
import React, { useState, useEffect } from "react";
import { refreshAccessToken, checkTokenValidity } from "../service/AuthService";
import { CloseSession } from "../components/CloseSession";
import { Histories } from "../components/Histories";
import { Ordenes } from "../components/Ordenes";

export function XlabPage() {
  useEffect(() => {
    const verifyUser = async () => {
      const user = await checkTokenValidity();
    };
    verifyUser();
  }, []);

  return (
    <div>
      <CloseSession />
      <GoPrincipal />
 


        <div className="flex">
          <div className="w-1/5  border border-gray-500 p-2"><Histories /></div>
          <div className="w-4/5  border border-gray-500 p-2"><Ordenes /></div>
          
          
        </div>
      </div>



)
}