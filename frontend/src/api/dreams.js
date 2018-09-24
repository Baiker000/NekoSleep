import { HTTP } from './common'

export const Dream = {
  create (config) {
    return HTTP.post('/dreams/', config).then(response => { return response.data })
  },
  delete (dream) {
    return HTTP.delete(`/dreams/${dream.id}/`)
  },
  list () {
    return HTTP.get('/dreams/').then(response => { return response.data })
  }
}
