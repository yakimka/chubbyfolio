<template>
  <!-- ***** Header Area Start ***** -->
  <div class="header-area" :class="{sticky: isScrollOnTop}">
    <div class="container-fluid">
      <div class="row">
        <div class="col-12">
          <div class="menu-area d-flex justify-content-between">
            <!-- Logo Area  -->
            <div class="logo-area">
              <b-nav>
                <b-nav-item :to="{name: 'home'}">
                  Home
                </b-nav-item>
                <b-nav-item :to="{name: 'about'}">
                  About
                </b-nav-item>
              </b-nav>
            </div>

            <div class="menu-content-area d-flex align-items-center">
              <!-- Header Social Area -->
              <div class="header-social-area d-flex align-items-center">
                <a href="#" data-toggle="tooltip" data-placement="bottom" title="Instagram">
                  <font-awesome-icon :icon="['fab', 'instagram']"/>
                </a>
                <a href="#" data-toggle="tooltip" data-placement="bottom" title="Facebook">
                  <font-awesome-icon :icon="['fab', 'facebook']"/>
                </a>
              </div>
              <!-- Menu Icon -->
              <span class="navbar-toggler-icon" id="menuIcon"></span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- ***** Header Area End ***** -->
</template>

<script>
export default {
  data() {
    return {
      scrollPosition: null
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
    }
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
