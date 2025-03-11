Para correr todo el proyecto ->>> npm start 
ingersamos "scripts": {
    "start": "concurrently \"cd backend && venv\\Scripts\\activate && uvicorn main:app --host 0.0.0.0 --port 8000 --reload\" \"cd frontend && npm run dev\" \"cd electron && npm start\""
  },
en pckage.json para inicializar el proyecto con un solo comando


