<template>
    <div class="flex flex-row text-on-background opacity-60 rounded-md p-2 gap-4">
        <a>{{ mean.toFixed(1) }}%</a>
        <a>{{ (typing / 5).toFixed(0) }}wpm</a>
        <a>{{ reaction.toFixed(0) }}ms</a>
    </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import type { PracticeData } from '@/models'

const props = defineProps<{
    data: PracticeData[] | null,
}>()

const unlocked = computed(() => {
    if (props.data == null) {
        return 0
    }
    return props.data.filter(obj => obj.unlocked).length
})

const typing = computed(() => {
    if (props.data == null) {
        return 0
    }
    const scores = props.data.filter(obj => obj.grades.count > 0).map(obj => obj.grades.typing)
    if (scores.length == 0) {
        return 0
    }
    return scores.reduce((prev, curr) => (prev + curr)) / scores.length
})

const reaction = computed(() => {
    if (props.data == null) {
        return 0
    }
    const scores = props.data.filter(obj => obj.grades.count > 0).map(obj => obj.grades.reaction)
    if (scores.length == 0) {
        return 0
    }
    return scores.reduce((prev, curr) => (prev + curr)) / scores.length
})

const mean = computed(() => {
    if (props.data == null) {
        return 0
    }
    const scores = props.data.map(obj => obj.grades.score)
    if (scores.length == 0) {
        return 0
    }
    return scores.reduce((prev, curr) => (prev + curr)) / scores.length
})


</script>