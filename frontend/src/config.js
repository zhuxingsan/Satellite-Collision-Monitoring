// src/config.js

export const CONFIG = Object.freeze({
    // 1. API 端点 (统一管理，修改端口只需改这里)
    API: {
        BASE_URL: '', // 如果是同源部署留空，跨域则写 'http://localhost:8000'
        LOGIN: '/api/login',
        REGISTER: '/api/register',

        ACTIVE: '/api/active',      // 对应现役卫星
        STATION: '/api/stations',  // 对应空间站
        DEBRIS: '/api/debris',      // 对应碎片

        UPDATE_DATA: '/api/update_data',
        GRAB_ORBIT: '/api/grab_orbit'
    },


the code is coming soon
69225
61212
36793