/** @type {import('tailwindcss').Config} */
export default {
  darkMode: "class",
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        base: {
          bg: "#0B0E12",
          panel: "#12161C",
          panel2: "#171C24",
          border: "#232A34",
          borderMuted: "#1A2029",
        },
        ink: {
          primary: "#E7EAEE",
          secondary: "#9AA5B1",
          muted: "#657081",
        },
        amber: {
          DEFAULT: "#D6A24A",
          bright: "#F2BE5C",
          dim: "#8A6A32",
        },
        status: {
          safe: "#3FA772",
          warn: "#D69A3C",
          critical: "#C24C3F",
          info: "#3E7CB8",
        },
      },
      fontFamily: {
        display: ["'IBM Plex Sans'", "sans-serif"],
        body: ["'Inter'", "sans-serif"],
        mono: ["'IBM Plex Mono'", "monospace"],
      },
      boxShadow: {
        panel: "0 1px 2px rgba(0,0,0,0.4), 0 0 0 1px rgba(255,255,255,0.02) inset",
      },
      borderRadius: {
        sm: "4px",
        DEFAULT: "6px",
        md: "8px",
      },
    },
  },
  plugins: [],
};
