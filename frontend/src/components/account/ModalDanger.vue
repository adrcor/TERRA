<template>
    <div class="absolute flex top-0 bottom-0 left-0 right-0 bg-background bg-opacity-40 items-center justify-center backdrop-blur-sm">
        <div class="w-96 bg-background bg-opacity-50 rounded-lg">
            <div ref="modal" class="flex flex-col h-full w-full bg-overlay bg-opacity-10 rounded-lg text-center justify-between p-3 gap-2">
                <a class="text-error text-xl font-medium">Warning</a>
                <p class="text-on-background text-opacity-60">All your {{ dataType }} data will be deleted permanently, and you won't be able to retrieve it later.</p>
                <p class="text-on-background text-opacity-60">Are you sure you want to proceed?</p>
                <div class="flex flex-row gap-3">
                    <button @click="onYes" class="flex-1 rounded-md p-2 bg-error bg-opacity-5 text-error text-opacity-60 transition-all
                            hover:bg-opacity-60 hover:text-on-error hover:text-opacity-100
                            active:bg-opacity-40 active: text-opacit-60">Yes</button>
                    <button @click="onNo" class="flex-1 rounded-md p-2 bg-overlay bg-opacity-5 text-on-background text-opacity-60 transition-all
                            hover:bg-opacity-60 hover:text-on-error hover:text-opacity-100
                            active:bg-opacity-40 active: text-opacit-60">No</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
import { onClickOutside } from '@vueuse/core'
import { ref } from 'vue'

const modal = ref<HTMLDivElement>()

onClickOutside(modal, () => emits('on-close'))

const props = defineProps<{
    dataType?: string
}>()

const emits = defineEmits([
    'on-yes',
    'on-close'
])

function onYes() {
    emits('on-yes')
}

function onNo() {
    console.log('on no')
    emits('on-close')
}

</script>