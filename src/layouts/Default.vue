<script>
import NavBar from '@/components/NavBar';
import SideBar from '@/components/SideBar';
import FooterBar from '@/components/FooterBar';
import {setLoadingState} from '@/helpers';

export default {
  components: {
    NavBar,
    SideBar,
    FooterBar
  },
  data() {
    return {
      loading: true
    };
  },
  created() {
    this.$on('spinner-state', function (state) {
      setLoadingState(this, state);
    });
  }
};
</script>

<template>
  <div>
    <top-page :loading="loading"></top-page>

    <nav-bar/>

    <div class="container section">
      <div class="columns">
        <div class="column is-8">
          <slot/>
        </div>

        <div class="column is-4">
          <side-bar/>
        </div>
      </div>
    </div>

    <footer-bar/>
  </div>
</template>
