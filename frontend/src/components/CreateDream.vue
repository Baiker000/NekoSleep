<template lang="pug">
  form()
    .columns
      .column
        b-field(label='Title')
          b-input(
          type="text"
          v-model="title"
          placeholder="Type dream title..."
          )
    .columns
      .column
        b-field(label='Text')
          b-input(
          type="textarea"
          v-model="text"
          rows=8
          placeholder="Type your dream..."
          )
    .columns
      .column
        b-field(label='Date')
          b-datepicker(
          v-model="date"
          :first-day-of-week="1"
          placeholder="Click to select..."
          position="is-top-right"
          )
            button.button.is-primary(
            @click ="date = new Date()"
            )
              b-icon(icon="calendar-today")
              span Today
            button.button.is-danger(
            @click="date = null"
            )
              b-icon(icon="close")
              span Clear
    .columns
      .column
        .button.is-dark(type="submit" @click="submitForm")
            span.icon
              b-icon(icon="plus")
            span Create
</template>

<script>
// eslint-disable-next-line
function today () {
  // eslint-disable-next-line
  var ddd = new Date
  var date = ddd.getFullYear() + '-' + ((ddd.getMonth() + 1) < 10 ? '0' + String(ddd.getMonth() + 1) : ddd.getMonth() + 1) + '-' + (ddd.getDate() < 10 ? '0' + String(ddd.getDate()) : ddd.getDate())
  return date
}

export default {
  name: 'create-dream',
  data () {
    return {
      'title': '',
      'text': '',
      'date': new Date() // today()
    }
  },
  methods: {
    submitForm (event) {
      this.createDream()
      this.title = ''
      this.text = ''
      this.date = null // today()
      event.preventDefault()
    },
    createDream () {
      this.$store.dispatch('dreams/createDream', {title: this.title, text: this.text, dream_date: this.date})
    }
  }
}
</script>

<style scoped>

</style>
