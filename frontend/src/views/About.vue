<template>
  <div>
    <!-- ***** Hero Area Start ***** -->
    <div class="hero-area d-flex align-items-center" v-match-heights="{el: ['.equalize']}">
      <!-- Back End Content -->
      <div class="backEnd-content">
        <img class="dots" src="/img/core-img/dots.png" alt="">
      </div>

      <!-- Hero Thumbnail -->
      <div class="hero-thumbnail aboutUs equalize bg-img"
           style="background-image: url(/img/bg-img/about.jpg);"></div>

      <!-- Hero Content -->
      <div class="hero-content aboutUs equalize">
        <div class="container-fluid h-100">
          <div class="row h-100 align-items-center justify-content-center">
            <div class="col-12 col-md-10">
              <div class="line"></div>
              <h2>Приветствую Вас! Меня зовут Ира и я фотограф:)</h2>
              <p>Каждый человек уникален! Через объектив моего фотоаппарата я покажу Вас настоящих.
                Такие снимки – драгоценные мгновения жизни, которыми Вы сможете поделиться со всем
                миром! До встречи на фотосессии!</p>
              <router-link class="btn sonar-btn white-btn"
                           :to="{name: 'contact', query: { scroll: true }}">
                связаться со мной
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- ***** Hero Area End ***** -->

    <div class="sonar-about-us-area bg-img">
      <div class="container-fluid">
        <div class="row">
          <div class="col-12 col-md-12 col-lg-12">
            <div class="about-us-content bg-white-alpha">
              <div class="section-heading text-left wow fadeInUp" data-wow-delay="300ms">
                <div class="line"></div>
                <h2>Обо мне</h2>
              </div>
              <p class="wow fadeInUp" data-wow-delay="600ms">Смею предположить, что Вы посетили мой
                сайт с целью найти “своего фотографа”, а
                значит Вы верите (как и я), что фотография ценна. Она может придать глубину и
                значимость жизни. Не только сегодня, но и годы спустя.
                Фотография всегда была моим хобби, но благодаря Киевской школе фотографии мое
                увлечение превратилось в профессию. Основными жанрами, в которых я работаю являются
                портретная фотография, репортажная съемка, а также food photo.
              </p>
              <div class="section-heading text-left mt-100 wow fadeInUp" data-wow-delay="300ms">
                <div class="line"></div>
                <h2>Мои сертификаты</h2>
              </div>
              <div class="wow fadeInUp" data-wow-delay="600ms">
                <div class="hero-area">
                  <carousel class="hero-slides"
                            :items="2"
                            :margin="40"
                            :loop="true"
                            :dots="false"
                            :autoplay="true"
                            :autoplayTimeout="5000"
                            :smartSpeed="1000"
                            :nav="false"
                            :responsive="{
                            0: {
                                items: 1
                            },
                            992: {
                                items: 2
                            },
                            1280: {
                                items: 3
                            }}">
                    <!-- Single Hero Slide -->
                    <img alt="сертификат" v-for="i in numberOfCerts" :key="i"
                         :src="`${certPath}${i}.${certExt}`">
                  </carousel>
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
import carousel from 'vue-owl-carousel';

const certificateName = 'cert_';

export default {
  data() {
    return {
      numberOfCerts: 6,
      certPath: `/img/certs/${certificateName}`,
      certExt: 'jpg',
      phoneNumber: ''
    };
  },
  components: { carousel },
  created() {
    this.$parent.$emit('spinner-state', false);
  }
};
</script>
