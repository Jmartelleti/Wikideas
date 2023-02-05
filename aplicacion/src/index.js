import React from "react"; //se encarga de crear los componentes
import ReactDOM from "react-dom/client"; //se encarga de insertarlos en el html

import App from "./App";
import "bootstrap/dist/css/bootstrap.min.css";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App/>
  </React.StrictMode>
);
