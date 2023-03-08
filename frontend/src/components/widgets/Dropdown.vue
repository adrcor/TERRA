<template>
    <div class="flex flex-col flex-grow min-w-[128px] relative">
        <button ref="refButton" @click="open = !open"
            class="flex flex-1 gap-1 p-2 rounded-md border-2 text-on-background opacity-60 hover:opacity-100">
            <div class="w-6 h-6">
                <slot></slot>
            </div>
            <div class="flex-1 text-center truncate">{{ selected }}</div>
        </button>

        <div ref="refDropdown" v-if="open"
            class="flex flex-col absolute w-full my-[3rem] rounded-md bg-background border-2 border-on-background border-opacity-60 hover:border-opacity-100">
            <button v-for="element in props.options" @click="onSelect(element)"
                class="text-on-background hover:bg-overlay hover:bg-opacity-5 text-opacity-60 hover:text-opacity-100 py-1">
                {{ element }}
            </button>
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'


const props = defineProps<{
    default: string,
    options: string[]
}>()

const open = ref<boolean>(false)
const refDropdown = ref<HTMLDivElement>()
const refButton = ref<HTMLDivElement>()
const selected = ref(props.default)

const emits = defineEmits([
    'on-update'
])

onMounted(() => addEventListener('click', checkClickOutside))
onUnmounted(() => removeEventListener('click', checkClickOutside))

function checkClickOutside(event: MouseEvent) {
    // Close dropdown if click outside of it
    if (event.target == null) {
        return
    }
    if (open.value && !refDropdown.value?.contains(event.target as Node) && !refButton.value?.contains(event.target as Node)) {
        open.value = false
    }
}

function onSelect(element: string) {
    open.value = false
    selected.value = element
    emits('on-update', selected.value)
}

</script>

