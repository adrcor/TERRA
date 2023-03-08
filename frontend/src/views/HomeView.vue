<template>
  <div class="flex flex-col flex-1 p-2 mb-16 justify-center items-center gap-4">
    <Filters />
    <MainTest ref="refMainTest" @end-test="onEndTest"/>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import { useStore } from '@/store'
import { api } from '@/api'
import MainTest from '@/components/main-test/MainTest.vue'
import type { CountryData, TestData } from '@/components/main-test/type'
import Filters from '@/components/main-test/Filters.vue'

const store = useStore()
const refMainTest = ref<InstanceType<typeof MainTest>>()

var data: CountryData[] = []

onMounted(() => {
  setData()
  addEventListener('keydown', eventListener)
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
  console.log(response)
  data = response.data
}

async function onTab() {
  if (data.length == 0) {
    for (const _ of Array(100).keys()) {
      await new Promise(r => setTimeout(r, 10))
      console.log(data)
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
  refMainTest.value?.resetTest()
}


function onEndTest(testData: TestData) {
  console.log("ON END TEST", testData)
}

</script>