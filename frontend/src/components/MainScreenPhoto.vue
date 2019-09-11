<template>
  <div :class="className">
    <div class="backend-content" v-if="backendContent">
      <img class="dots" src="/img/core-img/dots.png" alt="">
      <h2 v-if="word">{{word}}</h2>
    </div>
    <div class="portfolio-thumb">
      <img :src="photo[`image`]" alt="">
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
    className: { required: true },
    photo: { required: true },
    word: { required: false },
    backendContent: {
      required: false,
      default: true
    }
  }
};
</script>

<style scoped>

</style>
