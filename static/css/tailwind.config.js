/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['pricemonitor/templates/pricemonitor/*.html'],
  theme: {
    extend: {},
  },
  plugins: [require('@tailwindcss/forms')],
}