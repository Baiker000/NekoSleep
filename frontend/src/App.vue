<template lang="pug">
  #app
    nav.navbar.is-dark
        .navbar-brand
          .a.nav-item
            | NekoSleep
          .a.navbar-burger(data-target='navbar_menu' v-on:click='mobileMenu' v-bind:class='{"is-active": isActive}').is-hidden-desktop
            span
            span
            span
        .navbar-menu(id="navbar_menu" v-bind:class='{"is-active": isActive}')
          .navbar-start
            router-link(to='/create')
              a.navbar-item.is-tab.is-hidden-desktop
                | Create
            router-link(to='/list')
              a.navbar-item.is-tab.is-hidden-desktop
                | List
            router-link(to='/profile')
              a.navbar-item.is-tab.is-hidden-desktop
                | Profile(Login)
          .navbar-end
            template(v-if='isLogin')
              a.navbar-item.is-tab.is-active
                span.icon
                  i.fa.fa-user
              a.navbar-item.is-tab.is-active
                span.icon
                  i.fa.fa-sign-out-alt(v-on:click='logout')
    .section.main_content
      .columns
        aside.column.is-2.is-narrow-mobile.is-fullheight.hero.is-hidden-touch.has-background-dark
          .hero-head
            p.menu-label.has-text-white Navigation
            ul.menu-list
              li
                a
                  router-link(to='/create').has-text-white Create
              li
                a
                  router-link(to='/list').has-text-white List
              li
                a
                  router-link(to='/profile').has-text-white Profile(Login)
        .column
          .column
            .section
              router-view

    <!--router-link(to='/dreams') TO DREAMS-->
    <!--p-->
    <!--router-link(to='/login') TO LOGIN-->
    <!--p-->
    <!--button.btn.btn-primary(v-on:click='logout') logout-->
    <!--router-view-->
</template>

<script>
import {mapState} from 'vuex'

export default {
  name: 'App',
  computed: mapState({
    isLogin: state => state.userToken.jwt
  }),
  data () {
    return {
      isActive: false
      // isLogin: false
    }
  },
  components: {
  },
  methods: {
    logout () {
      this.$store.dispatch('userToken/logoutToken')
      // this.isLogin = false
      this.$router.push('/')
    },
    mobileMenu () {
      if (!this.isActive) {
        this.isActive = true
      } else {
        this.isActive = false
      }
    }
  },
  beforeCreate () {
    this.$store.dispatch('userToken/inspectToken')
    console.log(this.isLogin)
  }
}
</script>

<style lang="scss">
// Start main part
@import "~bulma/sass/utilities/_all";
// Customize variable
$navbar-height: 2.5rem;
//$navbar-item-color: hsl(0, 0%, 100%);
//$navbar-burger-color: hsl(0, 0%, 100%);
//Customize variable end
@import "~bulma";
@import "~buefy/src/scss/buefy";
//End main part
//

html, body, #app {
  height: 100%;
}
#app {
  min-height: 100%;
  //display: flex;
  //flex-direction: column;
}

/*.aside {*/
  /*position: -webkit-sticky;*/
  /*position: sticky;*/
  /*top: 0;*/
  /*flex: none;*/
  /*height: 100%;*/
/*}*/

/*.main_content {*/
  /*padding: 0px;*/
/*}*/

@media screen and (min-width: 1088px) {
  .main_content {
  padding: 0px;
  }
}

/*<!--.footer {-->*/
  /*<!--margin-top: -12px;-->*/
/*<!--}-->*/
/*@media screen and (max-width: 768px) {*/
  /*#menu-toggle:checked + .navbar-menu {*/
    /*display: none;*/
  /*}*/
/*}*/
/*#app {*/
  /*font-family: 'Avenir', Helvetica, Arial, sans-serif;*/
  /*-webkit-font-smoothing: antialiased;*/
  /*-moz-osx-font-smoothing: grayscale;*/
  /*text-align: center;*/
  /*color: #2c3e50;*/
  /*margin-top: 60px;*/
/*}*/
</style>
