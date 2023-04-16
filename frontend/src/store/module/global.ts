export interface GlobalState {
    testRunning: boolean,
    endTestScreen: boolean
}

export const globalStore = {
    namespaced: true,

    state: {
        testRunning: false,
        endTestScreen: false
    } as GlobalState,

    mutations: {
        setTestRunning(state: GlobalState, value: boolean) {
            state.testRunning = value
        },
        setEndTestScreen(state: GlobalState, value: boolean) {
            state.endTestScreen = value
        }
    }
}