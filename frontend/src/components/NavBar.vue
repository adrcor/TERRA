<template>
    <div class="flex flex-row items-center justify-between h-16 w-full max-w-3xl px-6 py-12">
        <router-link to="/" @click.native="router.go(0)" class="text-primary text-3xl">Terra</router-link>
        <router-link to="account" class="text-on-background text-2xl">{{ store.state.auth.username ? store.state.auth.username : 'Login' }}</router-link>
    </div>
</template>

<script setup lang="ts">
import { useStore } from '@/store'
import { useRouter } from 'vue-router';

const store = useStore()

const router = useRouter()

</script>