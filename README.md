# standalone search bar for Feishu/Lark

给飞书添加一个独立的顶部搜索入口 :p

![screenshot](https://github.com/Antonoko/feishu-standalone-search/blob/main/__asset__/screenshot-gif.gif)

### 如何使用
- 在 [Release](https://github.com/Antonoko/feishu-standalone-search/releases) 下载可执行文件。由于没有进行签名，可能会被系统安全软件拦截，需要手动信任。
- 如果担心安全问题，可以手动使用 python 执行 `app.py`，需要先安装依赖：`pip install -r requirements.txt`。
    - macOS 安装依赖：`pip install -r requirements-mac.txt`

### 工作原理
- 使用 Qt 置顶绘制一个搜索栏图片，点击后唤起前台飞书窗口、自动按下 ctrl + k 进入大搜；
- 右键菜单选择 close 退出；

> [!TIP]
>
> 很草包的一个小玩具，对 Windows 支持比较良好，在 macOS 上体验糟糕：启动速度慢、无法置顶显示、响应不跟手。
