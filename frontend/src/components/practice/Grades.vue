<template>
    <div class="flex flex-row flex-wrap items-center justify-center gap-1">
        <GradeCase v-for="obj in data" :data="obj" @click="onClick(obj)"/>
    </div>
    <div v-if="hovered" class="text-on-background">{{hovered.country}} {{ hovered.grades.score }}</div>
    <div v-if="!hovered" class="text-on-background">mean = 32</div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import type { PracticeData } from '@/models/practice-data';
import GradeCase from './GradeCase.vue';

const hovered = ref<PracticeData | null>(null)

const props = defineProps<{
    data: PracticeData[] | null
}>()

function onClick(obj: PracticeData) {
    if (hovered.value == obj) {
        hovered.value = null
    } else {
        hovered.value = obj
    }
}

</script>

