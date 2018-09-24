<template lang="pug">
  #dreams
    section.container.grid-960
      .columns
        .column.col-2
        .column.col-8.col-md-12
          header.text-center
            h2 Create dream
          create-dream
          header.text-center
            h2 List of dreams
          dream-list
        .column.col-2
</template>

<script>
import CreateDream from '../components/CreateDream'
import DreamList from '../components/DreamList'

export default {
  name: 'DreamView',
  components: {
    'create-dream': CreateDream,
    'dream-list': DreamList
  },
  created () {
    if (!this.$store.state.userToken.jwt) {
      this.$router.push('Login')
    }
  }
}
</script>

<style scoped>
#dreams {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
