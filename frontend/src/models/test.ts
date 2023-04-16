import type { Length } from "."
import type { Region } from '.'

export interface TestData {
    param: TestParam,
    result: TestResult
}

export interface TestParam {
    region: string,
    length: number
}

export interface TestResult {
    time: number,
    score: number,
    speed: number
}

export type TestDb = {
    id: number,
    id_user: string,
    length: Length,
    region: Region,
    score: number,
    time: number,
    speed: number,
    timestamp: string,
}

export interface TestMetrics {
    time: number,
    answer: number,
    length: number,
    accuracy: number,
    speed: number
}
