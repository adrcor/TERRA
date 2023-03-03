<template>
    <div class="flex flex-col w-full items-center gap-1">
        <div class="flex flex-row w-full items-center gap-1 rounded-md px-2 py-1 bg-overlay bg-opacity-5 text-on-background">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 flex-shrink-0">
                <path stroke-linecap="round" stroke-linejoin="round"
                    d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z" />
            </svg>
            <input v-model="username" @keyup="textSearch" type="text" placeholder="Username" class="bg-transparent w-full focus:outline-none"/>
            <State :state="state"/>
        </div>
        <a v-if="!validChars" class="text-error">- Can only contains letters, digits, - and _</a>
        <a v-if="!validLength" class="text-error">- Must be between 4 and 16 characters</a>
        <a v-if="backendError" class="text-error">{{ backendError }}</a>
    </div>
    
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { api } from '@/api';
import State from './UsernameSetterState.vue'

var timer: NodeJS.Timeout | null = null
const state = ref<null | 'valid' | 'error' | 'loading'>(null)

const validChars = ref<Boolean>(true)
const validLength = ref<Boolean>(true)
const backendError = ref<String>('')

const props = defineProps(['modelValue'])
const emit = defineEmits(['update:modelValue'])

const username = computed({
    get() {
        return props.modelValue
    },
    set(value) {
        emit('update:modelValue', value)
    }
})

async function verifyInput() {
    state.value = 'loading'

    if (!localValidate()) {
        state.value = 'error'
        return
    }

    const response = await api.get('/user/verify/' + props.modelValue)
    if (state.value == 'loading') {
        if (response.data.valid) {
            state.value = 'valid'
        } else {
            state.value = 'error'
            backendError.value = response.data.message
        }
    }
}

function localValidate() {
    const chars = /^[a-zA-Z0-9_-]+$/
    validChars.value = chars.test(username.value)
    validLength.value = username.value.length >= 4 && username.value.length <= 16
    return validChars.value && validLength.value
}

function textSearch() {
    state.value = null
    backendError.value = ''
    validChars.value = true
    validLength.value = true
    if (timer) {
        clearTimeout(timer)
    }
    if (props.modelValue != '') {
        timer = setTimeout(verifyInput, 500)
    }
}

</script>