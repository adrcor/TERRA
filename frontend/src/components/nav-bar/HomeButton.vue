<template>
    <button @click="onClick" class="text-primary text-3xl flex flex-row items-center opacity-80 hover:opacity-100 active:opacity-80">
        <img src="@/assets/icons/color/terra.svg" class="w-12 h-12"/>
        <a>TerraTrivia</a>
    </button>
</template>


<script setup lang="ts">
import { useRouter } from 'vue-router';

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