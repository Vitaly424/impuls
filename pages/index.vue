<template>
  <div class="page">
    <MainSlider />
    <About />
  </div>
</template>

<script>
import MainSlider from "@/components/MainSlider/MainSlider.vue";
import About from "@/components/About/About.vue";

export default {
  name: "IndexPage",
  components: { MainSlider, About },
};
</script>

<style>
</style>
