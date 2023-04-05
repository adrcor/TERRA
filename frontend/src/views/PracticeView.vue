<template>
    <div class="flex flex-col flex-1 p-2 mb-16 justify-center items-center gap-4">
        <Grades :data="data" @hovered-data="onHoveredData"/>
        <div class="flex flex-row items-center gap-2">
            <PracticeFilter @filter-update="onFilterUpdate"/>
            <Stats :data="data" :hoveredData="hoveredData"/>
        </div>
        <MainPractice ref="refMainPractice" @end-test="onEndTest"/>
    </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { api } from '@/api';
import PracticeFilter from '@/components/practice/PracticeFilter.vue';
import Grades from '@/components/practice/Grades.vue';
import type { PracticeData } from '@/models';
import Stats from '@/components/practice/Stats.vue';
import MainPractice from '@/components/practice/MainPractice.vue';

onMounted(() => {
    getData('af')
    addEventListener('keydown', eventListener)
})

var region = 'af'
const data = ref<PracticeData[] | null>(null)
const hoveredData = ref<PracticeData | null>(null)

const refMainPractice = ref<InstanceType<typeof MainPractice>>()

function onHoveredData(obj: PracticeData) {
    if (hoveredData.value == obj) {
        hoveredData.value = null
    } else {
        hoveredData.value = obj
    }
}

function eventListener(event: KeyboardEvent) {
    if (event.key == 'Tab') {
        event.preventDefault()
        event.stopPropagation()
        onTab()
    }
}

function onTab() {
    refMainPractice.value?.resetTest()
    refMainPractice.value?.launchTest(data.value, region)
}

async function getData(region: string) {
    const response = await api.get(`practice/data/${region}`)
    data.value = response.data
}

async function updateData(region: string) {
    const response = await api.post(`practice/update/${region}`, {params: [
        { country: 'Angola', typing: 400, reaction: 800 },
        { country: 'Burkina Faso', typing: 300, reaction: 1100 },
        { country: 'Angola', typing: 450, reaction: 600 },
    ]})
}

function onEndTest(d: PracticeData[]) {
    data.value = d
}

function onFilterUpdate(r: string) {
    region = r.toLowerCase()
    getData(r.toLowerCase())
}

</script>