<template>
    <div class="flex flex-col flex-1 p-2 mb-16 justify-center items-center gap-4">
        <Grades :data="data" @hovered-data="onHoveredData"/>
        <div class="flex flex-row items-center gap-2">
            <PracticeFilter @filter-update="onFilterUpdate"/>
            <Stats :data="data" :hoveredData="hoveredData"/>
        </div>
    </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { api } from '@/api';
import PracticeFilter from '@/components/practice/PracticeFilter.vue';
import Grades from '@/components/practice/Grades.vue';
import type { PracticeData } from '@/models/practice-data';
import Stats from '@/components/practice/Stats.vue';

onMounted(() => getData('af'))

const data = ref<PracticeData[] | null>(null)
const hoveredData = ref<PracticeData | null>(null)

function onHoveredData(obj: PracticeData) {
    if (hoveredData.value == obj) {
        hoveredData.value = null
    } else {
        hoveredData.value = obj
    }
}

async function onClick() {
    const response = await api.get('practice/data/af')
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

function onFilterUpdate(region: string) {
    getData(region.toLowerCase())
}

</script>