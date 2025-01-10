### VPS 到期监控助手 🚀

一个优雅的 VPS 到期日期监控工具，再也不用担心 VPS 续费超期了！通过 Telegram 机器人实时推送到期提醒，让您轻松管理多台服务器。



## ✨ 特色功能

- 🤖 支持 Telegram 机器人通知（3天内到期触发通知）
- ⏰ 自动定时检查（每天早8点和晚8点）
- 📊 支持批量管理多台服务器
- 🔔 灵活的提醒时间配置，按固定日期还是每月循环
- 💻 支持 GitHub Actions 自动运行





## 🚀 快速开始

下载项目到本地，双击运行

```
run_manager.bat
```

有两个地方需要手动修改，

- 修改`vps_manager.py `第53行，修改成你的监控地址，作用是仅在tg通知底部展示
- 把`config.example.json`重命名为`config.json`，目的是测试通知，注意只有即将到期才会触发通知

### 3. 通知部署

1. Fork 本仓库
2. 在仓库设置中添加以下 Secrets：
   - `TELEGRAM_BOT_TOKEN`: 您的 Telegram 机器人 token
   - `TELEGRAM_CHAT_ID`: 您的 Telegram 聊天 ID
3. Actions 会自动在每天早8点和晚8点（北京时间）运行检查

## 📝 使用说明

- 运行 `run_manager.bat` 管理您的 VPS 信息
- 运行 `check_expiry.bat`（Windows）快速检查到期状态
- 查看 `vps_monitor.log` 了解运行日志
- 通过 `index.html` 可视化查看 VPS 状态



## 📜 开源协议

本项目采用 MIT 协议开源，欢迎自由使用。

## ⭐ 支持项目

如果这个项目对您有帮助，请给它一个 Star！这是对我们最好的鼓励。

