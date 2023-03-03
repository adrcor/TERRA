import { createStore } from 'vuex'
import createPersistedState from 'vuex-persistedstate'
import auth from './module/auth'

export default createStore({
    modules: {
        auth
    },
    plugins: [createPersistedState()]
})