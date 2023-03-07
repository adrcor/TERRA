<template>
    <div class="flex flex-col items-center">
        <input ref="refInput" v-model="valueInput" @blur="focus" @input="event => onInput(event as InputEvent)" placeholder="Unfocused"
            class="text-center text-on-background text-2xl bg-transparent outline-none caret-primary focus:placeholder-transparent placeholder-on-background placeholder-opacity-60" />
        <h1 class="h-4" :class="displayHelp == true ? 'opacity-100' : 'opacity-0'">{{ expected }}</h1>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'

const refInput = ref<HTMLInputElement>()
const valueInput = ref<string>('')
const expected = ref<string>('')
const displayHelp = ref<boolean>(false)

var startTime: number | null = null

const props = defineProps({
    helpCharacter: {
        type: String,
        default: '.'
    }
})

const emits = defineEmits([
    'answer'
])

defineExpose({
    setExpected,
    resetInput
})

onMounted(() => {
    focus()
})

function focus() {
    // Keep the input focused on outside click
    if (refInput.value) {
        refInput.value.focus()
    }
}

function normalize(value: string) {
    // Replace accentued letter by non-accentued letter
    return value.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, "")
}

function onInput(input: InputEvent) {
    const normalizedInput = normalize(valueInput.value)
    const normalizedExpected = normalize(expected.value)

    // Display help when help character is detected
    if (input.data == props.helpCharacter && !displayHelp.value) {
        valueInput.value = ''
        displayHelp.value = true
    }

    // Emit answer when the input value math the answer
    if (expected.value != '' && normalizedInput == normalizedExpected) {
        sendAnswer()
    }

}

function resetInput() {
    displayHelp.value = false
    valueInput.value = ''
}

function setExpected(value: string) {
    // Reset input with new value sent from the parent component MainTest
    expected.value = value
    resetInput()
    startTime = new Date().getTime()
}

function sendAnswer() {
    emits('answer')
}

</script>