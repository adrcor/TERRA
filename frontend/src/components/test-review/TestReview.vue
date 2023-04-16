<template>
    <div class="flex flex-col items-center w-96 gap-4">
        <p v-if="!store.state.auth.logedIn" class="text-on-background opacity-80">Sign in to track your progress!</p>
        <ScoreBar :score="props.data" :highscore="props.highscore" :state="props.stateHigscore"/>
        <TestChart :histo="props.histo"/>
    </div>
</template>

<script setup lang="ts">
import type { TestData, TestResult } from '@/models'
import type { InputData } from '@/models'
import ScoreBar from './ScoreBar.vue'
import TestChart from './TestChart.vue'
import { useStore } from '@/store'

const store = useStore()

const props = defineProps<{
    data: TestData,
    histo: InputData[],
    highscore: TestResult,
    stateHigscore: 'loading' | 'normal' | 'new'
}>()

</script>