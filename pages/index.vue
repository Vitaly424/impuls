<template>
  <div class="page">
    <MainSlider />
    <About />

    <div class="container">
      <h2 class="title">Тестовые данные</h2>

      <button v-if="!list.length > 0" class="btn" type="button" @click.prevent="getData">
        Загрузить
      </button>

      <ul v-if="list.length">
        <li v-for="(item, index) in list" :key="index">
          <h3 class="title-small">{{item.title_brand}}</h3>
        </li>
      </ul>
      
      <p style="margin-top: 20px;" v-if="loading">Загрузка...</p>
    </div>
  </div>
</template>

<script>
import MainSlider from "@/components/MainSlider/MainSlider.vue";
import About from "@/components/About/About.vue";

export default {
  name: "IndexPage",
  components: { MainSlider, About },
  data() {
    return {
      list: [],
      loading: false
    };
  },
  methods: {
    async getData() {
      try {
        this.loading = true;
        const response = await fetch("https://musiclala.pythonanywhere.com/api/brands/?format=json");
        const data = await response.json();
        this.list = data;
        this.loading = false;
      } catch (e) {
        alert(e);
      }
    },
  },
};
</script>

<style></style>
