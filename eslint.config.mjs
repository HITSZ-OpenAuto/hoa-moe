// eslint.config.js
import { defineConfig } from "eslint/config";
import markdown from "@eslint/markdown";

export default defineConfig([
  {
    ignores: ["themes/**", "content/docs/**"],
  },
  {
    plugins: {
      markdown,
    },
    extends: ["markdown/recommended"],
    rules: {
      "markdown/no-missing-label-refs": "off",
    },
  },
]);
