<template>
    <div class="flex flex-col gap-1 w-2/3 h-full">
        <Highscore @on-select="onSelect" />
        <HistoChart ref="refHistoChart" :data="chartData"/>
        <DangerButtons />
    </div>
</template>

<script setup lang="ts">
import Highscore from '@/components/account/Highscore.vue'
import HistoChart from '@/components/account/HistoChart.vue'
import type { TestDb, Region, Length } from '@/models'
import { useStore } from '@/store'
import { ref, onMounted } from 'vue'
import { api } from '@/api';
import DangerButtons from '@/components/account/DangerButtons.vue'

const store = useStore()
const chartData = ref<TestDb[]>([])
const refHistoChart = ref()
var region: Region = store.state.filter.region
var length: Length = store.state.filter.length

onMounted(() => {
    onSelect(store.state.filter.region, store.state.filter.length)
})

async function setData() {
    const response = await api.get(`test/get/region=${region}&length=${length}`)
    chartData.value = response.data as TestDb[]
    refHistoChart.value.updateChart(response.data)
}

function onSelect(r: Region, l: Length) {
    region = r
    length = l
    setData()
}

</script>