<script>
import NavBar from '@/components/NavBar';
import FooterBar from '@/components/FooterBar';

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
    this.$on('spinner-state', function (state) {
      this.loading = state;
    });
  }
};
</script>

<template>
  <div>
    <top-page :loading="loading"></top-page>

    <nav-bar/>

    <div class="container">
      <slot/>
    </div>

    <footer-bar/>
  </div>
</template>
