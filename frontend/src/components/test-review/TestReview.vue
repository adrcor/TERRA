<template>
    <div class="flex flex-col items-center w-96 gap-4">
        <ScoreBar :data="props.data"/>
    </div>
</template>

<script setup lang="ts">
import type { TestData } from '../main-test/type';
import ScoreBar from './ScoreBar.vue';

const props = defineProps<{
    data: TestData
}>()

</script>