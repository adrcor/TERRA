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
        "primary": "#6eb1e1",
        "secondary": "#6ee18e",
        "background": "#121212",
        "overlay": "#ffffff",
        "error": "#cf6679",
        "on-primary": "#000000",
        "on-secondary": "#000000",
        "on-background": "#ffffff",
        "on-error": "#000000",
        "gr-20": "#cf6679",
        "gr-40": "#b6847e",
        "gr-60": "#9ea383",
        "gr-80": "#86c288",
        "gr-100": "#6ee18e",
      },
      fontFamily: {
        'sans': ['Quicksand', ...defaultTheme.fontFamily.sans]
      },
    },
  },
  plugins: [],
}
