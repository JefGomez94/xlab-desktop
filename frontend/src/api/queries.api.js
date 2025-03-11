import axios from "axios";

const DOMINIO_BACK = "http://localhost:9000";


export const loginUser = (userLogin, password, labNit) => {
    return axios.post(`${DOMINIO_BACK}/login/get_login/`, {
        'userLogin': userLogin,
        'password': password, 
        'labNit': labNit
    });
};

export const get_User = (token) => {
    return axios.get(`${DOMINIO_BACK}/login/get_User/`, {
        headers: { Authorization: `Bearer ${token}` },
      });
};

export const get_Refresh = (refreshToken) => {
    return axios.post(`${DOMINIO_BACK}/login/token/refresh/`, {
      refresh: refreshToken,
    });
}