import { createSelector } from 'reselect'
import { RootState } from '../../redux-store/types'

const dataStateSelector = (state: RootState) => state.secondPage

export const dataSelector = createSelector(dataStateSelector, (state) => state.data)
