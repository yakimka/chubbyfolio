<template>
  <div :class="className">
    <div class="backend-content">
      <img class="dots" src="/static/img/core-img/dots.png" alt="">
      <h2 v-if="word">{{word}}</h2>
    </div>
    <div class="portfolio-thumb">
      <img :src="photo[`image_p${num}`]" alt="">
    </div>
    <div class="portfolio-meta">
      <p class="portfolio-date">{{photo.date}}</p>
      <h2>{{photo.name}}</h2>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    className: {required: true},
    photo: {required: true},
    word: {required: false}
  },
  computed: {
    num: function () {
      let str = this.className;
      let n = str.indexOf('portfolio-item-');
      return parseInt(str.substr(n + 15, 1));
    }
  }
};
</script>

<style scoped>

</style>
