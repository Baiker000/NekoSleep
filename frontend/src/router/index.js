import Vue from 'vue'
import Router from 'vue-router'
// import DreamView from '@/views/DreamView'
import Login from '@/components/Login'
import CreateDream from '@/components/CreateDream'
import DreamList from '@/components/DreamList'
import Profile from '@/components/Profile'
import store from '../store'

Vue.use(Router)

const ifNotAuthenticated = (to, from, next) => {
  if (!store.state.userToken.jwt) {
    next()
    return
  }
  next('/')
}

const ifAuthenticated = (to, from, next) => {
  if (store.state.userToken.jwt) {
    next()
    return
  }
  next('/login')
}

export default new Router({
  routes: [
    {
      path: '/',
      // name: 'HelloWorld',
      name: 'Login',
      component: Login
    },
    {
      path: '/login',
      // name: 'HelloWorld',
      name: 'Login',
      component: Login,
      beforeEnter: ifNotAuthenticated
    },
    {
      path: '/create',
      name: 'CreateDream',
      component: CreateDream
    },
    {
      path: '/list',
      name: 'DreamList',
      component: DreamList,
      beforeEnter: ifAuthenticated
    },
    {
      path: '/profile',
      name: 'Profile',
      component: Profile,
      beforeEnter: ifAuthenticated
    }

  ]
})
