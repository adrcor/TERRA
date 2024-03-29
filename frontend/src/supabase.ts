import { createClient } from '@supabase/supabase-js'
import { store, key } from '@/store'
import {api} from '@/api' 

const supabaseUrl = import.meta.env.VITE_SUPABASE_URL
const supabaseAnonKey = import.meta.env.VITE_SUPABASE_ANON_KEY


export const supabase = createClient(supabaseUrl, supabaseAnonKey)

export const isAuthenticated = async () => {
    const {data, error} = await supabase.auth.getSession()
    if (data.session == null) {
        if (store.state.auth.logedIn) {
            store.commit('auth/unsetUser')
        }
        return false

    } else {
        if (store.state.auth.idUser !== data.session.user.id) {
            store.commit('auth/setIdUser', data.session.user.id)
        }
        return true
    }
}

async function setUsername() {
    const response = await api.get('/user/get-username')
    const username = response.data.username
    store.commit('auth/setUsername', username)
} 

export const getJwt = async () => {
    const {data, error} = await supabase.auth.getSession()

    if (data.session == null) {
        return null

    } else {
        return data.session.access_token
    }
}