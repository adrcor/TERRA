<template>
    <div class="flex flex-row flex-wrap bg-overlay bg-opacity-5 p-2 rounded-lg gap-2">
        <button @click="showModalTest = true" class="flex-1 rounded-md p-2 bg-error bg-opacity-5 text-error text-opacity-60 transition-all
                       hover:bg-opacity-60 hover:text-on-error hover:text-opacity-100
                       active:bg-opacity-40 active: text-opacit-60">
            Reset Tests
        </button>
        <button @click="showModalPractice = true" class="flex-1 rounded-md p-2 bg-error bg-opacity-5 text-error text-opacity-60 transition-all
                        hover:bg-opacity-60 hover:text-on-error hover:text-opacity-100
                        active:bg-opacity-40 active: text-opacit-60">
            Reset Practice
        </button>
        <button @click="updatePassword" class="flex-1 rounded-md p-2 bg-error bg-opacity-5 text-error text-opacity-60 transition-all
                        hover:bg-opacity-60 hover:text-on-error hover:text-opacity-100
                        active:bg-opacity-40 active: text-opacit-60">
            Update Password
        </button>
        <button @click="logout" class="flex-1 rounded-md p-2 bg-error bg-opacity-5 text-error text-opacity-60 transition-all
                        hover:bg-opacity-60 hover:text-on-error hover:text-opacity-100
                        active:bg-opacity-40 active: text-opacit-60">
            Logout
        </button>
    </div>
    <ModalDanger v-if="showModalTest" @on-yes="resetTest" @on-close="closeModals" dataType="test"/>
    <ModalDanger v-if="showModalPractice" @on-yes="resetPractice" @on-close="closeModals" dataType="practice"/>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { api } from '@/api'
import { supabase } from '@/supabase'
import { useRouter } from 'vue-router'
import ModalDanger from '@/components/account/ModalDanger.vue'

const router = useRouter()
const showModalTest = ref(false)
const showModalPractice = ref(false)

async function logout() {
    const response = await supabase.auth.signOut()
    router.push({ name: 'login' })
}

function updatePassword() {
    router.push({ name: 'password'})
}

async function resetTest() {
    const response = await api.delete('/test/delete')
    router.go(0)
}

async function resetPractice() {
    const response = await api.delete('/practice/delete')
    router.go(0)
}

function closeModals() {
    showModalTest.value = false
    showModalPractice.value = false
}

</script>