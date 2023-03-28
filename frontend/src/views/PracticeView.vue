<template>
    <div class="flex flex-col flex-1 p-2 mb-16 justify-center items-center gap-4">
        <Grades :data="data"/>
        <div class="flex flex-row">
            <PracticeFilter @filter-update="onFilterUpdate"/>
            
        </div>
    </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { api } from '@/api';
import PracticeFilter from '@/components/practice/PracticeFilter.vue';
import Grades from '@/components/practice/Grades.vue';
import type { PracticeData } from '@/models/practice-data';

onMounted(() => getData('af'))

const data = ref<PracticeData[] | null>(null)

async function onClick() {
    const response = await api.get('practice/data/af')
    console.log(response)
}

async function getData(region: string) {
    const response = await api.get(`practice/data/${region}`)
    console.log(response)
    data.value = response.data
}

async function updateData(region: string) {
    const response = await api.post(`practice/update/${region}`, {params: [
        { country: 'Angola', typing: 400, reaction: 800 },
        { country: 'Burkina Faso', typing: 300, reaction: 1100 },
        { country: 'Angola', typing: 450, reaction: 600 },
    ]})
    console.log(response)
}

function onFilterUpdate(region: string) {
    console.log(region)
    getData(region.toLowerCase())
}

</script>