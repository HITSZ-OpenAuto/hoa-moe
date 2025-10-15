<h3 align="center">
  <img src="./static/images/HITSZOpenAutoShadow.webp" width="400" alt="Logo"/>
</h3>

<h1 align="center">hoa.moe</h1>

<p align="center">
  <a href="https://deepwiki.com/HITSZ-OpenAuto/hoa-moe"><img src="https://deepwiki.com/badge.svg" alt="Ask DeepWiki"></a>
</p>

<p align="center">
  <a href="README.md">English</a> | <a href="README-zh.md">中文</a>
</p>

<p align="center">
  hoa.moe is the official website of <a href="https://github.com/HITSZ-OpenAuto">HITSZ OpenAuto</a>, 
  built with <a href="https://gohugo.io/">Hugo</a> and 
  <a href="https://imfing.github.io/hextra/">Hextra</a>.
</p>

---

## Features

- **Fast** - Built with Hugo, the world's fastest framework for building websites.
- **Responsive Layout and Dark Mode** - It looks great on all devices, from mobile, tablet to desktop. Dark mode is also supported to accommodate various lighting conditions.
- **Full-text Search** - Built-in offline full-text search powered by FlexSearch, no additional configuration required.
- **Comments** - Support comments powered by [giscus](https://giscus.app/).
- **Continuous integration** - All of the documents are automatically fetched from the repositories of [HITSZ OpenAuto](https://github.com/HITSZ-OpenAuto), and updated without manual intervention.

## Quick Start

### Clone the repository

```bash
git clone https://github.com/HITSZ-OpenAuto/hoa-moe.git --recurse-submodules --depth=1
cd hoa-moe
```

### Using Hugo

You need to [install Hugo extended version](https://gohugo.io/installation/) to build the website. After installation, run:

```bash
hugo server
```

View your site at the URL displayed in your terminal. Press `Ctrl + C` to stop Hugo’s development server.

### (Alternative) Using NPM

```bash
npm install
npm run dev # run the development server and watch for custom Tailwind CSS changes
npm run serve # simply run the development server
npm run build # build CSS and generate static pages
npm run build:css # build only CSS
```

## Contributing

If you would like to contribute to the document, please refer to our [contribution guide](https://hoa.moe/blog/contribution-guide/). We also welcome code contributions, especially those addressing existing issues.

## License

The content on the project is licensed under the CC BY-NC-SA 4.0 License. The source code is licensed under [MIT License](LICENSE).

## Acknowledgements

- [Hugo](https://gohugo.io/)
- [Hextra](https://imfing.github.io/hextra/)
- [Programming VTuber Logos (addon edition)](https://github.com/PetricaT/ProgrammingVTuberLogos-Addon), [@Petrica](https://github.com/PetricaT) helped us with designing the wonderful logo in homepage.
