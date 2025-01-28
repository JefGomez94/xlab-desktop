import React, { useEffect, useState } from "react";
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [data, setData] = useState("");

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/api/data")
      .then((response) => setData(response.data.message))
      .catch((error) => console.error(error));
  }, []);

  return <div>{data ? <h1>{data}</h1> : <h1>Cargando...</h1>}</div>;
}

export default App;
