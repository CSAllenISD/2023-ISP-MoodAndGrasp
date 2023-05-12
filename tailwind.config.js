/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
"./pages/**/*.{js,ts,jsx,tsx}",
"/components/"

  ],
  module.exports = {
    //...
    daisyui: {
      themes: [
        {
          mytheme: {
            primary: "#a991f7",
            secondary: "#f6d860",
            accent: "#37cdbe",
            neutral: "#3d4451",
            "base-100": "#ffffff",
          },
        },
        "dark",
        "cupcake",
      ],
    },
  }
  