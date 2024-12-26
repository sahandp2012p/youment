<template>
  <nav
    class="navbar glass"
  >
    <div class="navbar-start flex flex-grow items-center justify-between">
      <a href="/" class="btn btn-ghost text-xl font-bold text-gray-800">YouMent</a>
      <button
        id="menu-btn"
        class="md:hidden focus:outline-none btn btn-neutral w-20 h-20 relative flex items-center justify-center"
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
          class="menu-btn__line block w-8 h-1 bg-neutral-content rounded-full transition-all ease-linear duration-200"
        ></div>
      </button>
    </div>
    <ul
      ref="menu"
      id="menu"
      class="menu menu-vertical bg-transparent fixed md:h-auto top-0 bottom-0 -left-32 md:static h-screen transition-all duration-150 ease-in-out opacity-0 md:opacity-100 md:menu-horizontal"
    >
      <li>
        <RouterLink to="/" class="text-base-content"
          >Home</RouterLink
        >
      </li>
      <li>
        <RouterLink to="/onecomment" class="text-base-content"
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
      menu.value.classList.toggle("menu--open")
      document
        .querySelector(".menu-btn__line")
        .classList.toggle("menu-btn__line--open");
  }
};
</script>

<style scoped>
.menu--open {
  @apply opacity-100 bg-base-200 left-0
}

.menu-btn__line--open {
  @apply bg-transparent;
}

.menu-btn__line::after,
.menu-btn__line::before {
  @apply block relative w-8 h-1 bg-neutral-content rounded-full transition-all ease-linear duration-200;
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

/* 
Small screens 
@media (max-width: 768px) {
  #menu {
    max-height: 0;
    transition: max-height 0.3s ease-in-out;
    overflow: hidden;
  }
}

Medium and larger screens 
@media (min-width: 768px) {
  #menu {
    max-height: none;
    overflow: visible;
    display: flex;
  }
} */

</style>
