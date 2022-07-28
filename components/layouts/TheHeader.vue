<template>
  <header class="header">
    <div class="container">
      <div class="header__inner">

        <div class="header__logo logo">
          <nuxt-link to="/">IMPULS</nuxt-link>
        </div>

        <nav :class="['nav', 'mod-only-md', {'m-active': isMenu}]">
          <ul class="nav__list">
            <li class="nav__item" v-for="item in menu" :key="item.id">
              <nuxt-link class="nav__link" exact-active-class="m-active" :to="item.path">
                {{ item.name }}
              </nuxt-link>
            </li>
          </ul>
        </nav>

        <button :class="['burger-menu', 'mod-no-md ', {'m-active': isMenu}]" @click="openMenu">
           <span class="burger-menu__item"></span>
           <span class="burger-menu__item"></span>
           <span class="burger-menu__item"></span>
        </button>

      </div>
    </div>
  </header>
</template>

<script>
export default {
  data() {
    return {
      isMenu: false,
      menu: [
        {
          id: 1,
          name: "Главная",
          path: "/",
        },
        {
          id: 2,
          name: "Каталог",
          path: "/catalog",
        },
        {
          id: 3,
          name: "Как заказать",
          path: "/order-instruction",
        },
        {
          id: 4,
          name: "О компании",
          path: "/about",
        },
      ],
    };
  },
  methods: {
    openMenu() {
      this.isMenu = !this.isMenu;
    }
  }
};
</script>
