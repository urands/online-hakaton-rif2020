import React, { FC, useState } from 'react'
import { connect } from 'react-redux'
import { handleSearch } from '../actions'
import styles from './MainPage.module.sass'
import { RootState } from '../../../redux-store/types'
import { mapDispatchPropsType, propsTypes } from '../types'
import { useHistory } from 'react-router-dom'

const MainPage: FC<propsTypes> = ({ handleSearch }) => {
  const [search, setSearch] = useState('')
  const history = useHistory()

  return (
    <div className={styles.mainPage}>
      <div className={styles.container}>
        <div className={styles.box}>
          <input
            type='text'
            name='address'
            placeholder='Введите адрес для обработки'
            className={styles.search}
            onChange={(e: React.FormEvent<HTMLInputElement>) => {
              const text = e.currentTarget.value
              setSearch(text)
            }}
            value={search}
          />
          <button
            className={styles.button}
            onClick={() => {
              handleSearch(search)
              history.push('/secondPage')
            }}
          >
            Поиск
          </button>
        </div>
      </div>
    </div>
  )
}

const mapStateToProps = (state: RootState) => {
  return {}
}

const mapDispatchToProps: mapDispatchPropsType = {
  handleSearch
}

export default connect(mapStateToProps, mapDispatchToProps)(MainPage)
