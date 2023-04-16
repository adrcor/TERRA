<template>
    <div class="flex flex-row flex-wrap items-center justify-center gap-1">
        <GradeCase v-if="data" v-for="obj in data" :data="obj"/>
        <div class="py-1 w-6 text-sm text-center select-none bg-gray-500 bg-opacity-40" v-else="" v-for="obj in nCase">--</div>
    </div>
</template>

<script setup lang="ts">
import type { PracticeData, Region } from '@/models'
import GradeCase from './GradeCase.vue'
import { computed } from 'vue'
import { useStore } from '@/store'

const props = defineProps<{
    data: PracticeData[] | null
}>()

const store = useStore()

type RegionDic = {
    [key in Region]: number
}

const regionLength: RegionDic = {World: -1, AF: 54, AS: 48, EU: 45, NA: 23, OC: 14, SA: 12}

const nCase = computed(() => {
    return Array(regionLength[store.state.practice.region]).fill(0)
})

const test = Array(50).fill(0)

</script>

