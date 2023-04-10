<template>
    <h1 class="text-2xl text-on-background">{{ query }}</h1>
    <UserInput ref="refUserInput" :query="query" @answer="onAnswer" />
</template>

<script setup lang="ts">
import { ref } from 'vue'
import UserInput from '../widgets/UserInput.vue';
import type { PracticeData, PracticeHisto, Region } from '@/models'
import type { Geo } from '@/models'
import { api } from '@/api';
import { getPracticeQueryList } from '@/composables/practiceQuery';

var launchRunning = false
var practiceRunning = false
var region: Region | null = null
var histo: PracticeHisto[] = []

var queryList: Geo[] = []

const refUserInput = ref<InstanceType<typeof UserInput>>()

const query = ref<string>('Press Tab to start')

defineExpose({
    resetTest,
    launchTest
})

const emits = defineEmits([
    'end-test'
])

function launchTest(data: PracticeData[] | null, r: Region): void {
    if (launchRunning || !data) {
        return
    }
    launchRunning = true
    region = r
    queryList = getPracticeQueryList(data)

    query.value = '3'
    setTimeout(() => query.value = '2', 500)
    setTimeout(() => query.value = '1', 1000)
    setTimeout(startTest, 1500)
}

function startTest() {
    practiceRunning = true
    launchRunning = false
    updateQuery()
}

function resetTest(): void {
    if (launchRunning) {
        return
    }
    practiceRunning = false
    histo = []
    query.value = 'Press Tab to start'
    refUserInput.value?.setExpected('')
}

function endTest() {
    emits('end-test', histo, region)
    resetTest()
}

function updateQuery() {
    const newQuery = queryList.shift()
    if (newQuery == undefined) {
        endTest()
        return
    }
    query.value = newQuery.country
    refUserInput.value?.setExpected(newQuery.capital)
}

function onAnswer(inputData: any) {
    const typingTime = inputData.timeTotal - inputData.timeReaction
    const msPerChar = typingTime / inputData.answer.length
    const charPerMin = Math.floor(60000 / msPerChar)
    const newLog = { country: query.value, reaction: inputData.timeReaction, typing: charPerMin, valid: inputData.valid }
    histo.push(newLog)
    updateQuery()
}

</script>