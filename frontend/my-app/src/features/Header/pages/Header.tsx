import React, { FC } from 'react'
import { useHistory } from 'react-router-dom'
import logo from 'assets/img/logo.png'

import styles from './Header.module.sass'

const Header: FC = () => {
  const history = useHistory()

  return (
    <header className={styles.header}>
      <div className={styles.container}>
        <div className={styles.logoBlock} onClick={() => history.push('/')}>
          <img src={logo} alt='Нормализатор' className={styles.logo} />
          <p className={styles.title}>Нормализатор Dragon IT</p>
        </div>
        <div className={styles.helpBlock}>
          <div className={styles.button}>Помощь</div>
          <div className={styles.button}>Связаться с нами</div>
        </div>
      </div>
    </header>
  )
}

export default Header
