const fs = require('fs');
//vue.config.js
module.exports = {
    devServer: {
        //Start http configuration
        open: process.platform === 'darwin',
        host: '0.0.0.0',
        port: 443, //80
        https: { //true, //false
            key: fs.readFileSync('/etc/letsencrypt/live/investors.opn.ninja/privkey.pem'),
            cert: fs.readFileSync('/etc/letsencrypt/live/investors.opn.ninja/fullchain.pem'),
        },
        hotOnly: false,
        //End https configuration
        disableHostCheck: true,
    },
}
