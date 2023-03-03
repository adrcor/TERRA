<template>
    <button @click="getUser" class="px-3 py-1 rounded-xl bg-overlay bg-opacity-5 text-on-background">GET SESSION</button>    
    <h1 class="text-on-background text-xl">user = {{ user }}</h1>
    <button @click="logout" class="px-3 py-1 rounded-xl bg-overlay bg-opacity-5 text-on-background">LOGOUT</button>    
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { supabase } from '@/supabase'
import { useRouter } from 'vue-router'

const user = ref<String>('')
const router = useRouter()

async function getUser() {
    const response = await supabase.auth.getSession()
    console.log(response)
    if (response.data.session?.user.id) {
        user.value = response.data.session?.user.id
    }
}

async function logout() {
    const response = await supabase.auth.signOut()
    router.push({ name: 'login'})
}

</script>