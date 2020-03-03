const webpack = require('webpack');
const fs = require('fs');
const CopyWebpackPlugin = require('copy-webpack-plugin');
const SitemapPlugin = require('sitemap-webpack-plugin').default;
const prettydata = require('pretty-data');

let additionalHeadContend = '';
if (process.env.NODE_ENV === 'production') {
  const additionalHeadContendFilePath = 'additional_prod_files/head_content.html';
  if (fs.existsSync(additionalHeadContendFilePath)) {
    additionalHeadContend = fs.readFileSync(additionalHeadContendFilePath, 'utf8');
    additionalHeadContend = additionalHeadContend.replace(/(\r\n|\n|\r)/gm, '');
  }
}

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

    newConfig.plugins.push(
      new webpack.DefinePlugin({
        VUE_APP_ADDITIONAL_HEAD_CONTENT: `"${additionalHeadContend}"`
      })
    );

    if (process.env.NODE_ENV === 'production') {
      delete config.devtool;

      // copy custom static assets
      newConfig.plugins.push(
        new CopyWebpackPlugin([
          {
            from: 'additional_prod_files/static_root',
            to: '.'
          }
        ])
      );

      // create sitemap
      newConfig.plugins.push(
        new SitemapPlugin(process.env.VUE_APP_SITE_URL, paths, {
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
