import { SEARCHTEXT } from '../actionTypes'
import { Dispatch } from 'redux'
import axios from 'axios'

const handleSearch = (text: string) => async (dispatch: Dispatch) => {
  dispatch({
    type: SEARCHTEXT
  })

  const form = new FormData()
  form.set('address', text)

  const { data } = await axios.post('http://127.0.0.1/api/norm', form, {
    headers: { 'Content-Type': 'multipart/form-data' }
  })

  dispatch({
    type: SEARCHTEXT,
    payload: data
  })
}

export default handleSearch
