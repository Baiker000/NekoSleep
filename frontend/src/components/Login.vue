<template lang="pug">
#login
  form()
    .columns
      .column
        h2 Log In
    .columns
      .column
        b-field(label='Username')
           b-input(
           type="text"
           placeholder="Enter your username"
           v-model="username"
           )
    .columns
      .column
        b-field(label='Password')
           b-input(
           type="password"
           placeholder="Enter your password"
           password-reveal=''
           v-model="password"
           )
    .columns
      .column
        .button.is-dark(type="submit" @click="loginSubmit")
           span.icon
               i.fas.fa-sign-in-alt
           span Login
</template>

<script>
export default {
  name: 'Login',
  data () {
    return {
      'username': this.username,
      'password': ''
    }
  },
  methods: {
    loginSubmit () {
      this.$store.dispatch('userToken/obtainToken', {username: this.username, password: this.password})
      console.log(this.error)
      this.$router.push('/')
    }
  }

}
</script>

<style scoped>

</style>
