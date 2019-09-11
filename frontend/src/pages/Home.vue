<template>
  <div>
    <div class="hero-area" v-if="photosets && photosets.length > 3">
      <carousel class="hero-slides"
                :items="4"
                :margin="0"
                :loop="true"
                :dots="true"
                :autoplay="true"
                :autoplayTimeout="5000"
                :smartSpeed="1000"
                :nav="false"
                :responsive="{
                0: {
                    items: 1
                },
                576: {
                    items: 2
                },
                992: {
                    items: 3
                },
                1600: {
                    items: 4
                }}"
                v-if="isPhotosets">
        <!-- Single Hero Slide -->
        <div v-for="photoset in photosets" :key="photoset.id"
             class="single-hero-slide bg-img slide-background-overlay"
             :style="{ backgroundImage: `url(${photoset.preview})` }"
             @click="redirectToPhotoset(photoset.id)">
          <div class="container h-100">
            <div class="row h-100 align-items-end">
              <div class="col-12">
                <div class="hero-slides-content">
                  <div class="line"></div>
                  <h2>{{ photoset.name }}</h2>
                  <p>{{ photoset.description }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </carousel>
    </div>

    <!-- ***** Portfolio Area Start ***** -->
    <div class="portfolio-area section-padding-100">
      <div class="container">
        <div class="row">
          <div class="col-12">
            <div class="portfolio-title">
              <h2>“Разве не чудо, что камера умеет останавливать время, навсегда сохраняя в памяти
                волшебные моменты: красивые закаты, дни рождения, глазированные капкейки с соленой
                карамелью, покрытые глазурью?” Зои Сагг</h2>
            </div>
          </div>
        </div>

        <div v-if="isHas7Photos">
          <div class="row justify-content-between">
            <!-- Single Portfoio Area -->
            <div class="col-12 col-md-5">
              <main-screen-photo
                class-name="single-portfolio-item mt-100 portfolio-item-1 wow fadeIn"
                :photo="mainScreenPhotos[0]"
                word="Reality"></main-screen-photo>
            </div>
            <!-- Single Portfoio Area -->
            <div class="col-12 col-md-6">
              <main-screen-photo
                class-name="single-portfolio-item mt-230 portfolio-item-2 wow fadeIn"
                :photo="mainScreenPhotos[1]"></main-screen-photo>
            </div>
          </div>

          <div class="row">
            <!-- Single Portfoio Area -->
            <div class="col-12 col-md-10">
              <main-screen-photo
                class-name="single-portfolio-item mt-100 portfolio-item-3 wow fadeIn"
                :photo="mainScreenPhotos[2]"
                word="Photography"></main-screen-photo>
            </div>
          </div>

          <div class="row justify-content-end">
            <!-- Single Portfoio Area -->
            <div class="col-12 col-md-6">
              <main-screen-photo class-name="single-portfolio-item portfolio-item-4 wow fadeIn"
                                 :photo="mainScreenPhotos[3]"></main-screen-photo>
            </div>
          </div>

          <div class="row">
            <!-- Single Portfoio Area -->
            <div class="col-12 col-md-5">
              <main-screen-photo class-name="single-portfolio-item portfolio-item-5 wow fadeIn"
                                 :photo="mainScreenPhotos[4]"
                                 word="Hope"></main-screen-photo>
            </div>
          </div>

          <div class="row justify-content-center">
            <!-- Single Portfoio Area -->
            <div class="col-12 col-md-4">
              <main-screen-photo class-name="single-portfolio-item portfolio-item-6 wow fadeIn"
                                 :photo="mainScreenPhotos[5]"
                                 :backend-content="false"></main-screen-photo>
            </div>
          </div>

          <div class="row justify-content-end">
            <!-- Single Portfoio Area -->
            <div class="col-12 col-md-4">
              <main-screen-photo class-name="single-portfolio-item portfolio-item-7 wow fadeIn"
                                 :photo="mainScreenPhotos[6]"
                                 word="Future"></main-screen-photo>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- ***** Portfolio Area End ***** -->

    <!-- ***** Call to Action Area Start ***** -->
    <div class="sonar-call-to-action-area section-padding-0-100">
      <div class="backEnd-content">
        <h2>Dream</h2>
      </div>
      <div class="container">
        <div class="row">
          <div class="col-12">
            <div class="call-to-action-content wow fadeInUp" data-wow-delay="0.5s">
              <h2>Я опытный фотограф</h2>
              <router-link class="btn sonar-btn mt-15"
                           :to="{name: 'contact', query: { scroll: true }}">
                контакты
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- ***** Call to Action Area End ***** -->

  </div>
</template>

<script>
import carousel from 'vue-owl-carousel';
import Api from '@/Api';

export default {
  data() {
    return {
      photosets: null,
      mainScreenPhotos: null
    };
  },
  components: { carousel },
  methods: {
    redirectToPhotoset(id) {
      this.$router.push({ name: 'photoset', params: { id: id } });
    }
  },
  computed: {
    isPhotosets: function () {
      return this.photosets !== null && this.photosets.length >= 4;
    },
    isHas7Photos: function () {
      return this.mainScreenPhotos && this.mainScreenPhotos.length >= 7;
    }
  },
  created() {
    this.$parent.$emit('spinner-state', 2);
    Api.getPhotosetsForMainPage()
      .then(response => {
        this.photosets = response.data.results;
      })
      .catch(() => {
        alert('ERROR');
      })
      .then(() => {
        this.$parent.$emit('spinner-state', -1);
      });
    Api.getPreferences({ section: 'main_screen_photos' })
      .then(response => {
        this.mainScreenPhotos = response.data;
      })
      .catch(() => {
        alert('ERROR');
      })
      .then(() => {
        this.$parent.$emit('spinner-state', -1);
      });
  }
};
</script>
