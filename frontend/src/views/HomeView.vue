<template>
  <div v-if="!store.state.global.endTestScreen" class="flex flex-col flex-1 p-2 mb-16 justify-center items-center gap-4">
    <Filters />
    <MainTest ref="refMainTest" @end-test="onEndTest"/>
  </div>
  <div v-if="store.state.global.endTestScreen" class="flex flex-col flex-1 justify-center p-2 mb-16">
    <TestReview :data="reviewData" :histo="reviewHisto"/>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import { useStore } from '@/store'
import { api } from '@/api'
import MainTest from '@/components/main-test/MainTest.vue'
import type { InputData, CountryData, TestData } from '@/components/main-test/type'
import Filters from '@/components/main-test/Filters.vue'
import TestReview from '@/components/test-review/TestReview.vue'

const store = useStore()
const refMainTest = ref<InstanceType<typeof MainTest>>()

const reviewData = ref<TestData>({
  time: 0,
  score: 0,
  speed: 0,
  length: 1,
  region: ''
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

  refMainTest.value?.resetTest()
  refMainTest.value?.launchTest(
    data.filter((country) => country.region == store.state.filter.region || store.state.filter.region == 'World'),
    store.state.filter.length,
    store.state.filter.region
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
}

</script>