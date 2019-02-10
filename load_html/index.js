const { app, BrowserWindow } = require('electron');

const url = require('url')
let win = null

function boot() {
    win = new BrowserWindow();
    // win.loadURL(`file://${__dirname}/index.html`);
    win.loadURL(url.format({
        pathname: 'index.html',
        slashes: true
    }))
}

app.on('ready', boot);