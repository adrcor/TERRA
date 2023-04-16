<template>
    <div class="flex flex-col rounded-lg bg-overlay bg-opacity-5">
        <div class="flex flex-row justify-around text-on-background">
            <button v-for="item in regions" class="flex-1 py-4 rounded-lg bg-overlay bg-opacity-0 hover:bg-opacity-5 hover:text-opacity-100 transition-all" :class="{'text-primary text-opacity-100 bg-opacity-5': item == activeRegion, 'text-overlay text-opacity-60': item != activeRegion}" @click="activeRegion=item">{{ item }}</button>
        </div>
        <div class="flex flex-row justify-around text-on-background">
            <HighscoreCard v-for="length in lengths" @on-click="onClick" :test="highscores[activeRegion][length]" :length="length" :selected="activeRegion == selectedRegion && length == selectedLength"/>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { listRegion, listLength, type Region, type Length } from '@/models'
import type { TestDb } from '@/models'
import { api } from '@/api'
import { useStore } from '@/store'
import HighscoreCard from './HighscoreCard.vue'

const emits = defineEmits([
    'on-select'
])

const regions: Region[] = listRegion
const lengths: Length[] = listLength

type Highscores = {
    [key in Region]: {[key in Length]: TestDb | null}
}

const store = useStore() 

const activeRegion = ref<Region>(store.state.filter.region)
const selectedRegion = ref<Region>(store.state.filter.region)
const selectedLength = ref<Length>(store.state.filter.length)

const highscores = ref<Highscores>(regions.reduce((o, key) => ({...o, [key]: lengths.reduce((o, key) => ({ ...o, [key]: null }), {}) }), {}) as Highscores)

onMounted(getHighscore)

async function getHighscore() {
    const response = await api.get('highscore/get-all')
    response.data.forEach((test: TestDb) => {
        highscores.value[test.region as Region][test.length as Length] = test
    })
}

function onClick(region: Region, length: Length) {
    selectedRegion.value = region
    selectedLength.value = length
    emits('on-select', region, length)
}

</script>