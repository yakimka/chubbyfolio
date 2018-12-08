<script>
import NavBar from '@/components/NavBar';
import FooterBar from '@/components/FooterBar';

export default {
  components: {
    NavBar,
    FooterBar
  }
};
</script>

<template>
  <div>
    <nav-bar/>
    <!-- ***** Hero Area Start ***** -->
    <div class="hero-area d-flex align-items-center" v-match-heights="{el: ['.equalize']}">
      <!-- Hero Thumbnail -->
      <div class="hero-thumbnail equalize bg-img"
           style="background-image: url(/static/img/bg-img/portfolio.jpg);"></div>

      <!-- Hero Content -->
      <div class="hero-content equalize">
        <div class="container-fluid h-100">
          <div class="row h-100 align-items-center justify-content-center">
            <div class="col-12 col-md-8">
              <div class="line"></div>
              <h2>Take a look at my Portfolio</h2>
              <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent vel tortor
                facilisis, volutpat nulla placerat, tincidunt mi. Nullam vel orci dui.</p>
              <a href="#" class="btn sonar-btn white-btn">contact me</a>
            </div>
          </div>
        </div>
      </div>

      <!-- Portfolio Menu -->
      <!--<div class="sonar-portfolio-menu">-->
      <!--<div class="text-center portfolio-menu">-->
      <!--<button class="btn active" data-filter="*">All</button>-->
      <!--<button class="btn" data-filter=".landscapes">Landscapes</button>-->
      <!--<button class="btn" data-filter=".portraits">Portraits</button>-->
      <!--<button class="btn" data-filter=".fashion">Fashion</button>-->
      <!--<button class="btn" data-filter=".studio">Studio</button>-->
      <!--</div>-->
      <!--</div>-->
    </div>
    <!-- ***** Hero Area End ***** -->
    <slot/>

    <footer-bar/>
  </div>
</template>
