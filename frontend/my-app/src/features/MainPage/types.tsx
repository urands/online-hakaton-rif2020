export type searchType = string

export type stateType = {
  search: searchType
}

export type mapStatePropsType = {
  search?: searchType
}

export type mapDispatchPropsType = {
  handleSearch: (text: string) => void
}

export type propsTypes = mapDispatchPropsType
