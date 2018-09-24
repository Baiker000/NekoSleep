import { HTTP } from './common'

export const User = {
  get () {
    return HTTP.get('/get_user_info/').then(response => { return response.data })
  }
}
