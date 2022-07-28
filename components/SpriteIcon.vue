<template>
  <svg :width="width" :height="height">
    <use :xlink:href="link"></use>
  </svg>
</template>

<script>
export default {
  name: "SpriteIcon",
  props: {
    id: {
      type: String,
      require: true,
      validator(value) {
        if (value.indexOf("#") === 0) return true;

        console.warn(`id '${value}' должен начинаться с '#'`);
        return false;
      },
    },
    width: {
      type: [Number, String],
      default: 40,
    },
    height: {
      type: [Number, String],
      default: 40,
    },
  },
  computed: {
    link() {
      return require("../static/icons/icons-sprite.svg") + this.id;
    },
  },
};
</script>
