<template>
    <div>
        <div @mouseover="hovered = true" @mouseleave="hovered = false" class="py-1 w-6 text-sm text-center select-none"
        :class="{
            'bg-gray-500 bg-opacity-40': !data.unlocked,
            'bg-gr-25': data.unlocked && data.grades.score < 25,
            'bg-gr-50': data.unlocked && data.grades.score >= 25 && data.grades.score < 50,
            'bg-gr-75': data.unlocked && data.grades.score >= 50 && data.grades.score < 75,
            'bg-gr-100': data.unlocked && data.grades.score >= 75 && data.grades.score < 100,
            'bg-valid': data.unlocked && data.grades.score == 100
        }">
        {{data.code}}
        </div>

        <div class="absolute w-32 bg-background rounded-lg text-center translate-x-[-52px] translate-y-[2px] select-none transition-all" :class="{'opacity-95 z-50': hovered, 'opacity-0 -z-50': !hovered}">
            <div class="flex flex-col h-full w-full bg-overlay bg-opacity-5 rounded-lg">
                <a class="text-primary">{{ data.country }}</a>
                <a class="text-on-background">{{ data.grades.score }}%</a>
                <a class="text-on-background text-opacity-60">{{ (data.grades.typing / 5).toFixed() }}wpm</a>
                <a class="text-on-background text-opacity-60">{{ data.grades.reaction }}ms</a>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import type { PracticeData } from '@/models'

const props = defineProps<{
    data: PracticeData
}>()

const hovered = ref(false)

</script>