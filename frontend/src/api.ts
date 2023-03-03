import axios from 'axios'
import { getJwt } from '@/supabase'

const apiUrl = import.meta.env.VITE_BACKEND_URL

const api = axios.create({
    baseURL: apiUrl,
    withCredentials: true
})

api.interceptors.request.use(
    async config => {
        config.headers['Authorization'] = `Bearer ${await getJwt()}`;
        return config;
    },
    error => {
        return Promise.reject(error);
    }
)

export { api }