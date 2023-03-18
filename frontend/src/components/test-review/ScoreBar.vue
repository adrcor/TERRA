<template>
    <a :class="newHighscore ? 'text-opacity-60' : 'text-opacity-0'" class="text-on-background select-none">
        New Highscore !
    </a>
    
    <div class="flex flex-row justify-between w-full text-on-background text-center">

        <div class="flex flex-col">
            <div class="opacity-60">Score</div>
            <div class="text-primary text-2xl">{{ props.score.result.score }}/{{ props.score.param.length }}</div>
            <div class="text-md opacity-60" :class="{ 'text-error': diffScore < 0, 'text-secondary': diffScore > 0 }">
                {{ diffScore >= 0 ? '+' : '' }}{{ diffScore }}
            </div>
        </div>

        <div class="flex flex-col">
            <div class="opacity-60">Time</div>
            <div class="text-primary text-2xl">{{ (Math.floor(props.score.result.time) / 1000).toFixed(3) }}</div>
            <div class="text-md opacity-60" :class="{ 'text-error': diffTime > 0, 'text-secondary': diffTime < 0 }">
                {{ diffTime >= 0 ? '+' : '' }}{{ (Math.floor(diffTime) / 1000).toFixed(3) }}
            </div>
        </div>

        <div class="flex flex-col">
            <div class="opacity-60">Speed</div>
            <div class="text-primary text-2xl">
                {{ (Math.floor(props.score.result.speed) / 1000).toFixed(3) }}
            </div>
            <div class="text-md opacity-60" :class="{ 'text-error': diffSpeed < 0, 'text-secondary': diffSpeed > 0 }">
                {{ diffSpeed >= 0 ? '+' : '' }}{{ (Math.floor(diffSpeed) / 1000).toFixed(3) }}
            </div>
        </div>

    </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import type { TestData, TestResult } from '@/models';

const props = defineProps<{
    score: TestData,
    highscore: TestResult,
    state: 'loading' | 'normal' | 'new'
}>()

const diffScore = computed(() => props.state == 'normal' ? props.score.result.score - props.highscore.score : 0)
const diffTime = computed(() => props.state == 'normal' ? props.score.result.time - props.highscore.time : 0)
const diffSpeed = computed(() => props.state == 'normal' ? props.score.result.speed - props.highscore.speed : 0)

const newHighscore = computed(() => {
    if (props.state == 'loading') {
        return false
    }
    if (props.state == 'normal' && props.score.result.speed - props.highscore.speed <= 0) {
        return false
    }
    return true
})

</script>