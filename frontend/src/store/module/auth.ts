
interface AuthState {
    idUser: string | null,
    username: string | null,
    logedIn: boolean
}

export default {
    namespaced: true,
    
    state: {
        idUser: null,
        username: null,
        logedIn: false
    } as AuthState,

    mutations: {
        setIdUser(state: AuthState, idUser: string) {
            state.idUser = idUser
            state.logedIn = true
        },
        setUsername(state: AuthState, username: string) {
            state.username = username
        },
        unsetUser(state: AuthState) {
            state.idUser = null
            state.logedIn = false
            state.username = null
        }
    },
    getters: {
        getLogedIn (state: AuthState): boolean {
            return state.logedIn
        },
        getUsername (state: AuthState): string | null {
            return state.username
        }
    }
}