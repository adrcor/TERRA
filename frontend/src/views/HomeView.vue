<template>
  <div class="flex flex-col h-screen items-center gap-3 bg-background">
    <h1 class="text-3xl text-primary">Home</h1>
    <button @click="onClick" class="px-3 py-1 rounded-xl text-2xl bg-overlay bg-opacity-10 text-on-background hover:bg-opacity-20 active:bg-opacity-10">Test Api</button>
    <a class="text-2xl text-on-background">Api result = {{ apiResult }}</a>
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