document.addEventListener("DOMContentLoaded", function() {
    // 获取所有需要检测的链接元素
    const linkElements = document.querySelectorAll('.hoa-friend-link');

    const checkAllNetworks = async () => {
        const networkChecks = Array.from(linkElements).map(linkElement => {
            const networkPoint = linkElement.querySelector('.hoa-network-point');
            const link = linkElement.dataset.link;
            
            if (!networkPoint || !link) return Promise.resolve();
            
            return (async () => {
                // 初始状态移除所有背景色
                networkPoint.classList.remove('hx-bg-green-500', 'hx-bg-yellow-500', 'hx-bg-red-500');
                
                try {
                    const controller = new AbortController();
                    const timeoutId = setTimeout(() => controller.abort(), 4000);
                    
                    const startTime = Date.now();
                    
                    const response = await Promise.race([
                        fetch(link, {
                            method: 'HEAD',
                            signal: controller.signal,
                            mode: 'no-cors'
                        }).then(response => {
                            // console.log(`${link}: ${response.headers}`);
                        }),
                        new Promise((_, reject) => {
                            setTimeout(() => reject(new Error('Timeout')), 4000);
                        })
                    ]);
                    
                    clearTimeout(timeoutId);
                    const responseTime = Date.now() - startTime;
                    
                    // 根据响应时间添加对应的类
                    if (responseTime <= 2000) {
                        networkPoint.classList.add('hx-bg-green-500');
                    } else if (responseTime < 4000) {
                        networkPoint.classList.add('hx-bg-yellow-500');
                    }
                } catch (error) {
                    // 发生错误或超时时添加红色类名
                    networkPoint.classList.add('hx-bg-red-500');
                }
            })();
        });
    
        // 等待所有网络检查完成
        await Promise.all(networkChecks);
    };
        
    // 立即执行检查
    checkAllNetworks();
    
    // 每1h检查一次
    // setInterval(checkNetworkStatus, 3600000);
});