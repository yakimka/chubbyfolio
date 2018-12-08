<template>
  <div>
    <div class="hero-area">
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
              <h2>“In photography there is a reality so subtle that it becomes more
                <span>real</span> than reality.”</h2>
            </div>
          </div>
        </div>

        <div class="row justify-content-between">
          <!-- Single Portfoio Area -->
          <div class="col-12 col-md-5">
            <div class="single-portfolio-item mt-100 portfolio-item-1 wow fadeIn">
              <div class="backend-content">
                <img class="dots" src="/static/img/core-img/dots.png" alt="">
                <h2>Reality</h2>
              </div>
              <div class="portfolio-thumb">
                <img src="/static/img/bg-img/p1.png" alt="">
              </div>
              <div class="portfolio-meta">
                <p class="portfolio-date">Feb 02, 2018</p>
                <h2>Italy in the sunset</h2>
              </div>
            </div>
          </div>
          <!-- Single Portfoio Area -->
          <div class="col-12 col-md-6">
            <div class="single-portfolio-item mt-230 portfolio-item-2 wow fadeIn">
              <div class="backend-content">
                <img class="dots" src="/static/img/core-img/dots.png" alt="">
              </div>
              <div class="portfolio-thumb">
                <img src="/static/img/bg-img/p2.png" alt="">
              </div>
              <div class="portfolio-meta">
                <p class="portfolio-date">Feb 02, 2018</p>
                <h2>Mountain Landscape</h2>
              </div>
            </div>
          </div>
        </div>

        <div class="row">
          <!-- Single Portfoio Area -->
          <div class="col-12 col-md-10">
            <div class="single-portfolio-item mt-100 portfolio-item-3 wow fadeIn">
              <div class="backend-content">
                <img class="dots" src="/static/img/core-img/dots.png" alt="">
                <h2>Photography</h2>
              </div>
              <div class="portfolio-thumb">
                <img src="/static/img/bg-img/p3.png" alt="">
              </div>
              <div class="portfolio-meta">
                <p class="portfolio-date">Feb 02, 2018</p>
                <h2>Foggy sunset over the lake</h2>
              </div>
            </div>
          </div>
        </div>

        <div class="row justify-content-end">
          <!-- Single Portfoio Area -->
          <div class="col-12 col-md-6">
            <div class="single-portfolio-item portfolio-item-4 wow fadeIn">
              <div class="backend-content">
                <img class="dots" src="/static/img/core-img/dots.png" alt="">
              </div>
              <div class="portfolio-thumb">
                <img src="/static/img/bg-img/p2.png" alt="">
              </div>
              <div class="portfolio-meta">
                <p class="portfolio-date">Feb 02, 2018</p>
                <h2>Clouds on mountain top</h2>
              </div>
            </div>
          </div>
        </div>

        <div class="row">
          <!-- Single Portfoio Area -->
          <div class="col-12 col-md-5">
            <div class="single-portfolio-item portfolio-item-5 wow fadeIn">
              <div class="backend-content">
                <img class="dots" src="/static/img/core-img/dots.png" alt="">
                <h2>Hope</h2>
              </div>
              <div class="portfolio-thumb">
                <img src="/static/img/bg-img/p5.png" alt="">
              </div>
              <div class="portfolio-meta">
                <p class="portfolio-date">Feb 02, 2018</p>
                <h2>Over the canion</h2>
              </div>
            </div>
          </div>
        </div>

        <div class="row justify-content-center">
          <!-- Single Portfoio Area -->
          <div class="col-12 col-md-4">
            <div class="single-portfolio-item portfolio-item-6 wow fadeIn">
              <div class="portfolio-thumb">
                <img src="/static/img/bg-img/p6.png" alt="">
              </div>
              <div class="portfolio-meta">
                <p class="portfolio-date">Feb 02, 2018</p>
                <h2>Mirror lake</h2>
              </div>
            </div>
          </div>
        </div>

        <div class="row justify-content-end">
          <!-- Single Portfoio Area -->
          <div class="col-12 col-md-4">
            <div class="single-portfolio-item portfolio-item-7 wow fadeIn">
              <div class="backend-content">
                <img class="dots" src="/static/img/core-img/dots.png" alt="">
                <h2>Future</h2>
              </div>
              <div class="portfolio-thumb">
                <img src="/static/img/bg-img/p7.png" alt="">
              </div>
              <div class="portfolio-meta">
                <p class="portfolio-date">Feb 02, 2018</p>
                <h2>Mirror lake</h2>
              </div>
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
              <h2>I am an experienced photographer</h2>
              <h5>Let’s talk</h5>
              <a href="#" class="btn sonar-btn mt-100">contact me</a>
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
      photosets: null
    };
  },
  components: {carousel},
  methods: {
    redirectToPhotoset(id) {
      this.$router.push({name: 'photoset', params: {id: id}});
    }
  },
  computed: {
    isPhotosets: function () {
      return this.photosets !== null && this.photosets.length >= 4;
    }
  },
  created() {
    this.$parent.$emit('spinner-state', true);
    Api.getPhotosetsForMainPage()
      .then(response => {
        this.photosets = response.data.results;
      })
      .catch(() => {
        alert('ERROR');
      })
      .then(() => {
        this.$parent.$emit('spinner-state', false);
      });
  }
};
</script>
