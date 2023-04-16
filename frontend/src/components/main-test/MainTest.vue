<template>
    <div class="flex flex-col gap-4 items-center transition-opacity duration-75"
        :class="easeIn ? 'opacity-100' : 'opacity-0'">
        <MetricsDisplay :metrics="metrics" />
        <a class="text-2xl text-on-background">{{ query }}</a>
        <NewUserInput ref="refUserInput" @answer="onAnswer" />
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
//import UserInput from '../widgets/UserInput.vue'
import type { GeoRegion, TestMetrics, InputData, TestResult, TestData, TestParam } from '@/models';
import MetricsDisplay from './MetricsDisplay.vue'
import { getTestQueryList } from '@/composables/testQuery'
import NewUserInput from '../widgets/newUserInput.vue'

const refUserInput = ref<InstanceType<typeof NewUserInput>>()

var queryList: GeoRegion[] = []

var launchRunning: boolean = false
var testRunning: boolean = false

var histo: InputData[] = []
var startTime: number = -1
var score: number = 0
var error: number = 0

// Avoid text flashing when tabing from the end-test review
const easeIn = ref<boolean>(false)
setTimeout(() => easeIn.value = true, 10)

const query = ref<string>('Press Tab to start')

var testParam: TestParam = {
    region: '',
    length: 0
}

const metrics = ref<TestMetrics>({
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

function launchTest(data: GeoRegion[], param: TestParam) {
    if (launchRunning) {
        return
    }
    launchRunning = true

    testParam = param
    metrics.value.length = testParam.length
    
    queryList = getTestQueryList(data, testParam.length)

    query.value = '3'
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

function resetTest() {
    if (launchRunning) {
        return
    }
    testRunning = false

    metrics.value.time = 0
    metrics.value.answer = 0
    metrics.value.accuracy = 0
    metrics.value.speed = 0
    metrics.value.length = 0

    histo = []
    score = 0
    error = 0

    query.value = 'Press Tab to start'
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
    
    const out: TestData = {
        result: testResult,
        param: testParam
    }

    emits('end-test', out, histo)
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