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

    <slot/>

    <footer-bar/>
  </div>
</template>
