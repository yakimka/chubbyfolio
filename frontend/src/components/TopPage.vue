<template>
  <div>
    <!-- Preloader Start -->
    <div id="preloader" v-if="loading">
      <div class="preload-content">
        <div id="sonar-load"></div>
      </div>
    </div>
    <!-- Preloader End -->
    <!-- Grids -->
    <div class="grids d-flex justify-content-between">
      <div class="grid1"></div>
      <div class="grid2"></div>
      <div class="grid3"></div>
      <div class="grid4"></div>
      <div class="grid5"></div>
      <div class="grid6"></div>
      <div class="grid7"></div>
      <div class="grid8"></div>
      <div class="grid9"></div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    loading: {
      required: true
    }
  }
};
</script>
