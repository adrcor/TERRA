<template>
  <div v-if="!store.state.global.endTestScreen" class="flex flex-col flex-1 p-2 mb-16 justify-center items-center gap-4">
    <Filters />
    <MainTest ref="refMainTest" @end-test="onEndTest" />
  </div>
  <div v-if="store.state.global.endTestScreen" class="flex flex-col flex-1 justify-center p-2 mb-16">
    <TestReview :data="reviewData" :histo="reviewHisto" :highscore="reviewHighscore" />
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import { useStore } from '@/store'
import { api } from '@/api'
import MainTest from '@/components/main-test/MainTest.vue'
import type { CountryData, InputData, TestResult, Highscore, TestParam, TestData } from '@/models'
import Filters from '@/components/main-test/Filters.vue'
import TestReview from '@/components/test-review/TestReview.vue'
import { isAuthenticated } from '@/supabase'

const store = useStore()
const refMainTest = ref<InstanceType<typeof MainTest>>()

const reviewData = ref<TestData>({
  result: {
    time: 0,
    score: 0,
    speed: 0
  },
  param: {
    region: '',
    length: 0
  }
})

const reviewHighscore = ref<TestResult>({
  time: 0,
  score: 0,
  speed: 0
})

const reviewHisto = ref<InputData[]>([])

var data: CountryData[] = []

onMounted(() => {
  setData()
  addEventListener('keydown', eventListener)
  store.commit('global/setEndTestScreen', false)
})

onUnmounted(() => removeEventListener('keydown', eventListener))

function eventListener(event: KeyboardEvent) {
  if (event.key == 'Tab') {
    event.preventDefault()
    event.stopPropagation()
    onTab()
  }
  if (event.key == 'Escape') {
    onEscape()
  }
}

async function setData() {
  const response = await api.get('/geo/all')
  data = response.data
}

async function onTab() {
  store.commit("global/setEndTestScreen", false)

  // wait until data and mainTest are loaded
  if (data.length == 0 || refMainTest.value == null) {
    for (const _ of Array(100).keys()) {
      await new Promise(r => setTimeout(r, 10))
      if (data.length) {
        break
      }
    }
  }
  const testParam = { region: store.state.filter.region, length: store.state.filter.length } 
  refMainTest.value?.resetTest()
  refMainTest.value?.launchTest(
    data.filter((country) => country.region == store.state.filter.region || store.state.filter.region == 'World'),
    testParam
  )
}

async function onEscape() {
  // wait until mainTest is loaded 
  if (refMainTest.value == null) {
    for (const _ of Array(100).keys()) {
      await new Promise(r => setTimeout(r, 10))
      if (data.length) {
        break
      }
    }
  }
  store.commit("global/setEndTestScreen", false)
  refMainTest.value?.resetTest()
}


function onEndTest(testData: TestData, histo: InputData[]) {
  reviewData.value = testData
  reviewHisto.value = histo
  store.commit("global/setEndTestScreen", true)
  afterEndTest(testData)
}

async function afterEndTest(testData: TestData) {
  if (await isAuthenticated()) {
    await getHighscore(testData)
    await logTest(testData)
  }
}

async function getHighscore(testData: TestData) {
  const response = await api.get(`/highscore/get/${testData.param?.region}/${testData.param?.length}`)
  console.log(response)
  if (response.data == 'No highscore') {
    console.log('NO HIGHSCORE')
  } else {
    reviewHighscore.value = {time: response.data.time, score: response.data.score, speed: response.data.speed}
  }

} 

async function logTest(testData: TestData) {
  const response = await api.post('/test/add', testData)
  console.log(response)
}

</script>