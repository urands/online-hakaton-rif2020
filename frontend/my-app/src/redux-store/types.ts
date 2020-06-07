import createRootReducer from './rootReducer'
import { StateType } from 'typesafe-actions'

export type RootState = StateType<ReturnType<typeof createRootReducer>>
