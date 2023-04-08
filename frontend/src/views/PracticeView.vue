<template>
    <div class="flex flex-col flex-1 p-2 mb-16 justify-center items-center gap-4 w-2/3">
        <div class="flex flex-col flex-1 items-center gap-2 h-fit justify-end">
            <PracticeFilter @filter-update="onFilterUpdate"/>
            <Grades :data="data" :region="region"/>
        </div>
        <div class="flex flex-col items-center w-full">
            <Stats :data="data"/>
            <MainPractice ref="refMainPractice" @end-test="onEndTest"/>
        </div>
        <div class="flex-1"></div>
    </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { api } from '@/api';
import PracticeFilter from '@/components/practice/PracticeFilter.vue';
import Grades from '@/components/practice/Grades.vue';
import type { PracticeData, PracticeHisto, Region } from '@/models';
import Stats from '@/components/practice/Stats.vue';
import MainPractice from '@/components/practice/MainPractice.vue';

onMounted(() => {
    updateData()
    addEventListener('keydown', eventListener)
})

const region = ref<Region>('AF')
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

function onTab() {
    if (!data) {
        return
    }
    refMainPractice.value?.resetTest()
    refMainPractice.value?.launchTest(data.value, region.value)
}

function onEscape() {
    refMainPractice.value?.resetTest()
}

function onFilterUpdate(r: Region) {
    region.value = r
    updateData()
}

async function updateData() {
    data.value = null
    const response = await api.get(`practice/data/${region.value}`)
    data.value = response.data
}

async function onEndTest(histo: PracticeHisto[], r: Region) {
    const response = await api.post(`practice/update/${r}`, {
        params: histo
    })
    data.value = response.data
}

</script>