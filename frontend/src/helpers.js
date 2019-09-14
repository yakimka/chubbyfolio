import Api from '@/Api';

export function onLayoutCreate(that) {
  that.$on('spinner-state', function (state) {
    setLoadingState(that, state);
  });
}

function setLoadingState(that, state) {
  if (Number.isInteger(state) && state < 0) {
    that.loading += state;
  } else {
    that.loading = state;
  }
}

export async function getSocialInfo() {
  const cached = getSocialInfoFromCache();
  if (cached) {
    return cached;
  }

  const response = await Api.getPreferences({ section: 'social' });
  const resData = response.data;
  cacheSocialInfo(resData);
  return resData;
}

function getSocialInfoFromCache() {
  if (sessionStorage.getItem('social')) {
    try {
      return JSON.parse(sessionStorage.getItem('social'));
    } catch (e) {
      sessionStorage.removeItem('social');
    }
  }
}

function cacheSocialInfo(socialInfo) {
  sessionStorage.setItem('social', JSON.stringify(socialInfo));
}
