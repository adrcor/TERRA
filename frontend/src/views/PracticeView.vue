<template>
    <div class="flex flex-col flex-1 p-2 mb-4 justify-center items-center gap-4 w-2/3">
        <div class="flex flex-col flex-1 items-center gap-2 h-fit justify-end">
            <PracticeFilter />
            <Grades :data="data"/>
        </div>
        <div class="flex flex-col items-center w-full">
            <Stats :data="data"/>
            <MainPractice ref="refMainPractice" @end-test="onEndTest"/>
        </div>
        <button class="w-6 h-6 opacity-40" @click="onTab">
            <img src="@/assets/icons/solid/play.svg"/>
        </button>
        <div class="flex-1 w-2"></div>
    </div>
</template>

<script setup lang="ts">
import { onMounted, ref, watch } from 'vue'
import { api } from '@/api'
import PracticeFilter from '@/components/practice/PracticeFilter.vue'
import Grades from '@/components/practice/Grades.vue'
import type { PracticeData, PracticeHisto, Region } from '@/models'
import Stats from '@/components/practice/Stats.vue'
import MainPractice from '@/components/practice/MainPractice.vue'
import { useStore } from '@/store'

onMounted(() => {
    updateData()
    addEventListener('keydown', eventListener)
})

const store = useStore()

const data = ref<PracticeData[] | null>(null)

const refMainPractice = ref<InstanceType<typeof MainPractice>>()

function eventListener(event: KeyboardEvent) {
    if (event.key == 'Tab') {
        event.preventDefault()
        event.stopPropagation()
        onTab()
    }
    if (event.key == 'Escape') {
        onEscape()
    }
}

watch(() => store.state.practice.region, updateData)

function onTab() {
    if (!data) {
        return
    }
    refMainPractice.value?.resetTest()
    refMainPractice.value?.launchTest(data.value, store.state.practice.region)
}

function onEscape() {
    refMainPractice.value?.resetTest()
}


async function updateData() {
    data.value = null
    const response = await api.get(`practice/data/${store.state.practice.region}`)
    data.value = response.data
}

async function onEndTest(histo: PracticeHisto[], r: Region) {
    const response = await api.post(`practice/update/${r}`, {
        params: histo
    })
    data.value = response.data
}

</script>