<template>
  <div>
    <button
      class="btn btn-primary btn-margin"
      @click="check()">
      Check
    </button>
  </div>
</template>

<script>
import axios from 'axios';

const API_URL = 'http://localhost:8000';

export default {
  name: 'app',
  data () {
    return {
      authenticated: false,
      message: ''
    };
  },
  methods: {
    check () {
      const url = `${API_URL}/api/photosets/`;
      return axios.get(url)
        .then((response) => {
          console.log(response.data);
        });
    }
  }
};
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
</style>
