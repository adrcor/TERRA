import axios from 'axios'

const apiUrl = import.meta.env.VITE_BACKEND_URL

const api = axios.create({
    baseURL: apiUrl,
    withCredentials: true
})

api.interceptors.request.use(
    async config => {
        config.headers['Authorization'] = `Bearer test`;
        return config;
    },
    error => {
        return Promise.reject(error);
    }
)

export { api }