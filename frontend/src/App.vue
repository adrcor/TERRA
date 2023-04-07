<template>
  <div class="flex justify-center min-h-screen bg-background ">
      <div class="flex flex-col items-center gap-2 min-h-screen w-[1024px]">
        <NavBar />
        <RouterView />
      </div>
    </div>
</template>

<script setup lang="ts">
import { RouterView } from 'vue-router'
import NavBar from './components/nav-bar/NavBar.vue';
</script>