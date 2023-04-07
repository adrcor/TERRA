import type { Region, Length } from "@/models"

export interface FilterState {
    length: Length,
    region: Region
}

export const filterStore = {
    namespaced: true,

    state: {
        length: 10,
        region: 'World'
    } as FilterState,

    mutations: {
        set_length(state: FilterState, length: Length) {
            state.length = length
        },
        set_region(state: FilterState, region: Region) {
            state.region = region
        }
    }
}