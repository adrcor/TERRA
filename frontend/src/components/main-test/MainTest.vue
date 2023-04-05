<template>
    <div class="flex flex-col gap-4 items-center transition-opacity duration-75"
        :class="easeIn ? 'opacity-100' : 'opacity-0'">
        <MetricsDisplay :metrics="metrics" />
        <h1 class="text-2xl text-on-background">{{ query }}</h1>
        <UserInput ref="refUserInput" @answer="onAnswer" />
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import UserInput from './UserInput.vue'
import type { GeoRegion, LiveMetrics, InputData, TestResult, TestData, TestParam } from '@/models';
import MetricsDisplay from './MetricsDisplay.vue';

const refUserInput = ref<InstanceType<typeof UserInput>>()

var queryData: GeoRegion[] = []
var queryList: GeoRegion[] = []

var launchRunning: boolean = false
var testRunning: boolean = false

var startTime: number = -1
var histo: InputData[] = []
var score: number = 0
var error: number = 0

const easeIn = ref<boolean>(false)
setTimeout(() => easeIn.value = true, 10)

const query = ref<string>('Press Tab to start a test')

const testData: TestData = {
    result: {
        time: 0,
        score: 0,
        speed: 0
    },
    param: {
        region: '',
        length: 0
    }
}

const metrics = ref<LiveMetrics>({
    time: 0,
    answer: 0,
    length: 0,
    accuracy: 0,
    speed: 0
})

const emits = defineEmits([
    'end-test'
])

defineExpose({
    resetTest,
    launchTest
})


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
    const newQuery = queryList.shift()
    if (newQuery == undefined) {
        endTest()
        return
    }
    query.value = newQuery.country
    refUserInput.value?.setExpected(newQuery.capital)
}

function updateMetrics() {
    // Update displayed metrics and stop test when time is up
    const currTime = new Date().getTime()
    const spentTime = currTime - startTime

    if (score + error != metrics.value.answer) {
        metrics.value.answer = score + error
        metrics.value.accuracy = score / (score + error)
        metrics.value.speed = score / spentTime * 60000000
    }

    metrics.value.time = spentTime

    if (testRunning) {
        setTimeout(updateMetrics, 1000 / 60)
    }
}

function launchTest(data: GeoRegion[], testParam: TestParam): void {
    if (launchRunning) {
        return
    }
    launchRunning = true

    queryData = data
    testData.param = testParam
    metrics.value.length = testParam.length

    query.value = '3'
    setQueryList()

    setTimeout(() => query.value = '2', 500)
    setTimeout(() => query.value = '1', 1000)
    setTimeout(startTest, 1500)
}

function startTest() {
    testRunning = true
    launchRunning = false
    startTime = new Date().getTime()

    updateQuery()
    updateMetrics()
}

function resetTest(): void {
    if (launchRunning) {
        return
    }
    testRunning = false

    metrics.value.time = 0
    metrics.value.answer = 0
    metrics.value.accuracy = 0
    metrics.value.speed = 0

    histo = []
    score = 0
    error = 0

    query.value = 'Press Tab to start a test'
    refUserInput.value?.setExpected('')
}

function endTest() {
    emitData()
    refUserInput.value?.setExpected('')
    testRunning = false

}

function emitData() {
    const testTime = new Date().getTime() - startTime

    const testResult: TestResult = {
        time: testTime,
        score: score,
        speed: Math.floor(score / testTime * 60000000)
    }
    testData.result = testResult
    emits('end-test', testData, histo)
}

function onAnswer(inputData: InputData) {
    if (inputData.valid) {
        score += 1
    } else {
        error += 1
    }
    histo.push(inputData)
    updateQuery()
}

</script>