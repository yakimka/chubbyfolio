<script>
import NavBar from '@/components/NavBar';
import FooterBar from '@/components/FooterBar';
import { onLayoutCreate } from '@/helpers';

export default {
  components: {
    NavBar,
    FooterBar
  },
  data() {
    return {
      loading: true
    };
  },
  created() {
    onLayoutCreate(this);
  }
};
</script>

<template>
  <div>
    <top-page :loading="loading"></top-page>

    <nav-bar/>
    <!-- ***** Hero Area Start ***** -->
    <div class="hero-area d-flex align-items-center" v-match-heights="{el: ['.equalize']}">
      <!-- Hero Thumbnail -->
      <div class="hero-thumbnail equalize bg-img"
           style="background-image: url(/img/bg-img/portfolio.jpg);"></div>

      <!-- Hero Content -->
      <div class="hero-content equalize">
        <div class="container-fluid h-100">
          <div class="row h-100 align-items-center justify-content-center">
            <div class="col-12 col-md-8">
              <div class="line"></div>
              <h2>Моё портфолио</h2>
              <p>"Сделанные мною фотопортреты больше говорят обо мне, чем о людях, которых я
                фотографирую." Ричард Эйвдон <br>
                Полагаю, что бы ни было написано в биографии, лучший способ оценить фотографа – это
                посмотреть на его портфолио. И фотографии сами все о нем расскажут.</p>
              <router-link class="btn sonar-btn white-btn"
                           :to="{name: 'contact', query: { scroll: true }}">
                контакты
              </router-link>
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
