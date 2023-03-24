<template>
    <div class="w-2/3 h-1/2 p-4 border-2 border-overlay border-opacity-60 rounded-lg">
        <Line :data="chartData" :options="chartOptions"/>
    </div>
</template>

<script setup lang="ts">
import { Line } from 'vue-chartjs'
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from 'chart.js'
import type { ChartOptions, ChartData } from 'chart.js'
import type { TestDb } from '@/models';
import { ref, toRaw } from 'vue';

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend)

const props = defineProps<{
    data: TestDb[]
}>()

defineExpose({
    updateChart
})

const chartData = ref<ChartData<'line'>>({
    datasets: []
})

const chartOptions: ChartOptions<'line'> = {
    responsive: true,
    maintainAspectRatio: false,
    pointRadius: 4,
    hoverRadius: 8,
    showLine: false,
    interaction: {
        mode: 'nearest',
        intersect: false
    },
    scales: {
        x: {
            stacked: true,
            display: false
        },
        ySpeed: {
            type: 'linear',
            display: true,
            position: 'right',
            min: 0,
            border: {
                display: false
            },
            grid: {
                color: '#222222'
            },
            ticks: {
                color: '#666666'
            }
        }
    },
    plugins: {
        title: {
            display: false,
        },
        legend: {
            display: false,
        },
        tooltip: {
            displayColors: false,
            titleAlign: 'center',
            bodyAlign: 'center',
            footerAlign: 'center',
            footerFont: { weight: 'light' },
            backgroundColor: '#000000aa',
            footerColor: '#666666',
            bodyColor: '#ffffff99',
            titleColor: '#6eb1e1',

            callbacks: {
                title: function (context) {
                    const speed = context[0].raw as number
                    return speed.toFixed(3)
                },
                label: function (context) {
                    const index = context.dataIndex
                    const data = toRaw(props.data)
                    return [
                        data[index].score / data[index].length + '%',
                        (data[index].time / 1000).toFixed(3) + 's'
                    ]
                },
                footer: function (context) {
                    const timestamp = context[0].label
                    const date = timestamp.split('T')[0]
                    const [_weekday, month, day, year] = new Date(date).toDateString().split(' ')
                    
                    const time = timestamp.split('T')[1].split('.')[0]
                    const [hour, min, _sec] = time.split(':')
                    return `${day} ${month} ${year} - ${hour}:${min}`
                }
            }
        }
    }
} as ChartOptions<'line'>

function getChartData(labels: string[], speed: number[]) {
    return {
        labels: labels,
        datasets: [{
            label: 'Speed',
            backgroundColor: '#6eb1e1',
            data: speed,
            yAxisID: 'ySpeed'
        }
        ]
    }
}

function updateChart(data: TestDb[]) {
    console.log('chart', data)
    const labels = data.map((item) => item.timestamp)
    const speed = data.map((item) => item.speed / 1000)
    chartData.value = getChartData(labels, speed)
}

</script>