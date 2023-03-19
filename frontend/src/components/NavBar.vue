<template>
    <div class="flex flex-row items-center justify-between h-16 w-full max-w-3xl px-6 py-12">
        <button @click.native="onClick" class="text-primary text-3xl">Terra</button>
        <router-link to="account" class="text-on-background text-2xl">{{ store.state.auth.username ? store.state.auth.username : 'Login' }}</router-link>
    </div>
</template>

<script setup lang="ts">
import { useStore } from '@/store'
import { useRouter } from 'vue-router';

const store = useStore()

const router = useRouter()

function onClick() {
    const currentRoute = router.currentRoute.value.fullPath
    if (currentRoute == '/') {
        router.go(0)
    } else {
        router.push('/')
    }
}

</script>