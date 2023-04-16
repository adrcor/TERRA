
export interface AuthState {
    idUser: string | null,
    logedIn: boolean
}

export const authStore = {
    namespaced: true,
    
    state: {
        idUser: null,
        logedIn: false
    } as AuthState,

    mutations: {
        setIdUser(state: AuthState, idUser: string) {
            state.idUser = idUser
            state.logedIn = true
        },
        unsetUser(state: AuthState) {
            state.idUser = null
            state.logedIn = false
        }
    }
}