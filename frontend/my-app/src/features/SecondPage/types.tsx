export type stateType = {
  data: any
}

export type mapStatePropsType = {
  data: {
    build: string | null
    ['build_type']: string | null
    country: string | null
    housing: string | null
    index: string | null
    region: string | null
    ['region_type']: string | null
    room: string | null
    ['room_type']: string | null
    route: string | null
    ['route_type']: string | null
    subbuild: string | null
    subregion: string | null
    ['subregion_type']: string | null
    town: string | null
    ['town_type']: string | null
  }
}

export type propsTypes = mapStatePropsType

export type dataType = {
  build: string | null
  ['build_type']: string | null
  country: string | null
  housing: string | null
  index: string | null
  region: string | null
  ['region_type']: string | null
  room: string | null
  ['room_type']: string | null
  route: string | null
  ['route_type']: string | null
  subbuild: string | null
  subregion: string | null
  ['subregion']: string | null
  town: string | null
  ['town_type']: string | null
}
