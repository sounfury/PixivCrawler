

# PixivCrawler

<div align="center">PixivCrawler</div>

<div align="center">
    <img src="https://img.shields.io/badge/python-3.8+-blue" alt="Python Version" />
    <img src="https://img.shields.io/badge/scrapy-2.5+-orange" alt="Scrapy Version" />
    <img src="https://img.shields.io/badge/license-MIT-green" alt="License" />
</div>

---

## 📖 项目介绍

**PixivCrawler** 是一个基于 Scrapy 框架的图片爬虫项目，旨在从 [Pixiv](https://www.pixiv.net) 网站抓取插画和艺术家的相关信息。该项目能够自动化地提取艺术作品的图片链接和其他元数据，方便用户进行收藏和管理。

## 🛠️ 技术栈

- **Python**: 主要编程语言
- **Scrapy**: 高效的爬虫框架
- **Git**: 版本控制

## 🌟 功能亮点
- **高效抓取**: 支持批量获取插画和艺术家的数据，最大限度地提高爬取效率。
- **多种抓取方式**: 支持按标签、排行榜和关键词搜索抓取插画，灵活满足不同需求。
- **图片方向选择**: 用户可以指定抓取的图片类型（横图、竖图或正方形）。
- **多进程支持**: 通过 Scrapy 的并发请求功能，显著提高爬取速度。
- **灵活配置**: 可根据不同需求定制爬虫策略，支持多种爬取方式。
- **数据存储**: 将抓取的图片链接和信息存储在本地，可进行后续分析。
- **逻辑清晰**: 使用面向对象的设计方法，方便扩展和维护代码。

## ⚙️ 安装与使用
### 启动爬虫
1. **登录 Pixiv**: 请先在 Edge 浏览器中登录您的 Pixiv 账号。

2. **关闭浏览器进程**: 在运行爬虫之前，请确保关闭 Edge 浏览器进程，以便 cookie 库正常运行。

3. **克隆仓库**:
   ```bash
   git clone https://github.com/yourusername/PixivCrawler.git
   cd PixivCrawler
   ```
   
4. **安装依赖**:
    ```bash
      pip install -r requirements.txt
    ```

5. **运行爬虫**:
   ```bash
   scrapy crawl painter -a painter_id=YOUR_PAINTER_ID
   ```

   将 `YOUR_PAINTER_ID` 替换为您想要抓取的艺术家的 ID。
### 自定义设置
在`settings.py`里面可以自定义并发请求数，图片保存路径
## 📚 贡献

我们欢迎任何形式的贡献！您可以通过提交问题、请求功能或拉取请求来帮助我们改善项目。

1. Fork 本仓库
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建新的 Pull Request

## 📝 许可证

该项目遵循 [MIT 许可证](LICENSE)。

## 📬 联系我们

如有问题或建议，请通过以下方式联系我：

- Email: a2133266@outlook.email

---
