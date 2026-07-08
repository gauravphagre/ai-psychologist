import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./index.html",
    "./src/**/*.{ts,tsx}",
  ],

  theme: {
    extend: {
      colors: {
        background: "#0f172a",
        surface: "#1e293b",
        card: "#334155",
        primary: "#3b82f6",
        success: "#22c55e",
        warning: "#f59e0b",
        danger: "#ef4444",
      },

      borderRadius: {
        xl: "1rem",
        "2xl": "1.25rem",
      },
    },
  },

  plugins: [],
};

export default config;