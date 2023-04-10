import type { GeoRegion } from "@/models"


export function getTestQueryList(queryData: GeoRegion[], length: number) {
    // Set queryList as a list of random Object from queryData

    var minDistQuery = 5
    // minDistQuery can't be higher than the number of possible query
    if (queryData.length <= minDistQuery) {
        minDistQuery = queryData.length - 1
    }

    const queryList = []
    const buffer: number[] = []

    while (queryList.length < length) {
        var newIndex = getRandomIndex(length)
        while (buffer.includes(newIndex)) {
            // Redraw new value if already in buffer
            newIndex = getRandomIndex(length)
        }
        queryList.push(queryData[newIndex])
        buffer.push(newIndex)
        if (buffer.length > minDistQuery) {
            buffer.shift()
        }
    }
    return queryList
}

function getRandomIndex(length: number) {
    // Return random index of queryData
    return length * Math.random() << 0
}