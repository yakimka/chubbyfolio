<template>
  <div id="app">
    <component :is="layout">
      <router-view/>
    </component>
  </div>
</template>

<script>
const DEFAULT_LAYOUT = 'landing';

export default {
  computed: {
    layout() {
      return (this.$route.meta.layout || DEFAULT_LAYOUT) + '-layout';
    }
  }
};
</script>

<style>

</style>
