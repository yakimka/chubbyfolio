'use strict';

const fs = require('fs');

let additionalHeadContend = '';
let additionalHeadContendFilePath = './additional_prod_files/head_content.html';
if (fs.existsSync(additionalHeadContendFilePath)) {
    additionalHeadContend = fs.readFileSync(additionalHeadContendFilePath, 'utf8');
    additionalHeadContend = additionalHeadContend.replace(/(\r\n|\n|\r)/gm, "");
}

module.exports = {
  NODE_ENV: '"production"',
  ADDITIONAL_HEAD_CONTENT: `"${additionalHeadContend}"`,
  VUE_APP_ROOT_API: `"${process.env.VUE_APP_ROOT_API}"`,
  VUE_APP_SITE_NAME: `"${process.env.VUE_APP_SITE_NAME}"`
};
