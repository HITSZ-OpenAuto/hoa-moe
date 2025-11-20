---
title: 前端架构概览（旧版）
description: 适用于 Hextra v0.10.0 之前，使用 Tailwind CSS v3
date: 2025-01-26
authors:
  - name: longlin li
    link: https://github.com/longlin10086
    image: https://github.com/longlin10086.png
excludeSearch: false
math: true
weight: 5
---

> [!NOTE]
> 本文档适用于 Hextra v0.10.0 之前的版本，对应 HOA 1.0.0 及更早版本，若你使用的是更新版本，请参考[这篇文章](../frontend)。

### 前端调试方法

克隆本仓库代码后，在本地仓库根目录下运行 `hugo server`，你便可以从命令行获得调试时所需的端口号，浏览器内打开即可：

![port](server.png)

> [!WARNING]
> 由于 Hextra 主题使用 TailwindCSS，但在配置上有部分错误，我们需要手动做些调整才能将新的 Tailwind 样式渲染至页面。

1. 更改 `themes/hextra/tailwind.config.js`

   ```js
   module.exports = {
     prefix: 'hx-',  // 由于存在这么一行，所有 TailwindCSS 类都需要在原基础上加上 'hx-' 前缀
     content: [
       './**/hugo_stats.json',
       '../../layouts/**/*.{html, js}' // 新增这一行
     ],
     ...
   }
   ```

2. 更改 `themes/hextra/package.json`

   ```json
   {
     "scripts": {
       "dev:theme": "hugo server --logLevel=debug --config=hugo.yaml,../dev.toml --environment=theme --source=exampleSite --themesDir=../.. --disableFastRender -D --port 1313",
       "dev": "hugo server --source=exampleSite --themesDir=../.. --disableFastRender -D --port 1313",
       "build:css": "npx postcss --config postcss.config.js --env production assets/css/styles.css -o assets/css/compiled/main.css",
       "build": "hugo --gc --minify --themesDir=../.. --source=exampleSite",
       "watch": "npx postcss --config postcss.config.js --env production assets/css/styles.css -o ../../assets/css/compiled/main.css --watch" // 新增这一行
     }
   }
   ```

3. 在 `themes/hextra` 目录下运行 `npm run watch`

做完以上步骤后，我们在 `layouts` 下的 html 中写的 TailwindCSS 类才能被编译到 `assets/css/compiled/main.css` 中，从而被完整导入进 `head-css.html`。

如果你想更改组件样式，或添加新组件，则可以在根目录的 `layouts` 文件夹下进行修改了！如果涉及对 `themes` 主题文件夹内文件的修改，请按相同路径复制一份到根目录，再在新文件内做修改！
