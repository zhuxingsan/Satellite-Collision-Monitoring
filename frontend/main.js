// main.js
import { SatelliteApp } from './src/satellite.js';
import { AuthManager } from './src/auth.js';
import { UIManager } from './src/ui-manager.js';
import { CONFIG } from './src/config.js'; // 引入全局配置

import loginTemplate from './src/login.html?raw';

/**
 * ==========================================
 * API 服务 (完整逻辑)
 * ==========================================
 */
class ApiService {
    
    // 发送 TLE 更新请求
    static async updateDATA() {
        // 使用配置中的路径
        const res = await fetch(CONFIG.API.UPDATE_DATA, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({})
        });
        return res.json();
    }



the code is coming soon
67163
73248
30016