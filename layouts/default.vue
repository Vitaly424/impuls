<template>
  <div class="page">
    <TheHeader />
      <nuxt />
    <!-- <TheFooter /> -->
  </div>
</template>

<script>
import TheHeader from "@/components/layouts/TheHeader.vue";
// import TheFooter from "@/components/layouts/TheFooter.vue";

export default {
  components: { TheHeader },
};
</script>
