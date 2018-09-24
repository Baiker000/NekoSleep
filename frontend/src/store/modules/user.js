import { User } from '../../api/user'
import { SET_USER } from '../mutation-types'

const state = {
  user: []
}

const getters = {
  user: state => state.user[0]
}

const mutations = {
  [ SET_USER ] (state, { user }) {
    state.user = user
  }
}

const actions = {
  get_user ({commit}) {
    User.get().then(user => {
      commit(SET_USER, { user })
    })
  }
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}
