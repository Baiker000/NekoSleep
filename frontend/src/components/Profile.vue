<template lang="pug">
  #profile
    .hero.is-primary
      .container
        .columns
          .column
            figure.image.is-128x128.avatar
              img.is-rounded(:src=" user.avatar ")
          .column
            h2 {{ user.username }}

</template>

<script>
import {mapGetters} from 'vuex'

export default {
  name: 'Profile',
  computed: mapGetters('user', ['user']),
  beforeMount () {
    this.$store.dispatch('user/get_user')
  }
}
</script>

<style scoped>

  .avatar {
    transform: translateY(50%);
  }

</style>
