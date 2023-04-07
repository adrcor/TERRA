<template>
    <div class="w-2/3 h-1/2 p-4 bg-overlay bg-opacity-5 rounded-lg">
        <Line :data="chartData" :options="chartOptions"/>
    </div>
</template>

<script setup lang="ts">
import { Line } from 'vue-chartjs'
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from 'chart.js'
import type { ChartOptions, ChartData } from 'chart.js'
import type { TestDb } from '@/models';
import { ref, toRaw } from 'vue';
import { Color } from '@/models';

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
            title: {
                display: true,
                text: 'Speed',
                font: {
                    size: 14
                }
            },
            position: 'right',
            min: 0,
            border: {
                display: false
            },
            grid: {
                color: Color.white + Color.opacity5
            },
            ticks: {
                color: Color.white + Color.opacity40
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
            backgroundColor: Color.background + Color.opacity80,
            footerColor: Color.white + Color.opacity60,
            bodyColor: Color.white + Color.opacity80,
            titleColor: Color.primary,

            callbacks: {
                title: function (context) {
                    const speed = context[0].raw as number
                    return speed.toFixed(3)
                },
                label: function (context) {
                    const index = context.dataIndex
                    const data = toRaw(props.data)
                    return [
                        Math.floor(data[index].score / data[index].length * 100) + '%',
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
            backgroundColor: Color.primary,
            data: speed,
            yAxisID: 'ySpeed'
        }
        ]
    }
}

function updateChart(data: TestDb[]) {
    const labels = data.map((item) => item.timestamp)
    const speed = data.map((item) => item.speed / 1000)
    chartData.value = getChartData(labels, speed)
}

</script>