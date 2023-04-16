<template>
    <div class="flex flex-col items-center gap-6 p-12 rounded-xl bg-overlay bg-opacity-5 w-2/3 max-w-md mb-auto">
        <h1 class="text-on-background text-3xl self-center">
            Update password
        </h1>
        <form @submit.prevent="onUpdate" spellcheck="false" class="flex flex-col gap-3 items-center w-full">

            <div
                class="flex flex-row items-center w-full gap-1 rounded-md px-2 py-1 bg-overlay bg-opacity-5 text-on-background">
                <img src="@/assets/icons/line/lock.svg" class="w-6 h-6 flex-shrink-0" />
                <input v-model="formUpdate.password" :type="showPassword ? 'text' : 'password'" placeholder="New Password"
                    class="bg-transparent w-full focus:outline-none" />
                <button type="button" tabindex="-1" @click="showPassword = !showPassword"
                    class="opacity-60 hover:opacity-100">
                    <img v-if="!showPassword" src="@/assets/icons/line/show.svg" class="w-6 h-6">
                    <img v-if="showPassword" src="@/assets/icons/line/show-crossed.svg" class="w-6 h-6">
                </button>
            </div>

            <div
                class="flex flex-row items-center w-full gap-1 rounded-md px-2 py-1 bg-overlay bg-opacity-5 text-on-background">
                <img src="@/assets/icons/line/lock.svg" class="w-6 h-6 flex-shrink-0" />
                <input v-model="formUpdate.confirm" :type="showConfirm ? 'text' : 'password'" placeholder="Confirm New Password"
                    class="bg-transparent w-full focus:outline-none" />
                <button type="button" tabindex="-1" @click="showConfirm = !showConfirm"
                    class="opacity-60 hover:opacity-100">
                    <img v-if="!showConfirm" src="@/assets/icons/line/show.svg" class="w-6 h-6">
                    <img v-if="showConfirm" src="@/assets/icons/line/show-crossed.svg" class="w-6 h-6">
                </button>
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

const formUpdate = ref({
    password: '',
    confirm: ''
})

watch(formUpdate, () => {
    if (errorText.value) {
        errorText.value = ''
    }
}, { deep: true })

const router = useRouter()
const showPassword = ref(false)
const showConfirm = ref(false)
const errorText = ref('')
const disabled = ref(false)


async function onUpdate() {
    disabled.value = true
    if (formUpdate.value.password !== formUpdate.value.confirm) {
        errorText.value = "Passwords don't match"
        disabled.value = false
        return
    }

    const { data, error } = await supabase.auth.updateUser({ password: formUpdate.value.password })
    if (error) {
        errorText.value = error.message
        disabled.value = false
        return
    }

    disabled.value = false
    router.push({ name: 'account' })
}

</script>