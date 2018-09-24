import { ADD_DREAM, REMOVE_DREAM, SET_DREAM } from '../mutation-types'
import { Dream } from '../../api/dreams'

const state = {
  dreams: []
}

const getters = {
  dreams: state => state.dreams
}

const mutations = {
  [ ADD_DREAM ] (state, dream) {
    state.dreams = [dream, ...state.dreams]
  },
  [ REMOVE_DREAM ] (state, { id }) {
    state.dreams = state.dreams.filter(dream => { return dream.id !== id })
  },
  [ SET_DREAM ] (state, { dreams }) {
    state.dreams = dreams
  }
}

const actions = {
  createDream ({commit}, dreamData) {
    Dream.create(dreamData).then(dream => {
      commit(ADD_DREAM, dream)
    })
  },
  deleteDream ({commit}, dream) {
    Dream.delete(dream).then(response => {
      commit(REMOVE_DREAM, dream)
    })
  },
  getDreams ({commit}) {
    Dream.list().then(dreams => {
      commit(SET_DREAM, { dreams })
    })
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
