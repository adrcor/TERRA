import type { Region } from "@/models"

export interface PracticeState {
    region: Region
}

export const practiceStore = {
    namespaced: true,

    state: {
        region: 'AF'
    } as PracticeState,

    mutations: {
        set_region(state: PracticeState, region: Region) {
            state.region = region
        }
    }
}