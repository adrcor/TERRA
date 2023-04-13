<template>
    <router-link to="account" class="flex flex-row items-center text-on-background text-2xl opacity-60 hover:opacity-100">
        <img v-if="!store.state.auth.logedIn" src="@/assets/icons/login.svg" class="w-8 h-8" />
        <img v-if="store.state.auth.logedIn" src="@/assets/icons/account.svg" class="w-8 h-8" />
        <a>{{ store.state.auth.logedIn ? 'Account' : 'Login' }}</a>
    </router-link>
</template>

<script setup lang="ts">
import { useStore } from '@/store'

const store = useStore()

</script>
