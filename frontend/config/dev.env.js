'use strict';
const merge = require('webpack-merge');
const prodEnv = require('./prod.env');

module.exports = merge(prodEnv, {
  NODE_ENV: '"development"',
  VUE_APP_ROOT_API: `"${process.env.VUE_APP_ROOT_API}"`,
  VUE_APP_SITE_NAME: `"${process.env.VUE_APP_SITE_NAME}"`
});
