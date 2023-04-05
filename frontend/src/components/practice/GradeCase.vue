<template>
    <button class="py-1 w-6 text-sm text-center"
        :class="{
            'bg-gray-500 bg-opacity-40': !data.unlocked,
            'bg-gr-20': data.unlocked && data.grades.score < 20,
            'bg-gr-40': data.unlocked && data.grades.score >= 20 && data.grades.score < 40,
            'bg-gr-60': data.unlocked && data.grades.score >= 40 && data.grades.score < 60,
            'bg-gr-80': data.unlocked && data.grades.score >= 60 && data.grades.score < 80,
            'bg-gr-100': data.unlocked && data.grades.score >= 80 && data.grades.score <= 100
        }">
        {{data.code}}
    </button>
</template>

<script setup lang="ts">
import type { PracticeData } from '@/models'

const props = defineProps<{
    data: PracticeData
}>()

</script>