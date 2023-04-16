<template>
  <div v-if="!store.state.global.endTestScreen" class="flex flex-col flex-1 p-2 mb-8 justify-center items-center gap-4">
    <Filters />
    <MainTest ref="refMainTest" @end-test="onEndTest" />
    <button class="w-6 h-6 opacity-40" @click="onTab">
      <img v-if="!store.state.global.testRunning" src="@/assets/icons/solid/play.svg"/>
      <img v-if="store.state.global.testRunning" src="@/assets/icons/line/reset.svg"/>
    </button>
  </div>
  <div v-if="store.state.global.endTestScreen" class="flex flex-col flex-1 justify-center p-2 mb-8 items-center gap-4">
    <TestReview :data="reviewData" :histo="reviewHisto" :highscore="reviewHighscore" :state-higscore="reviewStateHighscore"/>
    <button class="w-6 h-6" @click="onTab" :class="{ 'opacity-0': store.state.global.testRunning, 'opacity-40': !store.state.global.testRunning }">
      <img src="@/assets/icons/line/reset.svg"/>
    </button>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import { useStore } from '@/store'
import { api } from '@/api'
import MainTest from '@/components/main-test/MainTest.vue'
import type { GeoRegion, InputData, TestResult, TestParam, TestData } from '@/models'
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

const reviewStateHighscore = ref<'loading' | 'normal' | 'new'>('loading')

const reviewHisto = ref<InputData[]>([])

var data: GeoRegion[] = []

onMounted(() => {
  setData()
  addEventListener('keydown', eventListener)
  store.commit('global/setEndTestScreen', false)
  store.commit("global/setTestRunning", false)
})

onUnmounted(() => {
  removeEventListener('keydown', eventListener)
  store.commit("global/setTestRunning", false)
})

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
  store.commit("global/setTestRunning", true)

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
  store.commit("global/setTestRunning", false)
  store.commit("global/setEndTestScreen", false)
  refMainTest.value?.resetTest()
}


function onEndTest(testData: TestData, histo: InputData[]) {
  reviewData.value = testData
  reviewHisto.value = histo
  store.commit("global/setEndTestScreen", true)
  store.commit("global/setTestRunning", false)
  afterEndTest(testData)
}

async function afterEndTest(testData: TestData) {
  if (await isAuthenticated()) {
    await getHighscore(testData)
    await logTest(testData)
  }
}

async function getHighscore(testData: TestData) {
  reviewStateHighscore.value = 'loading'
  const response = await api.get(`/highscore/get/${testData.param?.region}/${testData.param?.length}`)
  if (response.data == 'No highscore') {
    reviewStateHighscore.value = 'new'
  } else {
    reviewStateHighscore.value = 'normal'
    reviewHighscore.value = {time: response.data.time, score: response.data.score, speed: response.data.speed}
  }

} 

async function logTest(testData: TestData) {
  const response = await api.post('/test/add', testData)
}

</script>