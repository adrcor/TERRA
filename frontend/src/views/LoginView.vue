<template>
    <div class="flex flex-col items-center gap-6 p-12 rounded-xl bg-overlay bg-opacity-5 w-2/3 max-w-md mb-auto">
        <h1 class="text-on-background text-3xl self-center">
            Welcome Back
        </h1>
        <form @submit.prevent="onLogin" spellcheck="false" class="flex flex-col gap-3 items-center w-full">

            <div
                class="flex flex-row w-full items-center gap-1 rounded-md px-2 py-1 bg-overlay bg-opacity-5 text-on-background">
                <img src="@/assets/icons/line/arobase.svg" class="w-6 h-6">
                <input v-model="formLogin.email" type="text" placeholder="Email"
                    class="bg-transparent w-full focus:outline-none" />
            </div>

            <div
                class="flex flex-row items-center w-full gap-1 rounded-md px-2 py-1 bg-overlay bg-opacity-5 text-on-background">
                <img src="@/assets/icons/line/lock.svg" class="w-6 h-6 flex-shrink-0"/>
                <input v-model="formLogin.password" :type="showPassword ? 'text' : 'password'" placeholder="Password"
                    class="bg-transparent w-full focus:outline-none" />
                <button type="button" tabindex="-1" @click="showPassword = !showPassword"
                    class="opacity-60 hover:opacity-100">
                    <img v-if="!showPassword" src="@/assets/icons/line/show.svg" class="w-6 h-6">
                    <img v-if="showPassword" src="@/assets/icons/line/show-crossed.svg" class="w-6 h-6">
                    

                </button>
            </div>

            <button type="submit" :disabled="disabled"
                    class="py-1 w-full rounded-md bg-primary hover:opacity-90 active:opacity-50 disabled:opacity-50 text-on-primary">Sign In</button>
        </form>
        
        <button class="flex flex-row items-center justify-center gap-3 w-full py-1 rounded-md text-on-overlay bg-overlay bg-opacity-90 hover:bg-opacity-70 active:bg-opacity-50" @click="onGoogleAuth">
            <img class="w-4 h-4" src="@/assets/icons/color/google.svg"/>
            <a>Sign In with Google</a>
        </button>

        <a class="text-error">{{ errorText }}</a>

        <router-link to="register" class="text-primary self-end opacity-60 hover:opacity-100 active:opacity-60">Register now</router-link>
    </div>
</template>


<script setup lang="ts">
import { ref, watch } from 'vue'
import { supabase } from '@/supabase'
import { useRouter } from 'vue-router'

const formLogin = ref({
    email: '',
    password: ''
})

watch(formLogin, () => {
    if (errorText.value) {
        errorText.value = ''
    }
}, {deep: true})

const router = useRouter()
const showPassword = ref(false)
const errorText = ref('')
const disabled = ref(false)

async function onLogin() {
    disabled.value = true
    const { data, error } = await supabase.auth.signInWithPassword(formLogin.value)
    if (error) {
        errorText.value = error.message
        disabled.value = false
        return
    }
    disabled.value = false
    router.push({ name: 'home' })
}

async function onGoogleAuth () {
    const { data, error } = await supabase.auth.signInWithOAuth({
        provider: 'google',
        options: {
            redirectTo: window.location.origin
        }
    })
}

</script>