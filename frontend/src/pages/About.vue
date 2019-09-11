<template>
  <div>
    <!-- ***** Hero Area Start ***** -->
    <div class="hero-area d-flex align-items-center" v-match-heights="{el: ['.equalize']}">
      <!-- Back End Content -->
      <div class="backEnd-content">
        <img class="dots" src="/img/core-img/dots.png" alt="">
      </div>

      <!-- Hero Thumbnail -->
      <div class="hero-thumbnail aboutUs equalize bg-img"></div>

      <!-- Hero Content -->
      <div class="hero-content aboutUs equalize">
        <div class="container-fluid h-100">
          <div class="row h-100 align-items-center justify-content-center">
            <div class="col-12 col-md-10">
              <div class="line"></div>
              <h2>Hello, My name is Sam Smith and I am an experienced photographer</h2>
              <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent vel tortor
                facilisis, volutpat nulla placerat, tincidunt mi. Nullam vel orci dui. Suspendisse
                sit amet laoreet neque. Fusce sagittis suscipit sem. Lorem ipsum dolor sit amet,
                consectetur adipiscing elit. Praesent vel tortor facilisis, volutpat nulla
                placerat, tincidunt mi. Nullam vel orci dui. Suspendisse sit amet laoreet neque.
                Fusce sagittis suscipit sem.</p>
              <router-link class="btn sonar-btn white-btn"
                           :to="{name: 'contact', query: { scroll: true }}">
                contact me
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- ***** Hero Area End ***** -->

    <div class="sonar-about-us-area bg-img">
      <!-- Back End Content -->
      <div class="backEnd-content">
        <h2>Dream</h2>
      </div>

      <div class="container-fluid">
        <div class="row">
          <div class="col-12 col-md-12 col-lg-12">
            <div class="about-us-content bg-white">
              <div class="section-heading text-left wow fadeInUp" data-wow-delay="300ms">
                <div class="line"></div>
                <h2>Look at my qualities</h2>
              </div>
              <p class="wow fadeInUp" data-wow-delay="600ms">Lorem ipsum dolor sit amet,
                consectetur adipiscing elit. Praesent vel tortor facilisis, volutpat nulla
                placerat, tincidunt mi. Nullam vel orci dui. Suspendisse sit amet laoreet neque.
                Fusce sagittis suscipit sem. Lorem ipsum dolor sit amet, consectetur adipiscing
                elit. Praesent vel tortor facilisis, volutpat nulla placerat, tincidunt mi. Nullam
                vel orci dui. Suspendisse sit amet laoreet neque.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  created() {
    this.$parent.$emit('spinner-state', false);
  }
};
</script>
