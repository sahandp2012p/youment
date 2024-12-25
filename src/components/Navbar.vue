<template>
  <nav
    class="flex items-center justify-between px-4 py-2 bg-white shadow-lg md:flex-nowrap"
  >
    <div class="flex items-center justify-between">
      <a href="/" class="text-xl font-bold text-gray-800">YouMent</a>
      <button
        id="menu-btn"
        class="md:hidden focus:outline-none"
        @click="toggleMenu"
      >
        <!-- hamburger menu svg -->
        <svg
          class="w-6 h-6 text-gray-800"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M4 6h16M4 12h16m-7 6h7"
          ></path>
        </svg>
      </button>
    </div>
    <ul
      ref="menu"
      id="menu"
      class="overflow-hidden max-h-0 transition-all duration-300 ease-in-out md:overflow-visible md:max-h-none md:flex md:flex-row md:space-x-8"
    >
      <li>
        <RouterLink to="/" class="text-gray-700 hover:text-indigo-500"
          >Home</RouterLink
        >
      </li>
      <li>
        <RouterLink to="/onecomment" class="text-gray-700 hover:text-indigo-500"
          >One Comment Test</RouterLink
        >
      </li>
    </ul>
  </nav>
</template>

<script setup>
import { ref } from "vue";
import { RouterLink } from "vue-router";

const menu = ref(null);
const isOpen = ref(false);

const toggleMenu = () => {
  if (menu.value) {
    isOpen.value = !isOpen.value;
    if (isOpen.value) {
      menu.value.style.maxHeight = menu.value.scrollHeight + "px";
    } else {
      menu.value.style.maxHeight = "0";
    }
  }
};
</script>

<style scoped>
/* Small screens */
@media (max-width: 768px) {
  #menu {
    max-height: 0;
    transition: max-height 0.3s ease-in-out;
    overflow: hidden;
  }
}

/* Medium and larger screens */
@media (min-width: 768px) {
  #menu {
    max-height: none;
    overflow: visible;
    display: flex;
  }
}
</style>
