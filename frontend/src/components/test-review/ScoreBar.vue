<template>
    <div class="flex flex-row justify-between w-full text-on-background text-center">
        <div class="flex flex-col">
            <div class="opacity-60">Score</div>
            <div class="text-primary text-2xl">{{ props.data.score }}/{{ props.data.length }}</div>

        </div>
        <div class="flex flex-col">
            <div class="opacity-60">Time</div>
            <div class="text-primary text-2xl">{{ (Math.floor(props.data.time) / 1000).toFixed(3) }}</div>

        </div>
        <div class="flex flex-col">
            <div class="opacity-60">Speed</div>
            <div class="text-primary text-2xl">
                {{ (Math.floor(props.data.speed) / 1000).toFixed(3) }}
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import type { TestData } from '../main-test/type';

const props = defineProps<{
    data: TestData
}>()


</script>