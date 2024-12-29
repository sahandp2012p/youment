import { defineConfig } from "vite";
import path from "path";
import tailwindcss from "tailwindcss";
import autoprefixer from "autoprefixer";
import vue from "@vitejs/plugin-vue";

export default defineConfig({
  root: "src",
  plugins: [
    vue(),
    {
      ...tailwindcss,
      postcss: {
        plugins: [autoprefixer],
      },
    }
  ],
  css: {
    preprocessorOptions: {
      sass: {
        // Configure global SASS settings if necessary
      },
    },
  },
  assetsInclude: ['**/*.xml'],
  build: {
    sourcemap: true, // Enable sourcemaps for both JS and CSS
    rollupOptions: {
      input: {
        main: path.resolve("src", "index.html"),
        sitemap: path.resolve("src", "sitemap.xml")
      },
    },
    outDir: "../dist",
    emptyOutDir: true,
    minify: true,
    cssMinify: true,
  },
  server: {
    open: true, // Automatically open the browser
  },
});
