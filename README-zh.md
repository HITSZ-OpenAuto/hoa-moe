<h3 align="center">
	<img src="./static/images/HITSZOpenAutoShadow.webp" width="400" alt="Logo"/><br/>
</h3>
<h1 align="center">hoa.moe</h1>
<h5 align="center"><a href="README.md">English</a> | <a href="README-zh.md">中文</a></h5>

<p align="center">本网站使用 <a href="https://gohugo.io/">Hugo</a> 框架和 <a href="https://imfing.github.io/hextra/">Hextra</a> 主题进行构建，由 <a href="https://github.com/HITSZ-OpenAuto">HITSZ OpenAuto</a>团队管理维护。</p>

![showcase](static/images/showcase.webp)

## 网站特点

- **快速高效** - 使用当前世界上构建网站速度最快的 Hugo 框架搭建。
- **响应式布局及美观的暗黑主题** - 网站支持所有设备正常访问，无论是移动端还是桌面端。我们还提供了暗黑模式以供用户在不同亮度条件下进行选择。
- **完善的文本搜索功能** - 网站的文本搜索功能由 FlexSearch 进行驱动，不需要任何额外配置。
- **评论功能** - 网站支持由 [giscus](https://giscus.app/) 提供的评论功能。
- **持续集成** - 网站的所有文档都会从 [HITSZ OpenAuto](https://github.com/HITSZ-OpenAuto) 组织的仓库下自动抓取，更新不需要任何人为干预。

## 快速上手

### 克隆仓库

```bash
git clone https://github.com/HITSZ-OpenAuto/hoa-moe.git --recurse-submodules --depth=1
cd hoa-moe
```

### 使用 Hugo 搭建开发环境

你需要安装[Hugo 扩展版](https://gohugo.io/installation/)来构建网站。安装完成后，运行：

```bash
hugo server
```

在终端显示的 URL 访问你的网站。按 `Ctrl + C` 停止 Hugo 开发服务器。

### （可选）使用 NPM 搭建开发环境

```bash
npm install
npm run dev # 运行开发服务器并查看自定义 Tailwind CSS 的更改
npm run serve # 仅运行开发服务器
npm run build # 编译 CSS 并生成静态页面
npm run build:css # 仅编译 CSS
```

## 如何贡献

如果您想参与网页中的内容编写，请阅读我们的[《参与指南》](https://hoa.moe/blog/contribution-guide/)。我们也欢迎代码贡献，特别是那些解决现有问题的贡献。

## 开源许可证

由贡献者编写部分的许可采用 CC BY-NC-SA 4.0 协议；本网站源代码采用 [MIT 许可](LICENSE)。

## 鸣谢

- [Hugo](https://gohugo.io/)
- [Hextra](https://imfing.github.io/hextra/)
- [Programming VTuber Logos (addon edition)](https://github.com/PetricaT/ProgrammingVTuberLogos-Addon), [@Petrica](https://github.com/PetricaT) 帮助我们设计了首页中好看的 Logo
