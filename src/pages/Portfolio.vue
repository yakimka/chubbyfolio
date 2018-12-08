<template>
  <div>
    <!-- ****** Gallery Area Start ****** -->
    <section class="sonar-projects-area" id="projects">
      <div class="container-fluid">
        <div class="row sonar-portfolio">

          <!-- Single gallery Item -->
          <div
            class="col-12 col-sm-6 col-lg-3 single_gallery_item landscapes studio wow fadeInUpBig"
            data-wow-delay="300ms"
            v-for="photoset in photosets" :key="photoset.id">
            <router-link class="gallery-img"
                         :to="{name: 'photoset', params: {id: photoset.id}}">
              <img :src="photoset.cover" :alt="photoset.name">
            </router-link>
            <!-- Gallery Content -->
            <div class="gallery-content">
              <h4>{{ photoset.name }}</h4>
              <!--<p>category or description</p>-->
            </div>
          </div>
        </div>

        <div class="row" v-if="isNextPage">
          <div class="col-12 text-center">
            <span class="btn sonar-btn" @click="retrieveNextPage()">Load More</span>
          </div>
        </div>
      </div>
    </section>
    <!-- ****** Gallery Area End ****** -->
  </div>
</template>

<script>
import Api from '@/Api';
import axios from 'axios';

export default {
  data() {
    return {
      portfolio: null,
      photosets: null,
      loading: true
    };
  },
  methods: {
    retrieveNextPage() {
      this.loading = true;
      axios.get(this.portfolio.next)
        .then(response => {
          this.portfolio = response.data;
          this.photosets = [...this.photosets, ...response.data.results];
          this.$delete(this.portfolio, 'results');
          this.loading = false;
        })
        .catch(() => {
          alert('ERROR');
          this.loading = false;
        });
    }
  },
  computed: {
    isNextPage: function () {
      return this.portfolio !== null && this.portfolio.next !== null;
    }
  },
  created() {
    Api.getPhotosets()
      .then(response => {
        this.portfolio = response.data;
        this.photosets = JSON.parse(JSON.stringify(response.data.results));
        this.$delete(this.portfolio, 'results');
        this.loading = false;
      })
      .catch(() => {
        alert('ERROR');
        this.loading = false;
      });
  }
};
</script>

<style scoped>

</style>
