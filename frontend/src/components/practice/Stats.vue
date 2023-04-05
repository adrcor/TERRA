<template>
    <div v-if="hoveredData != null" class="flex flex-row text-on-background border-2 border-on-background opacity-60 rounded-md p-2 gap-4">
        <a>Country = {{ hoveredData.country }}</a>
        <a>Score = {{ hoveredData.grades.score }}</a>
        <a>Reaction = {{ hoveredData.grades.reaction }}</a>
        <a>Typing = {{ hoveredData.grades.typing }}</a>
    </div>

    <div v-else="" class="flex flex-row text-on-background border-2 border-on-background opacity-60 rounded-md p-2 gap-4">
        <a>Unlocked = {{ unlocked }}/{{ total }}</a>
        <a>Valid = {{ valid }}/{{ total }}</a>
        <a>Mean = {{ Math.floor(mean) }}</a>
    </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import type { PracticeData } from '@/models'

const props = defineProps<{
    data: PracticeData[] | null,
    hoveredData: PracticeData | null
}>()

const unlocked = computed(() => {
    if (props.data == null) {
        return 0
    }
    return props.data.filter(obj => obj.unlocked).length
})

const total = computed(() => {
    if (props.data == null) {
        return 0
    }
    return props.data.length
})

const valid = computed(() => {
    if (props.data == null) {
        return 0
    }''
   return props.data.filter(obj => obj.grades.score >= 80).length 
})


const mean = computed(() => {
    if (props.data == null) {
        return 0
    }
    const scores = props.data.filter(obj => obj.unlocked).map(obj => obj.grades.score)
    return scores.reduce((prev, curr) => (prev + curr)) / scores.length
})


</script>