<template>
  <div>
    <!-- ***** Hero Area Start ***** -->
    <div class="hero-area d-flex align-items-center" v-match-heights="{el: ['.equalize']}">
      <!-- Back End Content -->
      <div class="backEnd-content">
        <img class="dots" src="/static/img/core-img/dots.png" alt="">
      </div>

      <!-- Hero Thumbnail -->
      <div class="hero-thumbnail aboutUs equalize bg-img"
           style="background-image: url(/static/img/bg-img/about.jpg);"></div>

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
              <a href="#" class="btn sonar-btn white-btn">contact me</a>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- ***** Hero Area End ***** -->

    <div class="sonar-about-us-area bg-img" style="background-image: url(/static/img/bg-img/about2.jpg);">
      <!-- Back End Content -->
      <div class="backEnd-content">
        <h2>Dream</h2>
      </div>

      <div class="container-fluid">
        <div class="row">
          <div class="col-12 col-md-10 col-lg-7">
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
              <!-- Progress Bar Content Area -->
              <div class="services-progress-bar mt-50 wow fadeInUp" data-wow-delay="900ms">
                <!-- Single Progress Bar -->
                <div class="single_progress_bar">
                  <div id="bar1" class="barfiller">
                    <div class="tipWrap">
                      <span class="tip"></span>
                    </div>
                    <span class="fill" data-percentage="80"></span>
                  </div>
                  <p>Pacience</p>
                </div>
                <!-- Single Progress Bar -->
                <div class="single_progress_bar">
                  <div id="bar2" class="barfiller">
                    <div class="tipWrap">
                      <span class="tip"></span>
                    </div>
                    <span class="fill" data-percentage="90"></span>
                  </div>
                  <p>Creativity</p>
                </div>
                <!-- Single Progress Bar -->
                <div class="single_progress_bar">
                  <div id="bar3" class="barfiller">
                    <div class="tipWrap">
                      <span class="tip"></span>
                    </div>
                    <span class="fill" data-percentage="100"></span>
                  </div>
                  <p>Commited</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="sonar-about-us-area second-part bg-img"
         style="background-image: url(/static/img/bg-img/about3.jpg);">
      <!-- Back End Content -->
      <div class="backEnd-content">
        <h2>Really</h2>
      </div>

      <div class="container-fluid">
        <div class="row justify-content-end">
          <div class="col-12 col-md-10 col-lg-7">
            <div class="about-us-content bg-white">
              <div class="section-heading text-left wow fadeInUp" data-wow-delay="300ms">
                <div class="line"></div>
              </div>
              <p class="wow fadeInUp" data-wow-delay="600ms">Consectetur adipiscing elit. Praesent
                vel tortor facilisis, volutpat nulla placerat, tincidunt mi. Nullam vel orci dui.
                Suspendisse sit amet laoreet neque. Fusce sagittis suscipit sem. Lorem ipsum dolor
                sit amet, consectetur adipiscing elit. Praesent vel tortor facilisis, volutpat
                nulla placerat, tincidunt mi. Nullam vel orci dui. Suspendisse sit amet laoreet
                neque.</p>
              <div class="row mt-100 text-center wow fadeInUp" data-wow-delay="900ms">
                <div class="col-12 col-sm-6 col-md-4">
                  <div class="single-pie-bar" data-percent="90">
                    <canvas class="bar-circle" width="100" height="100"></canvas>
                    <p>Landsacpes</p>
                  </div>
                </div>
                <div class="col-12 col-sm-6 col-md-4">
                  <div class="single-pie-bar" data-percent="65">
                    <canvas class="bar-circle" width="100" height="100"></canvas>
                    <p>Portraits</p>
                  </div>
                </div>
                <div class="col-12 col-sm-6 col-md-4">
                  <div class="single-pie-bar" data-percent="25">
                    <canvas class="bar-circle" width="100" height="100"></canvas>
                    <p>Studio</p>
                  </div>
                </div>
              </div>
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
