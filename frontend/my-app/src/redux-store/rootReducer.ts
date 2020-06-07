import { combineReducers } from 'redux'
import { connectRouter } from 'connected-react-router'
import { History } from 'history'
import features from 'features'

const rootReducer = (history: History) =>
  combineReducers({
    router: connectRouter(history),
    mainPage: features.MainPage.reducer,
    header: features.Header.reducer,
    secondPage: features.SecondPage.reducer
  })

export default rootReducer
