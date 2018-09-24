import {TOKEN} from './common'

export const Token = {
  obtain (username, password) {
    return TOKEN.post('auth/obtain_token', username, password).then(response => {
      return response.data.token
    })
  },
  refresh () {
    return TOKEN.post('auth/refresh_token').then(response => { return response.data })
  }
}
