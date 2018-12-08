<template>
  <div id="exboo">
    <!-- ****** Gallery Area Start ****** -->
    <section class="sonar-projects-area" id="projects">
      <div class="container-fluid">
        <div class="row sonar-portfolio">

          <!-- Single gallery Item -->
          <div
            class="col-12 col-sm-6 col-lg-3 single_gallery_item landscapes studio wow fadeInUpBig"
            data-wow-delay="300ms"
            v-for="photo in photos" :key="photo.id">
            <a class="gallery-img" :href="photo.image">
              <img :src="photo.thumbnail" :alt="photo.name">
            </a>
            <!-- Gallery Content -->
            <div class="gallery-content">
              <h4>{{ photo.name }}</h4>
              <p>{{ photo.description }}</p>
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
      photoset: null,
      photos: null,
      loading: true
    };
  },
  methods: {
    retrieveNextPage() {
      this.loading = true;
      axios.get(this.photoset.next)
        .then(response => {
          this.photoset = response.data;
          this.photos = [...this.photos, ...response.data.results];
          this.$delete(this.photoset, 'results');
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
      return this.photoset !== null && this.photoset.next !== null;
    }
  },
  created() {
    Api.getPhotos(this.$route.params.id)
      .then(response => {
        this.photoset = response.data;
        this.photos = JSON.parse(JSON.stringify(response.data.results));
        this.$delete(this.photoset, 'results');
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
