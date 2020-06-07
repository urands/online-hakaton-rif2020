import React, { FC } from 'react'

import styles from './Footer.module.sass'

const Footer: FC = () => {
  return (
    <div className={styles.footer}>
      <p className={styles.copyright}>Все права защищены</p>
      <p className={styles.copyright}>Copyright &#169; Dragon IT 2020</p>
    </div>
  )
}

export default Footer
