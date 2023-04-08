<template>
    <h1 class="text-2xl text-on-background">{{ query }}</h1>
    <UserInput ref="refUserInput" :query="query" @answer="onAnswer" />
</template>

<script setup lang="ts">
import { ref } from 'vue'
import UserInput from '../main-test/UserInput.vue';
import type { PracticeData } from '@/models'
import type { Geo } from '@/models'
import { api } from '@/api';
import { getQueryList } from '@/composables/practiceQuery';

var launchRunning = false
var practiceRunning = false
var region: string | null = null
var histo: {country: string, reaction: number, typing: number}[] = []

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

function launchTest(data: PracticeData[] | null, r: string): void {
    if (launchRunning) {
        return
    }
    region = r 
    launchRunning = true

    query.value = '3'

    if (!data) {
       return 
    }
    queryList = getQueryList(data)

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

    query.value = 'Press Tab to start'
    refUserInput.value?.setExpected('')
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

function endTest() {
    refUserInput.value?.setExpected('')
    query.value = 'Press Tab to start'
    logProgress()
    histo = []
    practiceRunning = false
}

async function logProgress() {
    const response = await api.post(`practice/update/${region}`, {
        params: histo
    })
    emits('end-test', response.data)
}

function onAnswer(inputData: any) {
    const typingTime = inputData.timeTotal - inputData.timeReaction
    const msPerChar = typingTime / inputData.answer.length
    const charPerMin = Math.floor(60000 / msPerChar)
    const newLog = {country: query.value, reaction: inputData.timeReaction, typing: charPerMin }
    histo.push(newLog)
    // time 200ms - length 10 
    updateQuery()
}

</script>