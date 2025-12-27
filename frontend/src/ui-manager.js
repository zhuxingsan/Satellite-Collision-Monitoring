class LayoutController {
    constructor(triggersConfig) {
        this.triggers = triggersConfig || {};
        this._bindEvents();
    }

    _bindEvents() {
        for (const [btnId, panelId] of Object.entries(this.triggers)) {
            const btn = document.getElementById(btnId);
            const panel = document.getElementById(panelId);
            if (btn && panel) {
                btn.addEventListener('click', () => panel.classList.toggle('closed'));
            }
        }
    }

    // 控制底部详情面板的展开/收起逻辑
    toggleDetailPanel(overlayId, btnId) {
        const panel = document.getElementById(overlayId);
        const btn = document.getElementById(btnId);
        if (!panel || !btn) return;

        const isActive = panel.classList.contains('active');
        const isExpanded = panel.classList.contains('expanded');

        if (!isActive) {
            panel.classList.add('active');
            panel.classList.remove('expanded');
            btn.innerText = "[ SHOW FULL DATA ]";
        } else if (isActive && !isExpanded) {
            panel.classList.add('expanded');
            btn.innerText = "[ HIDE DETAILS ]";
        } else {
            panel.classList.remove('active');
            panel.classList.remove('expanded');
            btn.innerText = "[ SHOW DETAILS ]";
        }
    }
    
    
    
the code is coming soon
85327
91342
8409