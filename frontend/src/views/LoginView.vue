<template>
    <div class="flex flex-col gap-8 p-12 rounded-xl bg-overlay bg-opacity-5 w-2/3 max-w-md">
        <h1 class="text-on-background text-3xl self-center">
            Welcome Back
        </h1>
        <form @submit.prevent="onLogin" class="flex flex-col gap-3 items-center w-full">

            <div class="flex flex-row w-full items-center gap-1 rounded-md px-2 py-1 bg-overlay bg-opacity-5 text-on-background">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                    stroke="currentColor" class="w-6 h-6">
                    <path stroke-linecap="round"
                        d="M16.5 12a4.5 4.5 0 11-9 0 4.5 4.5 0 019 0zm0 0c0 1.657 1.007 3 2.25 3S21 13.657 21 12a9 9 0 10-2.636 6.364M16.5 12V8.25" />
                </svg>
                <input v-model="formLogin.email" type="text" placeholder="Email"
                    class="bg-transparent w-full focus:outline-none" />
            </div>

            <div class="flex flex-row items-center w-full gap-1 rounded-md px-2 py-1 bg-overlay bg-opacity-5 text-on-background">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                    stroke="currentColor" class="w-6 h-6">
                    <path stroke-linecap="round" stroke-linejoin="round"
                        d="M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z" />
                </svg>
                <input v-model="formLogin.password" :type="showPassword ? 'text' : 'password'" placeholder="Password"
                    class="bg-transparent w-full focus:outline-none" />
                <button type="button" @click="showPassword = !showPassword" class="opacity-60 hover:opacity-100">
                    <svg v-if="!showPassword" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                        stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round"
                            d="M2.036 12.322a1.012 1.012 0 010-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178z" />
                        <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                    </svg>
                    <svg v-if="showPassword" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                        stroke-width="1.5" stroke="currentColor" class="w-6 h-6">
                        <path stroke-linecap="round" stroke-linejoin="round"
                            d="M3.98 8.223A10.477 10.477 0 001.934 12C3.226 16.338 7.244 19.5 12 19.5c.993 0 1.953-.138 2.863-.395M6.228 6.228A10.45 10.45 0 0112 4.5c4.756 0 8.773 3.162 10.065 7.498a10.523 10.523 0 01-4.293 5.774M6.228 6.228L3 3m3.228 3.228l3.65 3.65m7.894 7.894L21 21m-3.228-3.228l-3.65-3.65m0 0a3 3 0 10-4.243-4.243m4.242 4.242L9.88 9.88" />
                    </svg>

                </button>
            </div>
            <a class="text-red-400">{{ errorText }}</a>
            <button type="submit"
                class="py-1 w-full rounded-md bg-primary hover:opacity-90 active:opacity-50 text-on-primary">Login</button>
        </form>
        <router-link to="register" class="text-primary self-end opacity-60 hover:opacity-100 active:opacity-60">Register
            now</router-link>
    </div>
</template>


<script setup lang="ts">
import { ref, watch, reactive } from 'vue'
import { supabase } from '@/supabase'
import { useRouter } from 'vue-router'

const formLogin = reactive<{
    email: string,
    password: string
}>({email: '', password: ''})

const router = useRouter()
const showPassword = ref(false)
const errorText = ref('')

watch(() => formLogin.email, () => {
    errorText.value = ''
})

watch(() => formLogin.password, () => {
    errorText.value = ''
})

async function onLogin() {
    const { data, error } = await supabase.auth.signInWithPassword(formLogin)

    if (error) {
        console.log(error)
        errorText.value = 'Invalid login credentials'
    } else {
        router.push({ name: 'account' })
    }
}
</script>