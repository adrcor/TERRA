<template>
    <div class="flex flex-row items-center justify-between h-16 w-full max-w-3xl px-6 py-12">
        <router-link to="/" class="text-primary text-3xl">Terra</router-link>
        <router-link to="account" class="text-on-background text-2xl">{{ store.state.auth.username ? store.state.auth.username : 'Login' }}</router-link>
    </div>
</template>

<script setup lang="ts">
import { useStore } from '@/store'

const store = useStore()

</script>