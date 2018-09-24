import Vue from 'vue'
import Vuex from 'vuex'
import dreams from './modules/dreams'
import userToken from './modules/userToken'
import user from './modules/user'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    dreams,
    userToken,
    user
  }
})
