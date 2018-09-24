// eslint-disable-next-line
import jwt_decode from 'jwt-decode'
import { Token } from '../../api/tokens'
import axios from 'axios'
import { UPDATE_TOKEN, REMOVE_TOKEN } from '../mutation-types'

const state = {
  jwt: localStorage.getItem('t') || ''
}

const getters = {
  isAuthenticated: state => !!state.jwt
}

const mutations = {
  [ UPDATE_TOKEN ] (state, newToken) {
    console.log('HELLO')
    localStorage.setItem('t', newToken)
    state.jwt = newToken
  },
  [ REMOVE_TOKEN ] (state) {
    localStorage.removeItem('t')
    state.jwt = null
    axios.defaults.headers.common['Authorization'] = ''
  }
}

const actions = {
  obtainToken ({commit}, username, password) {
    Token.obtain(username, password).then(token => {
      commit(UPDATE_TOKEN, token)
      axios.defaults.headers.common['Authorization'] = 'JWT' + ' ' + token
      console.log(token)
    }).catch(error => {
      console.log(error)
    })
  },
  refreshToken ({commit}) {
    const payload = {
      token: state.jwt
    }
    Token.refresh(payload).then(token => {
      commit(UPDATE_TOKEN, token)
    }).catch((error) => {
      console.log(error)
    })
  },
  inspectToken () {
    const token = state.jwt
    if (token) {
      axios.defaults.headers.common['Authorization'] = 'JWT' + ' ' + token
      const decoded = jwt_decode(token)
      const exp = decoded.exp
      const iat = decoded.iat
      if (exp - (Date.now() / 1000) < 86400 && (Date.now() / 1000) - iat < 31451400) {
        this.dispatch('refreshToken')
      } else if (exp - (Date.now() / 1000) < 86400) {
        this.dispatch('logoutToken')
      } else {
        this.dispatch('logoutToken')
      }
    }
  },
  logoutToken ({commit}) {
    commit(REMOVE_TOKEN)
  }
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}
