<template>
    <div class="flex flex-col items-center gap-6 p-12 rounded-xl bg-overlay bg-opacity-5 w-2/3 max-w-md mb-auto">
        <h1 class="text-on-background text-3xl self-center">
            Update password
        </h1>
        <form @submit.prevent="onForgot" spellcheck="false" class="flex flex-col gap-3 items-center w-full">

            <div
                class="flex flex-row w-full items-center gap-1 rounded-md px-2 py-1 bg-overlay bg-opacity-5 text-on-background">
                <img src="@/assets/icons/line/arobase.svg" class="w-6 h-6">
                <input v-model="email" type="text" placeholder="Email"
                    class="bg-transparent w-full focus:outline-none" />
            </div>

            <button type="submit" :disabled="disabled"
                class="py-1 w-full rounded-md bg-primary hover:opacity-90 active:opacity-50 disabled:opacity-50 text-on-primary">
                Update
            </button>
        </form>

        <a class="text-error">{{ errorText }}</a>

    </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'
import { supabase } from '@/supabase'
import { useRouter } from 'vue-router'

const router = useRouter()

const email = ref('')
const disabled = ref(false)
const errorText = ref('')
 
async function onForgot() {
    console.log(email.value)
    const { data, error } = await supabase.auth.resetPasswordForEmail(email.value, {
        redirectTo: window.location.origin,
    })
    console.log(data)
    console.log(error)
}

</script>