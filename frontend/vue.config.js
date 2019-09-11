const webpack = require('webpack');
const fs = require('fs');
const CopyWebpackPlugin = require('copy-webpack-plugin');

let additionalHeadContend = '';
if (process.env.NODE_ENV === 'production') {
  let additionalHeadContendFilePath = 'additional_prod_files/head_content.html';
  if (fs.existsSync(additionalHeadContendFilePath)) {
    additionalHeadContend = fs.readFileSync(additionalHeadContendFilePath, 'utf8');
    additionalHeadContend = additionalHeadContend.replace(/(\r\n|\n|\r)/gm, '');
  }
}

module.exports = {
  css: {
    sourceMap: true
  },
  configureWebpack: {
    devtool: 'source-map',
    plugins: [
      // copy custom static assets
      new CopyWebpackPlugin([
        {
          from: 'additional_prod_files/static_root',
          to: '.'
        }
      ]),
      new webpack.DefinePlugin({
        'VUE_APP_ADDITIONAL_HEAD_CONTENT': `"${additionalHeadContend}"`
      })
    ]
  }
};
