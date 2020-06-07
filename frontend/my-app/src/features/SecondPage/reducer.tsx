import { handleActions } from 'redux-actions'
import { SEARCHTEXT } from '../MainPage/actionTypes'
import { produce } from 'immer'
import { stateType } from './types'

const initState: stateType = { data: null }

export default handleActions(
  {
    [SEARCHTEXT]: (state, action) =>
      produce(state, (draft) => {
        const { payload } = action
        draft.data = payload
      })
  },
  initState
)
