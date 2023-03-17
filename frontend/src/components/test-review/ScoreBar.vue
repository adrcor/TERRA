<template>
    <a v-if="newHighscore" class="text-on-background">NEW HIGHSCORE</a>
    <div class="flex flex-row justify-between w-full text-on-background text-center">
        <div class="flex flex-col">
            <div class="opacity-60">Score</div>
            <div class="text-primary text-2xl">{{ props.score.score }}/{{ props.score.length }}</div>
            <div class="text-md opacity-60" :class="{ 'text-error': diffScore < 0, 'text-secondary': diffScore > 0 }">
                {{ diffScore >= 0 ? '+' : '' }}{{ diffScore }}
            </div>

        </div>
        <div class="flex flex-col">
            <div class="opacity-60">Time</div>
            <div class="text-primary text-2xl">{{ (Math.floor(props.score.time) / 1000).toFixed(3) }}</div>
            <div class="text-md opacity-60" :class="{ 'text-error': diffTime > 0, 'text-secondary': diffTime < 0 }">
                {{ diffTime >= 0 ? '+' : '' }}{{ (Math.floor(diffTime) / 1000).toFixed(3) }}
            </div>
        </div>
        <div class="flex flex-col">
            <div class="opacity-60">Speed</div>
            <div class="text-primary text-2xl">
                {{ (Math.floor(props.score.speed) / 1000).toFixed(3) }}
            </div>
            <div class="text-md opacity-60" :class="{ 'text-error': diffSpeed < 0, 'text-secondary': diffSpeed > 0 }">
                {{ diffSpeed >= 0 ? '+' : '' }}{{ (Math.floor(diffSpeed) / 1000).toFixed(3) }}
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, watch, computed } from 'vue'
import type { Highscore, TestData } from '../main-test/type';


const props = defineProps<{
    score: TestData,
    highscore: Highscore,
    newHighscore: boolean
}>()

const diffScore = computed(() => props.score.score - props.highscore.score )
const diffTime = computed(() => props.score.time - props.highscore.time)
const diffSpeed = computed(() => props.score.speed - props.highscore.speed)

const newHighscore = computed(() => props.score.speed > props.highscore.speed)

</script>