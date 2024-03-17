# hoa.moe

This is the website of [HITSZ OpenAuto](https://github.com/HITSZ-OpenAuto), built with [Hugo](https://gohugo.io/) and [Hextra](https://imfing.github.io/hextra/).

![showcase](static/images/showcase.webp)

## Features

- **Fast**: Built with Hugo, the world's fastest framework for building websites.
- **Responsive Layout and Dark Mode** - It looks great on all devices, from mobile, tablet to desktop. Dark mode is also supported to accomodate various lighting conditions.
- **Full-text Search** - Built-in offline full-text search powered by FlexSearch, no additional configuration required.
- **Comments** - Support comments powered by [cusdis](https://cusdis.com/).
- **Continuous integration** - All of the documents are automatically fetched from the repositories of [HITSZ OpenAuto](https://github.com/HITSZ-OpenAuto), and updated without manual intervention.

## Quick Start

### Clone the repository

```bash
git clone https://github.com/HITSZ-OpenAuto/hoa.moe.git --recurse-submodules
```

### Install Hugo

You need to install Hugo extended version to build the website.

```bash
# Windows
winget install Hugo.Hugo.Extended

# macOS
brew install hugo

# Linux
sudo snap install hugo
```

### Run the development server

```bash
cd hoa.moe
hugo server
```

Open `http://localhost:1313` in your browser.

## Contributing

If you want to contribute to the documention, please refer to the [HITSZ OpenAuto 文档编写指南](https://hoa.moe/blog/writing-rules/).

To post your article, you can simply create a new markdown file in the `content/blog` directory, and submit a pull request.If you are not familiar with Git, you can also send your article to [📮hi@hoa.moe](mailto:hi@hoa.moe). We will review your article and merge it into the main branch if it meets the [requirements](https://github.com/HITSZ-OpenAuto/.github/blob/main/pull_request_template.md).

## License

This project is licensed under the CC BY-NC-SA 4.0 License.

## Acknowledgements

- [Hugo](https://gohugo.io/)
- [Hextra](https://imfing.github.io/hextra/)
