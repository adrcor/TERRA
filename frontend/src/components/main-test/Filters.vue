<template>
    <div class="flex flex-row gap-3 w-fit items-center">
        <Dropdown :default="store.state.filter.region" :options="regionOptions" @on-update="onUpdateRegion">
            <img src="@/assets/icons/globe.svg" />
        </Dropdown>

        <Dropdown :default="store.state.filter.length" :options="lengthOptions" @on-update="onUpdateLength">
            <img src="@/assets/icons/chart-bar.svg" />
        </Dropdown>
    </div>
</template>

<script setup lang="ts">
import Dropdown from '@/components/widgets/Dropdown.vue'
import { listLength, listRegion, type Length, type Region } from '@/models';
import { useStore } from '@/store'

const store = useStore()

const lengthOptions: Length[] = listLength
const regionOptions: Region[] = listRegion


function onUpdateRegion(value: Region) {
    store.commit('filter/set_region', value)
}

function onUpdateLength(value: Length) {
    store.commit('filter/set_length', value)
}
</script>