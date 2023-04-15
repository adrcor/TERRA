<template>
    <router-link to="account" class="flex flex-row items-center text-on-background opacity-60 hover:opacity-100">
        <img v-if="!store.state.auth.logedIn" src="@/assets/icons/login.svg" class="w-6 h-6" />
        <img v-if="store.state.auth.logedIn" src="@/assets/icons/account.svg" class="w-6 h-6" />
        <a>{{ store.state.auth.logedIn ? 'Account' : 'Login' }}</a>
    </router-link>
</template>

<script setup lang="ts">
import { useStore } from '@/store'

const store = useStore()

</script>
