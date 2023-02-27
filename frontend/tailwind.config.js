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
        "on-error": "#000000"
      },
      fontFamily: {
        'sans': ['Quicksand', ...defaultTheme.fontFamily.sans]
      },
    },
  },
  plugins: [],
}
