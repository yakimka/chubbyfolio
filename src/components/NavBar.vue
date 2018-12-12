<template>
  <div :class="{'menu-open': menuOpen}">
    <!-- ***** Header Area Start ***** -->
    <div class="header-area" :class="{sticky: isScrollOnTop}">
      <div class="container-fluid">
        <div class="row">
          <div class="col-12">
            <div class="menu-area d-flex justify-content-between">
              <!-- Logo Area  -->
              <div class="logo-area">
                <b-nav>
                  <b-nav-item :to="{name: 'home'}">Главная</b-nav-item>
                </b-nav>
              </div>

              <div class="menu-content-area d-flex align-items-center">
                <!-- Header Social Area -->
                <div class="header-social-area d-flex align-items-center" v-if="social">
                  <a :href="social.instagram_link" target="_blank" data-toggle="tooltip"
                     data-placement="bottom" title="Instagram" v-if="social.instagram_link">
                    <font-awesome-icon :icon="['fab', 'instagram']"/>
                  </a>
                  <a :href="social.facebook_link" target="_blank" data-toggle="tooltip"
                     data-placement="bottom" title="Facebook" v-if="social.facebook_link">
                    <font-awesome-icon :icon="['fab', 'facebook']"/>
                  </a>
                </div>
                <!-- Menu Icon -->
                <span class="navbar-toggler-icon" id="menuIcon" title="Открыть главное меню"
                      @click="menuOpen = !menuOpen"></span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- ***** Header Area End ***** -->

    <!-- ***** Main Menu Area Start ***** -->
    <transition
      name="custom-classes-transition"
      enter-active-class="animated bounceInRight"
      leave-active-class="animated bounceOutRight">
      <div class="mainMenu d-flex align-items-center justify-content-between" v-if="menuOpen">
        <!-- Close Icon -->
        <div class="closeIcon" @click="menuOpen = !menuOpen">
          <font-awesome-icon class="ti-close" :icon="['fas', 'times-circle']"/>
        </div>
        <!-- Logo Area -->
        <div class="logo-area">
          <!--<a href="index.html">Sonar</a>-->
        </div>
        <!-- Nav -->
        <div class="sonarNav">
          <nav>
            <ul>
              <b-nav-item :to="{name: 'home'}">Главная</b-nav-item>
              <b-nav-item :to="{name: 'portfolio'}">Портфолио</b-nav-item>
              <b-nav-item to="#" v-scroll-to="'#contact-me'" v-if="isContactPage">Контакты
              </b-nav-item>
              <b-nav-item :to="{name: 'contact', query: { scroll: true }}" v-else>Контакты
              </b-nav-item>
              <b-nav-item :to="{name: 'about'}">Обо мне</b-nav-item>
            </ul>
          </nav>
        </div>
        <!-- Copwrite Text -->
        <div class="copywrite-text">
          <p>
            <!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
            Site created by <a
            href="https://t.me/yakimka" target="_blank">yakimka</a> | Based on template made by
            <a href="https://colorlib.com" target="_blank">Colorlib</a> | Copyright &copy;{{ new
            Date().getFullYear() }} | All rights reserved
            <!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
          </p>
        </div>
      </div>
    </transition>
    <!-- ***** Main Menu Area End ***** -->
  </div>
</template>

<script>
import Api from '@/Api';

export default {
  data() {
    return {
      scrollPosition: null,
      social: null,
      menuOpen: false
    };
  },
  methods: {
    updateScroll() {
      this.scrollPosition = window.scrollY;
    }
  },
  computed: {
    isScrollOnTop: function () {
      return this.scrollPosition !== null && this.scrollPosition > 10;
    },
    isContactPage: function () {
      return this.$route.name === 'contact';
    }
  },
  created() {
    Api.getPreferences({section: 'social'})
      .then(response => {
        this.social = response.data;
      });
  },
  mounted() {
    window.addEventListener('scroll', this.updateScroll);
  },
  destroy() {
    window.removeEventListener('scroll', this.updateScroll);
  }
};
</script>

<style lang="scss">
</style>
