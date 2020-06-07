import React, { FC, ReactNode } from 'react'
import { Header } from 'features/Header/pages'
import { Footer } from 'features/Footer/pages'

import styles from './MainLayout.module.sass'

type propsTypes = {
  children: ReactNode
}

const MainLayout: FC<propsTypes> = ({ children }) => {
  return (
    <div className={styles.wrapper}>
      <Header />
      <div className={styles.children}>{children}</div>
      <Footer />
    </div>
  )
}

export default MainLayout
