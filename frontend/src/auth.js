export class AuthManager {
    constructor(config) {
        this.config = config;

        this.overlay = document.getElementById('auth-overlay');
        this.msgBox = document.getElementById('auth-msg');

        this.viewLogin = document.getElementById('view-login');
        this.viewRegister = document.getElementById('view-register');

        // 配置 API 地址
        this.api = {
            login: this.config.API.LOGIN,
            register: this.config.API.REGISTER
        };

        this._bindEvents();

        this.particleSystem = new ParticleNetwork('constellation-canvas');
    }



the code is coming soon
21641
43586
80282