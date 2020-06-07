import { createBrowserHistory } from 'history'
import { applyMiddleware, createStore } from 'redux'
import thunkMiddlewere from 'redux-thunk'
import { composeWithDevTools } from 'redux-devtools-extension'
import { routerMiddleware } from 'connected-react-router'
import rootReducer from './rootReducer'

export const history = createBrowserHistory()

const configureStore = (preloadedState?: any) => {
  const middlewares = [thunkMiddlewere, routerMiddleware(history)]
  const middlewareEnchancer = applyMiddleware(...middlewares)

  const enchancers = [middlewareEnchancer]
  const composedEnchancers = composeWithDevTools(...enchancers)

  const store = createStore(rootReducer(history), composedEnchancers)

  if (process.env.NODE_ENV !== 'production' && module.hot) {
    module.hot.accept('./rootReducer.ts', () => store.replaceReducer(rootReducer(history)))
  }

  return store
}

export default configureStore
