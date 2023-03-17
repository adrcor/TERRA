export interface FilterState {
    length: number,
    region: string
}

export const filterStore = {
    namespaced: true,

    state: {
        length: 10,
        region: 'World'
    } as FilterState,

    mutations: {
        set_length(state: FilterState, length: number) {
            state.length = length
        },
        set_region(state: FilterState, region: string) {
            state.region = region
        }
    }
}