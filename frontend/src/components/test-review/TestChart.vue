<template>
    <Bar :data="chartData" :options="chartOptions" />
</template>

<script setup lang="ts">
import { ref, toRaw, onMounted } from 'vue'
import { Bar } from 'vue-chartjs'
import type {ChartOptions, ChartData} from 'chart.js'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
import type { InputData } from '../main-test/type';

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

const chartData = ref<ChartData<'bar'>>({
    datasets: []
})

const chartOptions: ChartOptions<'bar'> = {
    responsive: true,
    scales: {
        x: {
            stacked: true,
            display: false,
        },
        y: {
            stacked: true,
            ticks: {
                callback: function(val: string | number, _index: number): string | number {
                    if (typeof(val) == "number") {
                        return val % 1000 === 0 ? val : ''
                    } else {
                        return ''
                    }
                }
            },
            border: {
                display: false
            },
            grid: {
                color: function(context) {
                    console.log(context)
                    console.log(typeof(context))
                    if (context.tick.value % 1000 === 0) {
                        return '#444444'
                    } else {
                        return '#222222'
                    }
                }
            }
        },
    },
    plugins: {
        tooltip: {
            displayColors: false,
            titleAlign: 'center',
            bodyAlign: 'center',
            footerAlign: 'center',
            bodyColor: '#ffffff99',
            titleColor: '#6eb1e1',

            callbacks: {
                title: function(context) {

                },
                label: function (context) {
                    const index = context.dataIndex
                    if (props.histo[index].valid) {
                        const reaction = (props.histo[index].timeReaction / 1000).toFixed(3)
                        const typing = ((props.histo[index].timeTotal - props.histo[index].timeReaction) / 1000).toFixed(3)
                        return [
                            'Reaction: ' + reaction + 's',
                            'Typing: ' + typing + 's',
                        ]
                    } else {
                        return ['Help']
                    }
                },
                footer: function (items) {
                    var total = 0;
                    for (var i = 0; i < chartData.value.datasets.length; i++) {
                        const temp = chartData.value.datasets[i].data[items[0].dataIndex]
                        if (typeof(temp) == 'number') {
                            total += temp
                        }
                    }

                    return 'Total: ' + (total / 1000).toFixed(3) + 's'
                }
            }
        },
        legend: {
            display: false
        }
    },
}

const props = defineProps<{
    histo: InputData[]
}>()

onMounted(() => updateChart())

function getChartData(labels: string[], reactionTime: number[], typingTime: number[], error: number[]): ChartData<'bar'> {
    return {
        labels: labels,
        datasets: [{
            label: 'Reaction Time',
            backgroundColor: '#6ee18e',
            data: reactionTime
        },
        {
            label: 'Typing Time',
            backgroundColor: '#6eb1e1',
            data: typingTime
        },
        {
            label: 'Error',
            backgroundColor: '#cf6679',
            data: error
        }]
    }
}

function updateChart() {
    const histo = toRaw(props.histo)
    const labels = histo.map((item) => item.answer)
    const reactionTime = histo.map(item => { if (item.valid) { return item.timeReaction } else { return 0 } })
    const typingTime = histo.map(item => { if (item.valid) { return item.timeTotal - item.timeReaction } else { return 0 } })
    const error = histo.map(item => { if (!item.valid) { return item.timeTotal } else { return 0 } })
    chartData.value = getChartData(labels, reactionTime, typingTime, error)
}

</script>