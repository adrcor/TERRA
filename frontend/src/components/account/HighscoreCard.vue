<template>
    <button v-if="test" @click="onClick" class="flex flex-1 flex-col rounded-lg items-center py-4 bg-overlay bg-opacity-0 hover:bg-opacity-5 hover:text-opacity-100 transition-all" :class="selected ? 'text-primary bg-opacity-5 text-opacity-100' : 'text-on-background text-opacity-60'">
        <a class="opacity-40">{{ length }}</a>
        <a class="text-3xl">{{ test ? Math.floor(test.speed / 1000) : '-'}}</a>
        <a class="text-xl opacity-60">{{ test ? Math.floor((test.score / test.length) * 100) + '%' : '-' }}</a>
    </button>
    <div v-else class="flex flex-1 flex-col rounded-lg items-center py-4 select-none">
        <a class="opacity-40">{{ length }}</a>
        <a class="text-3xl">-</a>
        <a class="text-xl opacity-60">-</a>
    </div>
</template>

<script setup lang="ts">
import type { TestDb } from '@/models';

const props = defineProps<{
    length: number,
    test: null | TestDb,
    selected: boolean
}>()

const emits = defineEmits([
    'on-click'
])

function onClick() {
    emits('on-click', props.test?.region, props.length)
}

</script>