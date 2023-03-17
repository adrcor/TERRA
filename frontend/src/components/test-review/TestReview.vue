<template>
    <div class="flex flex-col items-center w-96 gap-4">
        <ScoreBar :score="props.data" :highscore="props.highscore" :newHighscore="true"/>
        <TestChart :histo="props.histo"/>
    </div>
</template>

<script setup lang="ts">
import type { TestData, InputData, Highscore } from '../main-test/type';
import ScoreBar from './ScoreBar.vue';
import TestChart from './TestChart.vue';

const props = defineProps<{
    data: TestData,
    histo: InputData[],
    highscore: Highscore
}>()

</script>