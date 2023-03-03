<template>
  <div class="flex flex-col items-center gap-3">
    <h1 class="text-3xl text-primary">Home</h1>
    <button @click="onClick" class="px-3 py-1 rounded-xl text-2xl bg-overlay bg-opacity-10 text-on-background hover:bg-opacity-20 active:bg-opacity-10">Test Api</button>
    <a class="text-2xl text-on-background">Api result = {{ apiResult }}</a>
    <button @click="onSession" class="px-3 py-1 rounded-xl text-2xl bg-overlay bg-opacity-10 text-on-background hover:bg-opacity-20 actvie:bg-opacity-10">
      Session
    </button>
  </div>
</template>


<script setup lang="ts">
import { ref, watch } from 'vue'
import { api } from '@/api'
import { supabase } from '@/supabase'

const apiResult = ref('')

async function onClick() {
  const response = await api.get('/')
  apiResult.value = response.data
}

async function onSession() {
  const response = await supabase.auth.getSession()
  console.log(response)
}

</script>