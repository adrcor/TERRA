import type { InjectionKey } from 'vue'
import { createStore, useStore as baseUseStore, Store } from 'vuex'
import createPersistedState from 'vuex-persistedstate'
import { authStore, type AuthState } from './module/auth'
import { filterStore, type FilterState } from './module/filter'
import { globalStore, type GlobalState } from './module/global'
import { practiceStore, type PracticeState } from './module/practice'

export interface State {
    auth: AuthState,
    filter: FilterState,
    global: GlobalState,
    practice: PracticeState
}

export const key: InjectionKey<Store<State>> = Symbol()

export const store: Store<State> = createStore({
    modules: {
        auth: authStore,
        filter: filterStore,
        global: globalStore,
        practice: practiceStore
    },
    plugins: [createPersistedState()]
})

export function useStore() {
    return baseUseStore(key)
}