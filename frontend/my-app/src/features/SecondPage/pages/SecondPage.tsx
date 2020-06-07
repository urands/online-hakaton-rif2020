import React, { FC, useState, useEffect, useCallback } from 'react'
import { connect } from 'react-redux'
import styles from './SecondPage.module.sass'
import { dataSelector } from '../selectors'
import { RootState } from '../../../redux-store/types'
import { mapStatePropsType, propsTypes } from '../types'
import { Spin } from 'antd'
import { LoadingOutlined } from '@ant-design/icons'
import { Maps } from '../components'

const SecondPage: FC<propsTypes> = ({ data }) => {
  const [isLoading, setLoading] = useState(false)
  const [isData, setData] = useState(data)
  const [burger, setBurger] = useState(true)
  const [address, setAddres] = useState<string>('')

  useEffect(() => {
    if (data) {
      setLoading(true)
      setData(data)
    }
  }, [setData, isData, data])

  const pullAdrees = useCallback(() => {
    if (isData) {
      const str = `${isData.index} ${isData.country} ${isData.region} ${isData.region_type} ${isData.subregion} ${isData.subregion_type} ${isData.town_type} ${isData.town} ${isData.route_type} ${isData.route} ${isData.build_type} ${isData.build} ${isData.housing} ${isData.subbuild} ${isData.room_type} ${isData.room}`
        .replace(/\s+/g, ' ')
        .trim()
      setAddres(str as string)
    }
  }, [isData])

  useEffect(() => {
    pullAdrees()
  }, [pullAdrees])

  const region = (): any => {
    if (isData) {
      if (isData.region_type === 'РЕСПУБЛИКА') {
        return (
          <>
            {isData.region_type} &nbsp;{isData.region}
          </>
        )
      } else {
        return (
          <>
            {isData.region} &nbsp;{isData.region_type}
          </>
        )
      }
    }
  }

  const antIcon = <LoadingOutlined style={{ fontSize: 48, color: 'green' }} spin />

  return !isLoading ? (
    <div className={styles.spinner}>
      <Spin indicator={antIcon} />
    </div>
  ) : (
    <div className={styles.wrapper}>
      {console.log(isData)}
      <div className={styles.pageBlock}>
        <div className={styles.addressBlock}>
          <div className={styles.addressHeader}>
            <button className={styles.addressMenu} onClick={() => setBurger(!burger)} />
          </div>
          {burger && (
            <div className={styles.dropdown}>
              <p className={styles.adressLabel}>Страна</p>
              <div className={styles.addressOutput}>{isData.country}</div>
              <p className={styles.adressLabel}>Регион</p>
              <div className={styles.addressOutput}>{region()}</div>
              <p className={styles.adressLabel}>{isData.town_type || 'Город'}/район</p>
              <div className={styles.addressOutput}>
                {isData.town && `${isData.town}`}
                {isData.subregion && `, ${isData.subregion}`}
                {isData.subregion_type && ` ${isData.subregion_type}`}
              </div>
              <p className={styles.adressLabel}>{isData.route_type || 'Улица'}</p>
              <div className={styles.addressOutput}>{isData.route}</div>
              <p className={styles.adressLabel}>Дом/корпус/строение</p>
              <div className={styles.addressOutput}>
                {isData.build}
                {isData.housing && `, ${isData.housing}`}
                {isData.subbuild && `, ${isData.subbuild}`}
              </div>
              <p className={styles.adressLabel}>{isData.room_type || 'Квартира'}</p>
              <div className={styles.addressOutput}>{isData.room}</div>
              <label className={styles.mapView}>
                Вид карты:
                <select className={styles.mapSelect}>
                  <option className={styles.mapOption}>Карта</option>
                  <option className={styles.mapOption}>Спутник</option>
                  <option className={styles.mapOption}>Гибрид</option>
                </select>
              </label>
            </div>
          )}
        </div>
        <div className={styles.map}>
          <Maps />
        </div>
        <div className={styles.info}>
          <span className={styles.address}>Адрес:</span>
          <input type='text' readOnly value={address as string} className={styles.result} />
        </div>
      </div>
    </div>
  )
}

const mapStateToProps = (state: RootState): mapStatePropsType => {
  return {
    data: dataSelector(state)
  }
}

export default connect(mapStateToProps)(SecondPage)
