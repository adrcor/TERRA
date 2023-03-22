import type { Length } from "./length"
import type { Region } from './region'

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
