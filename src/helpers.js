export function setLoadingState(that, state) {
  if (Number.isInteger(state) && state < 0) {
    that.loading += state;
  } else {
    that.loading = state;
  }
}
