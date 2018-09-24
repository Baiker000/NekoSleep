<template lang="pug">
  #app
    .columns(v-for="dream in dreams")
      .column
        .card
          .card-header
            button.btn.btn-clear.float-right(@click="deleteDream(dream)")
            .card-header-title {{ dream.title }}
            p {{ dream.dream_date }}
            p {{ dream.author }}
          .card-content {{ dream.text }}
          .card-footer(v-bind:class="hasTags")
            b-taglist
              b-tag.is-primary(v-for="tag in dream.tags" :key='tag.name') {{ tag.name }}
</template>

<script>
import {mapGetters} from 'vuex'

export default {
  name: 'dream-list',
  computed: mapGetters('dreams', ['dreams']),
  methods: {
    deleteDream (dream) {
      this.$store.dispatch('dreams/deleteDream', dream)
    }
  },
  beforeMount () {
    this.$store.dispatch('dreams/getDreams')
  }
}
</script>

<style scoped>
  header {
    margin-top: 50px;
  }
  .card-body {
    white-space: pre-wrap;
  }

  .card-footer {
    padding-top: 15px;
    padding-right: 15px;
    padding-bottom: 15px;
    padding-left: 15px;
  }
</style>
