<template>
  <section class="about">
    <div class="container">
      <div class="about__inner">
        <div class="about__content">
          <h2 class="title about__title m-color-white">
            Добро пожаловать <br />
            в интернет-магазин часов IMPULS!
          </h2>
          <div class="about__info">
            <p>
              Мы предлагаем продукцию знаменитой японской компании, которая с
              1974 года производит часы первоклассного качества. Copyright ©2022
              ООО «КАСИО», Интернет-магазин. Использование материалов возможно
              только при письменном согласии ООО «КАСИО» и наличии ссылки на
              сайт shop.casio.ru
            </p>
            <p>
              Широкий ассортимент позволяет каждому найти те часы, которые
              подойдут именно ему. Часы Casio, созданные из высококачественных
              современных материалов, стильно выглядят и никогда не подводят
              своего владельца. Вы можете заказать часы Casio с доставкой по
              всей территории России. Copyright ©2022 ООО «КАСИО»,
              Интернет-магазин. Использование материалов возможно только при
              письменном согласии ООО «КАСИО» и наличии ссылки на сайт
              shop.casio.ru
            </p>
          </div>
          <button class="btn" @click.prevent="nextCatalog">
            Перейти в каталог
          </button>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "About",
  methods: {
    nextCatalog() {
      this.$router.push("/catalog");
    },
  },
};
</script>

<style></style>
