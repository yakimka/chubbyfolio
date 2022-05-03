import loader from './loader';

export default {
  VUE_APP_ROOT_API: loader.getConfigValue('VUE_APP_ROOT_API'),
  VUE_APP_SITE_NAME: loader.getConfigValue('VUE_APP_SITE_NAME')
};
