import React, { FC } from 'react'
import { Switch, Route } from 'react-router-dom'
import features from 'features'
import MainLayout from 'components/MainLayout'

export const Router: FC = () => {
  return (
    <MainLayout>
      <Switch>
        <Route path='/' exact component={features.MainPage.pages.MainPage} />
        <Route path='/secondPage' component={features.SecondPage.pages.SecondPage} />
      </Switch>
    </MainLayout>
  )
}
