import type { InjectionKey } from 'vue'
import { createStore, useStore as baseUseStore, Store } from 'vuex'
import createPersistedState from 'vuex-persistedstate'
import { authStore } from './module/auth'
import type { AuthState } from './module/auth'

export interface State {
    auth: AuthState
}

export const key: InjectionKey<Store<State>> = Symbol()

export const store: Store<State> = createStore({
    modules: {
        auth: authStore
    },
    plugins: [createPersistedState()]
})

export function useStore () {
    return baseUseStore(key)
}