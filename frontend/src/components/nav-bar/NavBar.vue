<template>
    <div class="flex flex-row items-center justify-between h-16 w-full px-6 py-12">
         <HomeButton />

        <router-link to="/practice" class="flex flex-row gap-2 text-on-background opacity-60 hover:opacity-100">
            <img src="@/assets/icons/solid/practice.svg" class="w-6 h-6"/>
            <a>Practice</a>
        </router-link>

        <router-link to="/about" class="flex flex-row gap-2 text-on-background opacity-60 hover:opacity-100">
            <img src="@/assets/icons/solid/info.svg" class="w-6 h-6"/>
            <a>About</a>
        </router-link>

        <AccountButton />
    </div>
</template>

<script setup lang="ts">
import { useStore } from '@/store'
import { useRouter } from 'vue-router'
import HomeButton from './HomeButton.vue'
import AccountButton from './AccountButton.vue'

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