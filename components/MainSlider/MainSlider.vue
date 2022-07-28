<template>
  <section class="main-slider">
    <div class="container">
      <div class="main-slider__swiper swiper" ref="mainSlider">
        <div class="swiper-wrapper">
          <div
            class="swiper-slide"
            v-for="slide in mainSliders"
            :key="slide.id"
          >
            <a class="main-slider__item" href="#">
              <img class="main-slider__img" :src="slide.url" :alt="slide.alt" />
            </a>
          </div>
        </div>

        <div class="main-slider__arrows">
          <button class="main-slider__arrownext">
            <SpriteIcon
              class="main-slider__arrow"
              width="20"
              height="20"
              id="#i-arrow-right"
            />
          </button>

          <button class="main-slider__arrowprev">
            <SpriteIcon
              class="main-slider__arrow"
              width="20"
              height="20"
              id="#i-arrow-left"
            />
          </button>
        </div>
      </div>

      <div
        class="swiper-pagination main-slider__pagination"
        ref="swiperPagination"
      ></div>
    </div>
  </section>
</template>

<script>
import Swiper from "@/node_modules/swiper/swiper-bundle";
import SpriteIcon from "~/components/SpriteIcon.vue";

export default {
  name: "MainSlider",
  components: {
    SpriteIcon,
  },
  data() {
    return {
      mainSliders: [
        {
          id: 1,
          url: require("@/static/main/main-slider/img1.jpg"),
          alt: "Тест",
        },
        {
          id: 2,
          url: require("@/static/main/main-slider/img2.jpg"),
          alt: "Тест",
        },
        {
          id: 3,
          url: require("@/static/main/main-slider/img3.jpg"),
          alt: "Тест",
        },
      ],
    };
  },
  methods: {
    initialSliders() {
      new Swiper(this.$refs.mainSlider, {
        slidesPerView: 1,
        effect: "fade",
        speed: 500,
        autoplay: {
          speed: 1000
        },
        touchAction: false,
        pagination: {
          el: this.$refs.swiperPagination,
          type: "bullets",
          clickable: true,
        },
        navigation: {
          nextEl: ".main-slider__arrownext",
          prevEl: ".main-slider__arrowprev",
        },
      });
    },
  },
  mounted() {
    this.initialSliders();
  },
};
</script>
