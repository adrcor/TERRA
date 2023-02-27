import axios from 'axios'

const apiUrl = import.meta.env.VITE_BACKEND_URL

const api = axios.create({
    baseURL: apiUrl,
})

export { api }