import type { InjectionKey } from 'vue'
import { createStore, useStore as baseUseStore, Store } from 'vuex'
import createPersistedState from 'vuex-persistedstate'
import { authStore } from './module/auth'
import type { AuthState } from './module/auth'
import { filterStore } from './module/filter'
import type { FilterState } from './module/filter'

export interface State {
    auth: AuthState,
    filter: FilterState
}

export const key: InjectionKey<Store<State>> = Symbol()

export const store: Store<State> = createStore({
    modules: {
        auth: authStore,
        filter: filterStore
    },
    plugins: [createPersistedState()]
})

export function useStore () {
    return baseUseStore(key)
}