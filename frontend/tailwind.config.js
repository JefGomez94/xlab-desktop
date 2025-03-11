/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",      // Para que TailwindCSS funcione en tus archivos src
    "node_modules/flowbite-react/**/*.{js,jsx,ts,tsx}", // Para que Flowbite funcione
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require("flowbite/plugin"),
  ],
};