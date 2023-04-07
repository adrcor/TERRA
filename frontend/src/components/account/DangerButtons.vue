<template>
    <div class="flex flex-row bg-overlay bg-opacity-5 p-2 rounded-lg gap-2">
        <button class="flex-1 rounded-md p-2 bg-error bg-opacity-5 text-error text-opacity-60 transition-all
                       hover:bg-opacity-60 hover:text-on-error hover:text-opacity-100
                       active:bg-opacity-40 active: text-opacit-60">
            Reset Test Data
        </button>
        <button class="flex-1 rounded-md p-2 bg-error bg-opacity-5 text-error text-opacity-60 transition-all
                        hover:bg-opacity-60 hover:text-on-error hover:text-opacity-100
                        active:bg-opacity-40 active: text-opacit-60">
            Reset Practice Data
        </button>
        <button @click="logout" class="flex-1 rounded-md p-2 bg-error bg-opacity-5 text-error text-opacity-60 transition-all
                        hover:bg-opacity-60 hover:text-on-error hover:text-opacity-100
                        active:bg-opacity-40 active: text-opacit-60">
            Logout
        </button>
    </div>
</template>

<script setup lang="ts">
import { supabase } from '@/supabase'
import { useRouter } from 'vue-router'

const router = useRouter()

async function logout() {
    const response = await supabase.auth.signOut()
    router.push({ name: 'login' })
}

</script>