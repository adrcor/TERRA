<template>
  <div class="flex flex-col items-center">
    <h1 class="text-3xl">Home</h1>
    <button @click="onClick" class="text-2xl bg-blue-500 py-1 px-3 rounded-xl hover:bg-blue-400 active:bg-blue-500">Test Api</button>
    <a class="text-2xl">Api result = {{ apiResult }}</a>
  </div>
</template>


<script setup lang="ts">
import { ref } from 'vue'
import { api } from '@/api'

const apiResult = ref('')

async function onClick() {
  const response = await api.get('/')
  apiResult.value = response.data
}

</script>