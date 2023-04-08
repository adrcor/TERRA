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


var launchRunning = false
var practiceRunning = false
var region: string | null = null
var histo: {country: string, reaction: number, typing: number}[] = []


var practiceData: PracticeData[] | null = null
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
    if (launchRunning || !data) {
        return
    }
    region = r 
    launchRunning = true
    practiceData = data

    query.value = '3'
    setQueryList()

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


function setQueryList() {

    if (practiceData == null) {
        return null
    }

    const unlocked: Geo[] = practiceData
        .filter(obj => obj.unlocked)
        .map(obj => { return { country: obj.country, capital: obj.capital } as Geo })

    const weightUnlocked: number[] = practiceData
        .filter(obj => obj.unlocked)
        .map(obj => Math.max((100 - obj.grades.score), 1))

    console.log(weightUnlocked)

    const mandatory: Geo[] = shuffle(practiceData
        .filter(obj => obj.unlocked && obj.grades.score < 40)
        .map(obj => { return { country: obj.country, capital: obj.capital } as Geo }))

    queryList = []
    const buffer: string[] = []
    const minDistQuery = 3

    while (queryList.length < 10) {
        if (mandatory.length > 0) {
            const nextMandatory = mandatory.shift()
            if (!nextMandatory) {
                return
            }
            queryList.push(nextMandatory)
            buffer.push(nextMandatory.country)
        } else {
            var nextQuery = randomWeighted(unlocked, weightUnlocked)
            while (buffer.includes(nextQuery.country)) {
                nextQuery = randomWeighted(unlocked, weightUnlocked)
            }
            queryList.push(nextQuery)
            buffer.push(nextQuery.country)
        }

        if (buffer.length > minDistQuery) {
            buffer.shift()
        }
    }


}

function shuffle(array: Geo[]) {
    return array.map(value => ({ value, sort: Math.random() }))
        .sort((a, b) => a.sort - b.sort)
        .map(({ value }) => value)
}


function randomWeighted<T>(options: T[], weight: number[]): T {
    const cumulativeWeight: number[] = []
    weight.reduce((prev, curr, i) => cumulativeWeight[i] = prev + curr, 0)
    const random = Math.random() * cumulativeWeight[cumulativeWeight.length - 1]
    for (var i = 0; i < options.length; i++) {
        if (random < cumulativeWeight[i]) {
            return options[i]
        }
    }
    return options[options.length - 1]
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