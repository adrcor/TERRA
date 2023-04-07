<template>
    <Highscore @on-select="onSelect" />
    <HistoChart ref="refHistoChart" :data="chartData"/>
    <button @click="logout" class="px-3 py-1 rounded-xl bg-overlay bg-opacity-5 text-on-background">LOGOUT</button>
</template>

<script setup lang="ts">
import Highscore from '@/components/account/Highscore.vue'
import HistoChart from '@/components/account/HistoChart.vue'
import type { TestDb, Region, Length } from '@/models'
import { supabase } from '@/supabase'
import { useRouter } from 'vue-router'
import { useStore } from '@/store'
import { ref, onMounted } from 'vue'
import { api } from '@/api';

const router = useRouter()
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

async function logout() {
    const response = await supabase.auth.signOut()
    router.push({ name: 'login'})
}

function onSelect(r: Region, l: Length) {
    region = r
    length = l
    setData()
}

</script>