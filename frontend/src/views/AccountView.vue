<template>
    <Highscore @on-select="onSelect" />
    <button @click="logout" class="px-3 py-1 rounded-xl bg-overlay bg-opacity-5 text-on-background">LOGOUT</button>    
</template>

<script setup lang="ts">
import Highscore from '@/components/account/Highscore.vue';
import type { Length } from '@/models/length';
import type { Region } from '@/models/region';
import { supabase } from '@/supabase'
import { useRouter } from 'vue-router'

const router = useRouter()

async function logout() {
    const response = await supabase.auth.signOut()
    router.push({ name: 'login'})
}

function onSelect(region: Region, lenght: Length) {
    console.log(region, length)
}

</script>