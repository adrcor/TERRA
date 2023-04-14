export const Color = {
    primary: '#60b0f0',
    secondary: '#70e090',
    valid: "#70e090",
    error: '#d06090',
    background: '#121212',
    white: '#ffffff',
    black: '#000000',
    opacity5: '0d',
    opacity20: '33',
    opacity40: '66',
    opacity60: '99',
    opacity80: 'cc'
}

export const Gradient = {
    gr20: Color.error,
    gr40: rgbToHex(Array.from(Array(3).keys()).map(index => Math.floor(hexToRgb(Color.error)[index] * .75 + hexToRgb(Color.valid)[index] * .25))),
    gr60: rgbToHex(Array.from(Array(3).keys()).map(index => Math.floor(hexToRgb(Color.error)[index] * .50 + hexToRgb(Color.valid)[index] * .50))),
    gr80: rgbToHex(Array.from(Array(3).keys()).map(index => Math.floor(hexToRgb(Color.error)[index] * .25 + hexToRgb(Color.valid)[index] * .75))),
    gr100: Color.valid
}

function hexToRgb(hex: string) {
    const r = parseInt(hex.slice(1, 3), 16)
    const g = parseInt(hex.slice(3, 5), 16)
    const b = parseInt(hex.slice(5, 7), 16)
    return [r, g, b]
}

function rgbToHex(rgb: number[]) {
    return '#' + rgb[0].toString(16) + rgb[1].toString(16) + rgb[2].toString(16) 
}