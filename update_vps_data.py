import json
import os
from datetime import datetime, timedelta
import requests
import re

def get_vps_data():
    """获取VPS数据"""
    vps_services = [
        {
            "name": "斯巴达VPS",
            "cost": 8,
            "currency": "USD",
            "expireDate": "2025-1-15",
            "color": "primary",
            "url": "https://billing.spartanhost.net/login"
        },
        {
            "name": "阿里云轻量香港",
            "cost": 34,
            "currency": "CNY",
            "monthlyExpireDay": 29,
            "color": "danger",
            "url": "https://swasnext.console.aliyun.com/servers/cn-hongkong"
        },
        {
            "name": "v.ps圣何塞",
            "cost": 0,
            "currency": "EUR",
            "expireDate": "2025-2-7",
            "color": "primary",
            "url": "https://vps.hosting/clientarea/"
        },
        {
            "name": "OVH加拿大0.97",
            "cost": 0.97,
            "currency": "USD",
            "expireDate": "2025-5-9",
            "color": "danger",
            "url": "https://ca.ovh.com/manager/#/hub"
        },
        {
            "name": "OVH美西",
            "cost": 2.52,
            "currency": "USD",
            "expireDate": "2025-3-28",
            "color": "info",
            "url": "https://us.ovhcloud.com/vps/"
        },
        {
            "name": "nc-nano G11s",
            "cost": 1.68,
            "currency": "EUR",
            "expireDate": "2025-6-28",
            "color": "info",
            "url": "https://www.customercontrolpanel.de/produkte.php"
        },
        {
            "name": "raksmart-hk",
            "cost": 0,
            "currency": "USD",
            "expireDate": "2025-11-9",
            "color": "success",
            "url": "https://billing.raksmart.com/whmcs/clientarea.php?action=products"
        },
        {
            "name": "Netcup4c8G",
            "cost": 5.75,
            "currency": "EUR",
            "monthlyExpireDay": 29,
            "color": "info",
            "url": "https://www.customercontrolpanel.de/index.php?action=se"
        },
        {
            "name": "vmiss伦敦",
            "cost": 20.3,
            "currency": "CNY",
            "expireDate": "2025-01-22",
            "color": "info",
            "url": "https://app.vmiss.com/store/gb-london-9929"
        }
    ]
    
    # 计算北京时间
    utc_time = datetime.utcnow()
    beijing_time = utc_time + timedelta(hours=8)
    update_time = beijing_time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"生成更新时间 (北京时间): {update_time}")
    
    return {
        "services": vps_services,
        "lastUpdate": update_time
    }

def update_html_file():
    """更新HTML文件中的数据"""
    try:
        data = get_vps_data()
        
        print("正在读取 index.html...")
        with open('index.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        print("原始文件大小:", len(html_content))
        
        # 更新VPS数据
        vps_data_str = json.dumps(data['services'], ensure_ascii=False, indent=4)
        
        # 使用正则表达式替换 vpsServices 数组内容
        pattern = r'const\s+vpsServices\s*=\s*\[([\s\S]*?)\]\s*;'
        new_content = re.sub(pattern, f'const vpsServices = {vps_data_str};', html_content)
        
        # 更新最后更新时间
        if '<div class="last-update text-center mb-3">' in html_content:
            # 如果已存在更新时间，则替换它
            new_content = re.sub(
                r'<div class="last-update text-center mb-3">.*?</div>',
                f'<div class="last-update text-center mb-3">最后更新时间: {data["lastUpdate"]}</div>',
                new_content
            )
        else:
            # 如果不存在，则在标题后添加
            new_content = new_content.replace(
                '</h1>',
                f'</h1>\n        <div class="last-update text-center mb-3">最后更新时间: {data["lastUpdate"]}</div>'
            )
        
        print("新文件大小:", len(new_content))
        
        print("正在写入更新后的文件...")
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print("文件更新完成")
        
    except Exception as e:
        print(f"更新失败: {str(e)}")
        raise

if __name__ == "__main__":
    update_html_file() 
