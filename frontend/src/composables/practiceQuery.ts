import type { PracticeData, Geo } from "@/models"

export function getPracticeQueryList(practiceData: PracticeData[]): Geo[] {

    const targetLength = 10
    const validScore = 50
    const minDistQuery = 3
    const minWeight = 5
    
    const unlocked: Geo[] = practiceData
        .filter(obj => obj.unlocked)
        .map(obj => { return { country: obj.country, capital: obj.capital } as Geo })

    const weightUnlocked: number[] = practiceData
        .filter(obj => obj.unlocked)
        .map(obj => Math.max((100 - obj.grades.score), minWeight))

    const mandatory: Geo[] = shuffle(practiceData
        .filter(obj => obj.unlocked && obj.grades.score < validScore)
        .map(obj => { return { country: obj.country, capital: obj.capital } as Geo }))

    
    const queryList: Geo[] = []
    const buffer: string[] = []

    while (queryList.length < targetLength) {
        if (mandatory.length > 0) {
            const nextMandatory = mandatory.pop()
            if (!nextMandatory) {
                continue
            }
            queryList.push(nextMandatory)
            buffer.push(nextMandatory.country)
        } else {
            var nextQuery = randomWeighted(unlocked, weightUnlocked)
            while (buffer.includes(nextQuery.country)) {
                nextQuery = randomWeighted(unlocked, weightUnlocked)
            }
            queryList.push(nextQuery)
            buffer.push(nextQuery.country)
        }

        if (buffer.length > minDistQuery) {
            buffer.shift()
        }
    }
    return queryList
}

function shuffle(array: Geo[]) {
    return array.map(value => ({ value, sort: Math.random() }))
        .sort((a, b) => a.sort - b.sort)
        .map(({ value }) => value)
}

function randomWeighted<T>(options: T[], weight: number[]): T {
    const cumulativeWeight: number[] = []
    weight.reduce((prev, curr, i) => cumulativeWeight[i] = prev + curr, 0)
    const random = Math.random() * cumulativeWeight[cumulativeWeight.length - 1]
    for (var i = 0; i < options.length; i++) {
        if (random < cumulativeWeight[i]) {
            return options[i]
        }
    }
    return options[options.length - 1]
}
