/** @type {import('tailwindcss').Config} */
const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx,vue}",
  ],
  theme: {
    extend: {
      colors: {
        "primary": "#60b0f0",
        "secondary": "#70e090",
        "background": "#121212",
        "overlay": "#ffffff",
        "valid": "#70e090",
        "error": "#d06090",
        "on-primary": "#000000",
        "on-secondary": "#000000",
        "on-background": "#ffffff",
        "on-error": "#000000",
        "gr-25": "#cf6679",
        "gr-50": "#b6847e",
        "gr-75": "#9ea383",
        "gr-100": "#86c288",
      },
      fontFamily: {
        'sans': ['Quicksand', ...defaultTheme.fontFamily.sans]
      },
    },
  },
  plugins: [],
}
