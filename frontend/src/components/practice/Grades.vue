<template>
    <div class="flex flex-row flex-wrap items-center justify-center gap-1">
        <GradeCase v-for="obj in data" :data="obj" @click="onClick(obj)"/>
    </div>
</template>

<script setup lang="ts">
import type { PracticeData } from '@/models/practice-data';
import GradeCase from './GradeCase.vue';

const emits = defineEmits([
    'hovered-data'
])

const props = defineProps<{
    data: PracticeData[] | null
}>()

function onClick(obj: PracticeData) {
    emits('hovered-data', obj)
}

</script>

