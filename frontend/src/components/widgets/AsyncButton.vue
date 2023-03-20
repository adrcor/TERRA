<template>
    <button @click="onAsyncClick" :disabled="disabled" class="flex flex-col items-center py-1 w-full rounded-md bg-primary hover:opacity-90 active:opacity-50 text-on-primary disabled:opacity-50">
        <slot v-if="!disabled"></slot>
        <slot v-if="disabled" name="loading">Loading...</slot>
    </button>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const props = defineProps({
    onClick: {
        type: Function,
        required: true
    }
})

const disabled = ref(false)

async function onAsyncClick(): Promise<void> {
    disabled.value = true
    await props.onClick()
    disabled.value = false
}
</script>