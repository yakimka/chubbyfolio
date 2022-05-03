const SitemapPlugin = require('sitemap-webpack-plugin').default;
const prettydata = require('pretty-data');

const paths = [
  '/',
  '/portfolio',
  '/contact-me',
  '/about-me'
];

const prettyPrint = xml => {
  return prettydata.pd.xml(xml);
};

module.exports = {
  css: {
    sourceMap: process.env.NODE_ENV !== 'production'
  },
  devServer: {
    disableHostCheck: true
  },
  configureWebpack: config => {
    const newConfig = {
      plugins: []
    };

    if (process.env.NODE_ENV === 'production') {
      delete config.devtool;

      // create sitemap
      newConfig.plugins.push(
        new SitemapPlugin('https://sitemap.url/', paths, {
          priority: '0.9',
          skipGzip: true,
          formatter: prettyPrint
        })
      );
    } else {
      newConfig.devtool = 'source-map';
    }

    return newConfig;
  }
};
