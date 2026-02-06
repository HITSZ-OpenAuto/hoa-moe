---
title: （必修）创新训练课 B
weight: 4
toc: true
editURL: "https://github.com/HITSZ-OpenAuto/AUTO2003B/edit/main/README.md"
math: true
---

{{< update-info update_time="2026 年 2 月 6 日" author="Jiao Ziang" message="Merge pull request #25 from HITSZ-OpenAuto/ci/add-root-readme-toml" >}}

<div class="hoa-badge">

![%E6%88%90%E7%BB%A9%E6%9E%84%E6%88%90](https://img.shields.io/badge/%E6%88%90%E7%BB%A9%E6%9E%84%E6%88%90-gold)
![%E5%A4%A7%E4%BD%9C%E4%B8%9A100%](https://img.shields.io/badge/%E5%A4%A7%E4%BD%9C%E4%B8%9A-100%25-wheat)

</div>

本课程与教师基本无关，结题答辩时的老师也是任意分配的。
夏季学期结束时需提交开题报告；成果最后在大一立项结题的同时验收，需提交结题报告。

## 在线资源

- [MaxwellJay256/MetroTicketingSystem](https://github.com/MaxwellJay256/MetroTicketingSystem)：模拟地铁售票系统，有二进制成品和 demo。
- [chenxijun/KingdomCard](https://github.com/chenxijun/KingdomCard)：三国杀游戏。C/S 架构，支持局域网联机。前端 Qt6，后端 Modern C++。
- [Simulate_Shenzhen_Subway_Ticketing_System](https://github.com/novemberinnorth/Simulate_Shenzhen_Subway_Ticketing_System)：使用 C++ Qt6 实现图形化的模拟深圳地铁自动售票系统。
- [Sieroy/Musnake](https://github.com/Sieroy/Musnake)：使用 SDL2 实现图形界面的、融合轻量音游玩法的贪吃蛇游戏。附有可玩 demo。

## 课程内容

课程设计是在学生完成高级语言程序设计课程学习后进行的。
翻译：**自己动手制作一个程序**。

选题从课程给出的几个中选择一个，或者提交你自己的选题。
2022 级给出的选题有：

- 学院职工管理信息管理系统
- 学院学生信息管理系统
- 模拟地铁自动售票系统
- 贪吃蛇小游戏
- 跳棋游戏
- 简易三国杀游戏

## 学习建议

这应该是自动化学生为数不多的参与软件开发的机会。

选题
图省事的话推荐贪吃蛇之类的小游戏，借助 AI 不到 1 天就能速通，但是你需要想想答辩的时候能说些什么。
如果想多积累一点敲代码经验，可以选择客户端类型的软件（信息管理系统、售票系统），体验一下前、后端的开发思想。

组队
课程要求 1-2 人一个小组。如果选择组队，建议启用 git 这种版本控制系统。
如果对团队协作没有信心，或者对你的队友没有信心，一个人组队会轻松很多。

挑选一个开发框架
**课程要求项目必须使用 `C/C++`**，需要使用第三方库来实现 GUI。

1. **EasyX**：基于 `GDI+`，古老简单但功能有限。
2. **Qt**：跨平台的 GUI 开发框架，功能强大，学生证可以申请教育许可证（个人推荐）。
3. **MFC**：Windows 编程框架，兼容性好但开发效率低。
4. **C#**：仅限在实现图形界面的时候使用，代码逻辑仍需使用 `C/C++`。

IDE
推荐使用 **Visual Studio**（MFC 或 C# 的最佳选择，也有 Qt 插件）或 **Qt Creator**。

## 资料下载

如果你是校内学生，可点击如下「内网网盘」按钮查看本门课程的电子书、课件和实验软件等。

{{< hoa-filetree/container driveURL="https://open.osa.moe/openauto/AUTO2003B" repoURL="https://github.com/HITSZ-OpenAuto/AUTO2003B" >}}
{{< hoa-filetree/folder name="course_design" date="" state="closed" >}}
{{< hoa-filetree/folder name="WKY" date="" state="closed" >}}
{{< hoa-filetree/file name="创新训练课 B 报告" type="docx" size="1.3 MB" date="2025/06/28" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/WKY/%E5%88%9B%E6%96%B0%E8%AE%AD%E7%BB%83%E8%AF%BEB%E6%8A%A5%E5%91%8A.docx" >}}
{{< hoa-filetree/file name="答辩 PPT_吴坤远" type="pptx" size="351.1 KB" date="2025/06/28" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/WKY/%E7%AD%94%E8%BE%A9PPT_%E5%90%B4%E5%9D%A4%E8%BF%9C.pptx" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="fish_game" date="" state="closed" >}}
{{< hoa-filetree/folder name="Debug" date="" state="closed" >}}
{{< hoa-filetree/file name="fish_game" type="exe" size="152.0 KB" date="2023/11/29" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/Debug/fish_game.exe" >}}
{{< hoa-filetree/file name="fish_game.exe" type="recipe" size="314 bytes" date="2023/11/29" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/Debug/fish_game.exe.recipe" >}}
{{< hoa-filetree/file name="fish_game" type="ilk" size="1.0 MB" date="2023/11/29" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/Debug/fish_game.ilk" >}}
{{< hoa-filetree/file name="fish_game" type="log" size="279 bytes" date="2023/11/29" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/Debug/fish_game.log" >}}
{{< hoa-filetree/file name="fish_game" type="pdb" size="5.1 MB" date="2023/11/29" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/Debug/fish_game.pdb" >}}
{{< hoa-filetree/folder name="fish_game.tlog" date="" state="closed" >}}
{{< hoa-filetree/file name="CL.command.1" type="tlog" size="2.0 KB" date="2023/11/29" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/Debug/fish_game.tlog/CL.command.1.tlog" >}}
{{< hoa-filetree/file name="CL.read.1" type="tlog" size="20.2 KB" date="2023/11/29" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/Debug/fish_game.tlog/CL.read.1.tlog" >}}
{{< hoa-filetree/file name="CL.write.1" type="tlog" size="412 bytes" date="2023/11/29" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/Debug/fish_game.tlog/CL.write.1.tlog" >}}
{{< hoa-filetree/file name="fish_game" type="lastbuildstate" size="191 bytes" date="2023/11/29" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/Debug/fish_game.tlog/fish_game.lastbuildstate" >}}
{{< hoa-filetree/file name="link.command.1" type="tlog" size="2.2 KB" date="2023/11/29" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/Debug/fish_game.tlog/link.command.1.tlog" >}}
{{< hoa-filetree/file name="link.read.1" type="tlog" size="3.0 KB" date="2023/11/29" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/Debug/fish_game.tlog/link.read.1.tlog" >}}
{{< hoa-filetree/file name="link.write.1" type="tlog" size="450 bytes" date="2023/11/29" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/Debug/fish_game.tlog/link.write.1.tlog" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/file name="fish_game.vcxproj.FileListAbsolute" type="txt" size="127 bytes" date="2023/11/29" icon="icons/txt.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/Debug/fish_game.vcxproj.FileListAbsolute.txt" >}}
{{< hoa-filetree/file name="main" type="obj" size="144.0 KB" date="2023/11/29" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/Debug/main.obj" >}}
{{< hoa-filetree/file name="main.obj" type="enc" size="147.7 KB" date="2023/11/29" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/Debug/main.obj.enc" >}}
{{< hoa-filetree/file name="test" type="obj" size="19.9 KB" date="2023/11/29" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/Debug/test.obj" >}}
{{< hoa-filetree/file name="vc142" type="idb" size="427.0 KB" date="2023/11/29" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/Debug/vc142.idb" >}}
{{< hoa-filetree/file name="vc142" type="pdb" size="164.0 KB" date="2023/11/29" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/Debug/vc142.pdb" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/file name="EAT" type="mp3" size="12.1 KB" date="2023/11/29" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/EAT.mp3" >}}
{{< hoa-filetree/file name="FAIL" type="mp3" size="99.4 KB" date="2023/11/29" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/FAIL.mp3" >}}
{{< hoa-filetree/file name="NOPE" type="mp3" size="12.6 KB" date="2023/11/29" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/NOPE.mp3" >}}
{{< hoa-filetree/folder name="Release" date="" state="closed" >}}
{{< hoa-filetree/file name="fish_game" type="log" size="29.6 KB" date="2023/11/29" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/Release/fish_game.log" >}}
{{< hoa-filetree/folder name="fish_game.tlog" date="" state="closed" >}}
{{< hoa-filetree/file name="CL.command.1" type="tlog" size="2 bytes" date="2023/11/29" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/Release/fish_game.tlog/CL.command.1.tlog" >}}
{{< hoa-filetree/file name="fish_game" type="lastbuildstate" size="156 bytes" date="2023/11/29" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/Release/fish_game.tlog/fish_game.lastbuildstate" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/file name="vc142" type="pdb" size="78.0 KB" date="2023/11/29" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/Release/vc142.pdb" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/file name="VICTORY" type="mp3" size="142.5 KB" date="2023/11/29" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/VICTORY.mp3" >}}
{{< hoa-filetree/file name="bg" type="jpg" size="355.8 KB" date="2023/11/29" icon="icons/image.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/bg.jpg" >}}
{{< hoa-filetree/file name="bg2" type="jpg" size="888.0 KB" date="2023/11/29" icon="icons/image.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/bg2.jpg" >}}
{{< hoa-filetree/file name="bgm" type="mp3" size="1.9 MB" date="2023/11/29" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/bgm.mp3" >}}
{{< hoa-filetree/file name="fish1_l" type="jpg" size="946 bytes" date="2023/11/29" icon="icons/image.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/fish1_l.jpg" >}}
{{< hoa-filetree/file name="fish1_r" type="jpg" size="1.2 KB" date="2023/11/29" icon="icons/image.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/fish1_r.jpg" >}}
{{< hoa-filetree/file name="fish1bg_l" type="jpg" size="888 bytes" date="2023/11/29" icon="icons/image.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/fish1bg_l.jpg" >}}
{{< hoa-filetree/file name="fish1bg_r" type="jpg" size="890 bytes" date="2023/11/29" icon="icons/image.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/fish1bg_r.jpg" >}}
{{< hoa-filetree/file name="fish2_l" type="jpg" size="2.8 KB" date="2023/11/29" icon="icons/image.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/fish2_l.jpg" >}}
{{< hoa-filetree/file name="fish2_r" type="jpg" size="3.8 KB" date="2023/11/29" icon="icons/image.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/fish2_r.jpg" >}}
{{< hoa-filetree/file name="fish2bg_l" type="jpg" size="1.8 KB" date="2023/11/29" icon="icons/image.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/fish2bg_l.jpg" >}}
{{< hoa-filetree/file name="fish2bg_r" type="jpg" size="2.1 KB" date="2023/11/29" icon="icons/image.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/fish2bg_r.jpg" >}}
{{< hoa-filetree/file name="fish3_l" type="jpg" size="7.1 KB" date="2023/11/29" icon="icons/image.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/fish3_l.jpg" >}}
{{< hoa-filetree/file name="fish3_r" type="jpg" size="4.7 KB" date="2023/11/29" icon="icons/image.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/fish3_r.jpg" >}}
{{< hoa-filetree/file name="fish3bg_l" type="jpg" size="2.9 KB" date="2023/11/29" icon="icons/image.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/fish3bg_l.jpg" >}}
{{< hoa-filetree/file name="fish3bg_r" type="jpg" size="2.8 KB" date="2023/11/29" icon="icons/image.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/fish3bg_r.jpg" >}}
{{< hoa-filetree/file name="fish4_l" type="jpg" size="11.1 KB" date="2023/11/29" icon="icons/image.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/fish4_l.jpg" >}}
{{< hoa-filetree/file name="fish4_r" type="jpg" size="6.7 KB" date="2023/11/29" icon="icons/image.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/fish4_r.jpg" >}}
{{< hoa-filetree/file name="fish4bg_l" type="jpg" size="5.0 KB" date="2023/11/29" icon="icons/image.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/fish4bg_l.jpg" >}}
{{< hoa-filetree/file name="fish4bg_r" type="jpg" size="4.7 KB" date="2023/11/29" icon="icons/image.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/fish4bg_r.jpg" >}}
{{< hoa-filetree/file name="fish_game" type="sln" size="1.4 KB" date="2023/11/29" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/fish_game.sln" >}}
{{< hoa-filetree/file name="fish_game" type="vcxproj" size="6.9 KB" date="2023/11/29" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/fish_game.vcxproj" >}}
{{< hoa-filetree/file name="fish_game.vcxproj" type="filters" size="945 bytes" date="2023/11/29" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/fish_game.vcxproj.filters" >}}
{{< hoa-filetree/file name="fish_game.vcxproj" type="user" size="165 bytes" date="2023/11/29" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/fish_game.vcxproj.user" >}}
{{< hoa-filetree/file name="hippocampus_l" type="jpg" size="3.1 KB" date="2023/11/29" icon="icons/image.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/hippocampus_l.jpg" >}}
{{< hoa-filetree/file name="hippocampus_r" type="jpg" size="4.1 KB" date="2023/11/29" icon="icons/image.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/hippocampus_r.jpg" >}}
{{< hoa-filetree/file name="hippocampusbg_l" type="jpg" size="2.2 KB" date="2023/11/29" icon="icons/image.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/hippocampusbg_l.jpg" >}}
{{< hoa-filetree/file name="hippocampusbg_r" type="jpg" size="2.2 KB" date="2023/11/29" icon="icons/image.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/hippocampusbg_r.jpg" >}}
{{< hoa-filetree/file name="intro" type="jpg" size="15.4 KB" date="2023/11/29" icon="icons/image.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/intro.jpg" >}}
{{< hoa-filetree/file name="intro0" type="jpg" size="35.9 KB" date="2023/11/29" icon="icons/image.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/intro0.jpg" >}}
{{< hoa-filetree/file name="intro1" type="jpg" size="17.2 KB" date="2023/11/29" icon="icons/image.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/intro1.jpg" >}}
{{< hoa-filetree/file name="intro2" type="jpg" size="10.8 KB" date="2023/11/29" icon="icons/image.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/intro2.jpg" >}}
{{< hoa-filetree/file name="main" type="cpp" size="24.3 KB" date="2023/11/29" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/main.cpp" >}}
{{< hoa-filetree/file name="player1_l" type="jpg" size="30.8 KB" date="2023/11/29" icon="icons/image.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/player1_l.jpg" >}}
{{< hoa-filetree/file name="player1_r" type="jpg" size="24.6 KB" date="2023/11/29" icon="icons/image.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/player1_r.jpg" >}}
{{< hoa-filetree/file name="player1bg_l" type="jpg" size="12.6 KB" date="2023/11/29" icon="icons/image.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/player1bg_l.jpg" >}}
{{< hoa-filetree/file name="player1bg_r" type="jpg" size="12.5 KB" date="2023/11/29" icon="icons/image.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/player1bg_r.jpg" >}}
{{< hoa-filetree/file name="player2_l" type="jpg" size="2.4 KB" date="2023/11/29" icon="icons/image.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/player2_l.jpg" >}}
{{< hoa-filetree/file name="player2_r" type="jpg" size="2.3 KB" date="2023/11/29" icon="icons/image.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/player2_r.jpg" >}}
{{< hoa-filetree/file name="player2bg_l" type="jpg" size="1.4 KB" date="2023/11/29" icon="icons/image.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/player2bg_l.jpg" >}}
{{< hoa-filetree/file name="player2bg_r" type="jpg" size="1.4 KB" date="2023/11/29" icon="icons/image.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/player2bg_r.jpg" >}}
{{< hoa-filetree/file name="shark_l" type="jpg" size="17.2 KB" date="2023/11/29" icon="icons/image.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/shark_l.jpg" >}}
{{< hoa-filetree/file name="shark_r" type="jpg" size="24.7 KB" date="2023/11/29" icon="icons/image.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/shark_r.jpg" >}}
{{< hoa-filetree/file name="sharkbg_l" type="jpg" size="10.7 KB" date="2023/11/29" icon="icons/image.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/sharkbg_l.jpg" >}}
{{< hoa-filetree/file name="sharkbg_r" type="jpg" size="11.2 KB" date="2023/11/29" icon="icons/image.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/fish_game/sharkbg_r.jpg" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="psp" date="" state="closed" >}}
{{< hoa-filetree/file name="创新训练课 B 报告-psp" type="pdf" size="875.1 KB" date="2025/06/28" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/psp/%E5%88%9B%E6%96%B0%E8%AE%AD%E7%BB%83%E8%AF%BEB%E6%8A%A5%E5%91%8A-psp.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/folder name="地铁站示例" date="" state="closed" >}}
{{< hoa-filetree/file name="Qt-创新训练题目 3" type="zip" size="10.8 MB" date="2023/11/29" icon="icons/zip.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/%E5%9C%B0%E9%93%81%E7%AB%99%E7%A4%BA%E4%BE%8B/Qt-%E5%88%9B%E6%96%B0%E8%AE%AD%E7%BB%83%E9%A2%98%E7%9B%AE3.zip" >}}
{{< hoa-filetree/file name="项目展示答辩" type="zip" size="24.0 MB" date="2023/11/29" icon="icons/zip.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/%E5%9C%B0%E9%93%81%E7%AB%99%E7%A4%BA%E4%BE%8B/%E9%A1%B9%E7%9B%AE%E5%B1%95%E7%A4%BA%E7%AD%94%E8%BE%A9.zip" >}}
{{< hoa-filetree/file name="黄继凡 - 创新训练课 B 报告" type="docx" size="1.6 MB" date="2023/11/29" icon="icons/docx.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/course_design/%E5%9C%B0%E9%93%81%E7%AB%99%E7%A4%BA%E4%BE%8B/%E9%BB%84%E7%BB%A7%E5%87%A1-%E5%88%9B%E6%96%B0%E8%AE%AD%E7%BB%83%E8%AF%BEB%E6%8A%A5%E5%91%8A.docx" >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/folder >}}
{{< hoa-filetree/file name="readme" type="toml" size="2.8 KB" date="2026/02/06" icon="icons/file.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/readme.toml" >}}
{{< hoa-filetree/folder name="slides" date="" state="closed" >}}
{{< hoa-filetree/file name="第 1 章 高级语言程序设计" type="pdf" size="2.4 MB" date="2023/12/01" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/slides/%E7%AC%AC1%E7%AB%A0%20%E9%AB%98%E7%BA%A7%E8%AF%AD%E8%A8%80%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1.pdf" >}}
{{< hoa-filetree/file name="第 2 章 可行性研究" type="pdf" size="885.0 KB" date="2023/12/01" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/slides/%E7%AC%AC2%E7%AB%A0%20%E5%8F%AF%E8%A1%8C%E6%80%A7%E7%A0%94%E7%A9%B6.pdf" >}}
{{< hoa-filetree/file name="第 3 章 需求分析" type="pdf" size="804.9 KB" date="2023/12/01" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/slides/%E7%AC%AC3%E7%AB%A0%20%E9%9C%80%E6%B1%82%E5%88%86%E6%9E%90.pdf" >}}
{{< hoa-filetree/file name="第 4 章 总体设计" type="pdf" size="188.2 KB" date="2023/12/01" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/slides/%E7%AC%AC4%E7%AB%A0%20%E6%80%BB%E4%BD%93%E8%AE%BE%E8%AE%A1.pdf" >}}
{{< hoa-filetree/file name="第 5 章 详细设计 1" type="pdf" size="327.5 KB" date="2023/12/01" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/slides/%E7%AC%AC5%E7%AB%A0%20%E8%AF%A6%E7%BB%86%E8%AE%BE%E8%AE%A11.pdf" >}}
{{< hoa-filetree/file name="第 6 章 实现" type="pdf" size="397.7 KB" date="2023/12/01" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/slides/%E7%AC%AC6%E7%AB%A0%20%E5%AE%9E%E7%8E%B0.pdf" >}}
{{< hoa-filetree/file name="第 7 章 维护" type="pdf" size="96.9 KB" date="2023/12/01" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/slides/%E7%AC%AC7%E7%AB%A0%20%E7%BB%B4%E6%8A%A4.pdf" >}}
{{< hoa-filetree/file name="课程设计题目" type="pdf" size="582.0 KB" date="2023/12/01" icon="icons/pdf.png" url="https://gh.hoa.moe/github.com/HITSZ-OpenAuto/AUTO2003B/raw/main/slides/%E8%AF%BE%E7%A8%8B%E8%AE%BE%E8%AE%A1%E9%A2%98%E7%9B%AE.pdf" >}}
{{< /hoa-filetree/folder >}}
{{< /hoa-filetree/container >}}

## 参与

《HITSZ 自动化课程攻略共享计划》是所有同学都可以参与编写的，如果你有好的笔记或者资料，欢迎前往我们的 [GitHub](https://github.com/HITSZ-OpenAuto) 进行参与，也可以发邮件至 [📮hi@hoa.moe](mailto:hi@hoa.moe) 联系我们，我们会在收到的第一时间进行答复。

{{< callout type="" >}}
  © 版权声明：[知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议](https://creativecommons.org/licenses/by-nc-sa/4.0/)
{{< /callout >}}

