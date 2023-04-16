<template>
    <div class="flex flex-row text-on-background justify-between text-opacity-60 text-xl w-full">
        <span>{{ metrics.answer }}/{{ metrics.length }}</span>
        <span>{{ Math.floor(metrics.time / 1000) }}s</span>
        <span>{{ Math.round(metrics.accuracy * 100) }}%</span>
        <span>{{ metrics.speed ? Math.floor(metrics.speed / 1000) : 0 }}/min</span>
    </div>
</template>

<script setup lang="ts">
import type { TestMetrics } from '@/models';

defineProps<{
    metrics: TestMetrics
}>()

</script>