<template>
    <h1>Practice</h1>
    <button class="text-primary border border-on-background rounded-lg" @click="onClick">TEST</button>
    <button class="text-primary border border-on-background rounded-lg" @click="onPost">POST</button>
</template>

<script setup lang="ts">
import { api } from '@/api';

async function onClick() {
    const response = await api.get('practice/data/af')
    console.log(response)
}

async function onPost() {
    const response = await api.post('practice/update/af', {params: [
        { country: 'Angola', typing: 400, reaction: 800 },
        { country: 'Burkina Faso', typing: 300, reaction: 1100 },
        { country: 'Angola', typing: 450, reaction: 600 },
    ]})
    console.log(response)
}

</script>