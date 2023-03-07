
<template>
    <h1 class="text-2xl text-on-background">{{ query }}</h1>
    <UserInput ref="refUserInput" @answer="onAnswer" />
</template>

<script setup lang="ts">
import { ref } from 'vue'
import UserInput from './UserInput.vue'
import type { CountryData, Metrics, TestData } from './type'

const refUserInput = ref<InstanceType<typeof UserInput>>()

var queryData: CountryData[] = []
var queryList: CountryData[] = []

var launchRunning: boolean = false
var testRunning: boolean = false

const query = ref<string>('Press Tab to start a test')

const testData: TestData = {
    time: null,
    score: null,
    speed: null,
    length: null,
    region: null
}

const metrics = ref<Metrics>({
    time: 0,
    score: 0,
    error: 0,
    length: 5,
    accuracy: 0,
    speed: 0
})

defineExpose({
    resetTest,
    launchTest
})

function resetTest(): void {
    if (!refUserInput.value) {
        return
    }
    endTest()
}

function getRandomIndex() {
    // Return random index of queryData
    return queryData.length * Math.random() << 0
}

function setQueryList() {
    // Set queryList as a list of random Object from queryData

    var minDistQuery = 5
    // minDistQuery can't be higher than the number of possible query
    if (queryData.length <= minDistQuery) {
        minDistQuery = queryData.length - 1
    }

    queryList = []
    const buffer: number[] = []

    while (queryList.length < metrics.value.length) {
        var newIndex = getRandomIndex()
        while (buffer.includes(newIndex)) {
            // Redraw new value if already in buffer
            newIndex = getRandomIndex()
        }
        queryList.push(queryData[newIndex])
        buffer.push(newIndex)
        if (buffer.length > minDistQuery) {
            buffer.shift()
        }
    }
}

function updateQuery() {
    // Update query and user input expected value
    const newQuery = queryList.shift()
    if (newQuery == undefined) {
        endTest()
        return
    }
    query.value = newQuery.country
    refUserInput.value?.setExpected(newQuery.capital)
}

function launchTest(data: CountryData[]): void {
    if (launchRunning) {
        return
    }
    launchRunning = true
    queryData = data
    setQueryList()

    query.value = '3'
    setTimeout(() => query.value = '2', 500)
    setTimeout(() => query.value = '1', 1000)
    setTimeout(startTest, 1500)
}

function onAnswer() {
    updateQuery()
}

function startTest() {
    testRunning = true
    launchRunning = false

    updateQuery()
}

function endTest() {
    query.value = 'Press Tab to start a test'
    refUserInput.value?.resetInput()
    testRunning = false

}

</script>