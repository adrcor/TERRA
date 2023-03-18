<template>
    <div class="flex flex-col items-center text-on-background">
        <input ref="refInput" v-model="valueInput" @blur="focus" @input="event => onInput(event as InputEvent)" placeholder="Unfocused"
            class="text-center text-2xl bg-transparent outline-none caret-primary focus:placeholder-transparent placeholder-on-background placeholder-opacity-60" />
        <h1 class="h-4" :class="displayHelp == true ? 'opacity-100' : 'opacity-0'">{{ expected }}</h1>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import type { InputData } from '@/models'

const refInput = ref<HTMLInputElement>()
const valueInput = ref<string>('')
const expected = ref<string>('')
const displayHelp = ref<boolean>(false)

var startTime: number = 0
var timeReaction: number = 0


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
    setExpected
})

onMounted(() => {
    focus()
})

function focus() {
    // Keep the input focused on outside click
    refInput.value?.focus()
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

    if (expected.value != '' && normalizedInput == normalizedExpected) {
        sendAnswer()
    }
    // Check for the first correct character to set the reaction time
    if (normalizedInput.length == 1) {
        if (timeReaction == -1 && normalizedInput[0] == normalizedExpected[0]) {
            timeReaction = new Date().getTime() - startTime
        }
    }


}

function resetInput() {
    displayHelp.value = false
    valueInput.value = ''
    timeReaction = -1
}

function setExpected(value: string) {
    // Reset input with new value sent from the parent component MainTest
    expected.value = value
    resetInput()
    startTime = new Date().getTime()
}

function sendAnswer() {
    const data: InputData = {
        answer: expected.value,
        valid: !displayHelp.value,
        timeReaction: timeReaction,
        timeTotal: new Date().getTime() - startTime
    }
    emits('answer', data)
}

</script>