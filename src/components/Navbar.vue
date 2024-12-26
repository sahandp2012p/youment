<template>
  <nav
    class="flex items-center justify-between px-4 py-2 bg-white shadow-lg md:flex-nowrap"
  >
    <div class="flex items-center justify-between">
      <a href="/" class="text-xl font-bold text-gray-800">YouMent</a>
      <button
        id="menu-btn"
        class="md:hidden focus:outline-none w-20 h-20 relative bg-white flex items-center justify-center"
        @click="toggleMenu"
      >
        <!-- hamburger menu svg
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
        </svg> -->
        <div
          class="menu-btn__line block w-8 h-1 bg-gray-800 rounded-full transition-all ease-linear duration-200"
        ></div>
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
      document
        .querySelector(".menu-btn__line")
        .classList.toggle("menu-btn__line--open");
    } else {
      menu.value.style.maxHeight = "0";
      document
        .querySelector(".menu-btn__line")
        .classList.toggle("menu-btn__line--open");
    }
  }
};
</script>

<style scoped>
.menu-btn__line--open {
  @apply bg-transparent;
}

.menu-btn__line::after,
.menu-btn__line::before {
  @apply block relative w-8 h-1 bg-gray-800 rounded-full transition-all ease-linear duration-200;
  content: "";
}

.menu-btn__line::before {
  @apply top-2;
}

.menu-btn__line::after {
  @apply bottom-[0.7rem];
}

.menu-btn__line--open::before {
  @apply top-[0.1rem] rotate-45;
}

.menu-btn__line--open::after {
  @apply bottom-[0.1rem] -rotate-45;
}

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
