<template>
    <div class="flex flex-row items-center justify-between h-16 w-full px-6 py-12">
        <div class="flex-1">
            <HomeButton />
        </div>
        <div class="flex-1 text-center">
            <MiddleButton to="practice">Practice</MiddleButton>
        </div>
        <div class="flex flex-1 justify-end">
            <AccountButton />
        </div>
    </div>
</template>

<script setup lang="ts">
import { useStore } from '@/store'
import { useRouter } from 'vue-router';
import HomeButton from './HomeButton.vue';
import AccountButton from './AccountButton.vue';
import MiddleButton from './MiddleButton.vue';

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