import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'
import { optimizeImports, icons, optimizeCss } from "carbon-preprocess-svelte";

// https://vitejs.dev/config/
export default defineConfig({
  base: '',
  plugins: [
    svelte({ preprocess: [optimizeImports(), icons(), optimizeCss()] })
  ]
})
