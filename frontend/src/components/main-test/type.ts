
export interface CountryData {
    country: string,
    capital: string,
    region: string
}

export interface TestData {
    time: number,
    score: number,
    speed: number,
    length: number,
    region: string
}

export interface InputData {
    answer: string,
    valid: boolean,
    timeReaction: number,
    timeTotal: number
}

export interface Highscore {
    time: number,
    score: number,
    speed: number
}