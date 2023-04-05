export interface PracticeData {
    country: string,
    capital: string,
    code: string,
    region: string,
    unlocked: boolean,
    grades: Grades
}


export interface Grades {
    count: number,
    reaction: number,
    typing: number,
    score: number
}