<template>
    <router-link :to="to" class="text-on-background text-opacity-60 hover:text-opacity-100">
        <slot></slot>
    </router-link>
</template>

<script setup lang="ts">

const props = defineProps<{
    to: string
}>()

</script>