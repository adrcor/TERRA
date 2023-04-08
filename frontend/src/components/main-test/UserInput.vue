<template>
    <div class="flex flex-col items-center text-on-background gap-3">
        <input ref="refInput" v-model="valueInput" @blur="focus" @input="event => onInput(event as InputEvent)" placeholder="Unfocused"
            class="text-center text-2xl bg-transparent outline-none caret-primary focus:placeholder-transparent placeholder-on-background placeholder-opacity-60" />
        <h1 v-if="!showAnswer" class="h-4 transition-opacity duration-1000" :class="{'opacity-60': showHelp, 'opacity-0': !showHelp}">Press / to show the answer</h1>
        <h1 v-else="" class="h-4 opacity-100">{{ expected }}</h1>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import type { InputData } from '@/models'

const refInput = ref<HTMLInputElement>()
const valueInput = ref<string>('')
const expected = ref<string>('')
const showAnswer = ref<boolean>(false)
const showHelp = ref<boolean>(false)
var helpTimeout: ReturnType<typeof setTimeout> | null = null

var startTime: number = 0
var timeReaction: number = 0

const props = defineProps({
    helpCharacter: {
        type: String,
        default: '/'
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
    if (input.data == props.helpCharacter && !showAnswer.value) {
        valueInput.value = ''
        showAnswer.value = true
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
    showAnswer.value = false
    valueInput.value = ''
    timeReaction = -1
}

function setExpected(value: string) {
    // Reset input with new value sent from the parent component MainTest
    expected.value = value
    resetInput()
    startTime = new Date().getTime()
    if (helpTimeout) {
        clearTimeout(helpTimeout)
    }
    showHelp.value = false
    helpTimeout = setTimeout(() => showHelp.value = true, 5000)
}

function sendAnswer() {
    const data: InputData = {
        answer: expected.value,
        valid: !showAnswer.value,
        timeReaction: timeReaction,
        timeTotal: new Date().getTime() - startTime
    }
    emits('answer', data)
}

</script>