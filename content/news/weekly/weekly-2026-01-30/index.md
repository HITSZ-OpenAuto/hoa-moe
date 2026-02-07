---
authors:
  - image: https://github.com/openai.png
    link: https://github.com/openai
    name: ChatGPT
date: "2026-02-06"
draft: false
excludeSearch: false
title: AUTO 周报 2026-01-30 - 2026-02-06
---

## 本周更新摘要

- 平台 / 工具 (HOA 系列)
  - hoa-toml：完善生成器与文档，新增教师评价表格、仓库徽章逻辑、README 从 TOML 生成等；整理仓库布局并规范化 Markdown/表格格式与 URL 处理。
  - hoa-prServer / hoa-backend：搭建 FastAPI JSON 服务骨架，加入 repo lookup/submit-to-PR、pending poller、docker 配置与模块文档；修复 CI/格式器与 shields.io 问题，并改进 Markdown 渲染与提交反馈。hoa-backend 新增 major-data 子模块并改进 semester 文件夹在 meta.json 中的排序。
  - hoa-fuma / hoa-blog / hoa-news：前端功能增强（中文搜索、主题跟随、i18n hideLocale、学期索引页与课程卡、新闻页、自动导航等），迁移 blog/news 内容到专用仓库并加入 LICENSE；多处布局与 CI 优化。
  - hoa-cli：重命名并精简命令，加入 grades_summary 支持（自动附加成绩构成细节）。
  - 其它：新增用于院系专业数据的 hoa-major-data 初始导入；repos-management 自动更新仓库列表。

- 新测试 / 示例仓库
  - TEST1001：（示例）大学物理实验 初始化并自动化生成/格式化 README（多次 CI 自动提交）。

- 课程资料与重要内容更新（精选）
  - 经济学原理 (ECON2005F)：课程介绍与讲义更新，新增教师评价与小组展示示例。
  - 微积分 B (MATH1015B)：更正教师姓名错字并增加先修内容说明；微积分 A/B 有合并/同步更新。
  - 工程训练（电子工艺实习）(ENGG1003)：增加开设学期信息（第二学年春季）。
  - 马克思主义基本原理 / 中国近现代史纲要：分别新增 2025 年考试信息。
  - 体育 (PE100X)：调整成绩构成并增加一门飞盘课描述。
  - 凸优化与最优控制 (AUTO5023)：补充结构化课程信息（AUTO5023.toml）。
  - 课程数据同步：hoa-major-data 中更新了 COMP3002 信息。

- CI / 自动化与批量维护
  - 大量仓库（覆盖多门课程）进行了 CI/workflow 优化、自动格式化 README/readme.toml、添加/更新自动化格式化与工作流（自动提交生成的 README），以及删除过时的 metadata/example 文件。
  - 许多课程仓库仅做了 README.md / readme.toml 的自动更新或格式化，属于例行维护。

- 其他杂项
  - 若干仓库进行了小幅代码/格式修复、路径调整或无意义文件删除，已在自动化清理中处理。

## 更新内容

### 周五 (2.6)

- GitHub Actions 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/TEST1001) 中提交了信息：ci: format toml & regenerate README [automated]

- Jiao Ziang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/TEST1001) 中提交了信息：Merge pull request #3 from HITSZ-OpenAuto/bot/rdme-20260205-175810

- hoa-prServer 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/TEST1001) 中提交了信息：chore: update TEST1001 readme.toml

- GitHub Actions 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/TEST1001) 中提交了信息：ci: format toml & regenerate README [automated]

- Jiao Ziang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/TEST1001) 中提交了信息：1

### 周四 (2.5)

- GitHub Actions 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/TEST1001) 中提交了信息：ci: format toml & regenerate README [automated]

- JLPL666 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/TEST1001) 中提交了信息：初始化测试仓库

- JLPL666 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/TEST1001) 中提交了信息：first commit

- Fun10165 在 [离散数学](https://github.com/HITSZ-OpenAuto/COMP2030) 中提交了信息：Merge pull request #13 from Fun10165/main

- Fun10165 在 [马克思主义基本原理](https://github.com/HITSZ-OpenAuto/GEIP1011) 中提交了信息：增加 25 秋考试信息 (#39)

- Fun10165 在 [中国近现代史纲要](https://github.com/HITSZ-OpenAuto/GEIP1016) 中提交了信息：增加 25 春考试信息 (#25)

- Fun10165 在 [微积分 A](https://github.com/HITSZ-OpenAuto/MATH1015A) 中提交了信息：Merge pull request #28 from Fun10165/main

- Fun10165 在 [微积分 B](https://github.com/HITSZ-OpenAuto/MATH1015B) 中提交了信息：更正老师名字中的错别字，增加微积分 B 先修内容 (#27)

- IcyDesert 在 [设计与制造 B](https://github.com/HITSZ-OpenAuto/MECH2020) 中提交了信息：Merge pull request #2 from HITSZ-OpenAuto/feat/files-movement

- Fun10165 在 [工程训练（电子工艺实习）](https://github.com/HITSZ-OpenAuto/ENGG1003) 中提交了信息：增加开设学期（第二学年春季） (#18)

- Jiao Ziang 在 [经济学原理](https://github.com/HITSZ-OpenAuto/ECON2005F) 中提交了信息：删除提交错误的">"符号

- Alexis 在 [经济学原理](https://github.com/HITSZ-OpenAuto/ECON2005F) 中提交了信息：增加了对老师的评价和小组展示的实例 (#20)

- Anastasia-Charies 在 [经济学原理](https://github.com/HITSZ-OpenAuto/ECON2005F) 中提交了信息：更新了经济学原理的课程介绍和讲义资料 (#15)

- 浮萍（混子）在 [大学物理](https://github.com/HITSZ-OpenAuto/PHYS1001) 中提交了信息：Merge pull request #33 from DUCKSEEDYHB/patch-1

- Junda Wu 在 [最优估计](https://github.com/HITSZ-OpenAuto/AUTO5013) 中提交了信息：Merge pull request #18 from HITSZ-OpenAuto/ow1

### 周三 (2.4)

- Jiao Ziang 在 [体育](https://github.com/HITSZ-OpenAuto/PE100X) 中提交了信息：Merge pull request #32 from SpeechlessPanda/patch-1

- Jiao Ziang 在 [跨专业选修课程体系](https://github.com/HITSZ-OpenAuto/CrossSpecialty) 中提交了信息：Merge pull request #23 from fruly-ZERO/main

### 周二 (2.3)

- Mingjia Zhou 在 [体育](https://github.com/HITSZ-OpenAuto/PE100X) 中提交了信息：Revise grading distribution and learning recommendations

- Mingjia Zhou 在 [体育](https://github.com/HITSZ-OpenAuto/PE100X) 中提交了信息：增加了对一门飞盘课的描述

### 周六 (1.31)

- fruly 在 [跨专业选修课程体系](https://github.com/HITSZ-OpenAuto/CrossSpecialty) 中提交了信息：docs: add course badges and description

- Kowyo 在 [设计与制造 B](https://github.com/HITSZ-OpenAuto/MECH2020) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#1)

- Kowyo 在 [设计与制造 C](https://github.com/HITSZ-OpenAuto/MECH3041) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#3)

- Kowyo 在 [机电系统控制基础](https://github.com/HITSZ-OpenAuto/MECH3005) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#3)

- Kowyo 在 [机器人学基础](https://github.com/HITSZ-OpenAuto/MECH3060) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#3)

- Kowyo 在 [计算机专业导论](https://github.com/HITSZ-OpenAuto/COMP2001) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#3)

- Kowyo 在 [电路与电子学 I](https://github.com/HITSZ-OpenAuto/EE1018) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#4)

- Kowyo 在 [新时代中国特色社会主义理论与实践](https://github.com/HITSZ-OpenAuto/GEIP4004) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#4)

- Kowyo 在 [专业综合实践](https://github.com/HITSZ-OpenAuto/EE304X) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#4)

- Kowyo 在 [深度学习体系结构](https://github.com/HITSZ-OpenAuto/COMP3043) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#7)

- Kowyo 在 [人工智能](https://github.com/HITSZ-OpenAuto/COMP3005) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#12)

- Kowyo 在 [智能证券投资](https://github.com/HITSZ-OpenAuto/COMP3042) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#12)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3039) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#8)

- Kowyo 在 [网络与系统安全](https://github.com/HITSZ-OpenAuto/COMP3054) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#11)

- Kowyo 在 [自然语言处理](https://github.com/HITSZ-OpenAuto/COMP3021) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#10)

- Kowyo 在 [计算机视觉](https://github.com/HITSZ-OpenAuto/COMP3029) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#9)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3019) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#8)

- Kowyo 在 [图像处理](https://github.com/HITSZ-OpenAuto/COMP3018) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#8)

- Kowyo 在 [服务计算](https://github.com/HITSZ-OpenAuto/COMP3017) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#10)

- Kowyo 在 [软件体系结构](https://github.com/HITSZ-OpenAuto/COMP3028) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#10)

- Kowyo 在 [信息检索](https://github.com/HITSZ-OpenAuto/COMP3030) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#9)

- Kowyo 在 [机器学习概论](https://github.com/HITSZ-OpenAuto/COMP3006) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#9)

- Kowyo 在 [汇编语言与接口技术](https://github.com/HITSZ-OpenAuto/COMP3053) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#8)

- Kowyo 在 [软件工程](https://github.com/HITSZ-OpenAuto/COMP3002) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#10)

- Kowyo 在 [大数据导论](https://github.com/HITSZ-OpenAuto/COMP3009) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#9)

- Kowyo 在 [计算机体系结构](https://github.com/HITSZ-OpenAuto/COMP3044) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#9)

- Kowyo 在 [模式识别](https://github.com/HITSZ-OpenAuto/COMP3007) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#10)

- Kowyo 在 [密码学基础](https://github.com/HITSZ-OpenAuto/COMP3040) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#9)

- Kowyo 在 [形式语言与自动机](https://github.com/HITSZ-OpenAuto/COMP3004) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#10)

- Kowyo 在 [计算机体系结构](https://github.com/HITSZ-OpenAuto/COMP3011) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#9)

- Kowyo 在 [近世代数](https://github.com/HITSZ-OpenAuto/COMP2010) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#10)

- Kowyo 在 [面向领域的计算机系统设计与开发实践](https://github.com/HITSZ-OpenAuto/COMP2029) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#10)

- Kowyo 在 [软件构造实践](https://github.com/HITSZ-OpenAuto/COMP3060) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#9)

- Kowyo 在 [数据库系统](https://github.com/HITSZ-OpenAuto/COMP3010) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#9)

- Kowyo 在 [编译原理](https://github.com/HITSZ-OpenAuto/COMP3013) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#10)

- Kowyo 在 [操作系统](https://github.com/HITSZ-OpenAuto/COMP3001) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#10)

- Kowyo 在 [软件构造](https://github.com/HITSZ-OpenAuto/COMP3059) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#13)

- Kowyo 在 [计算机设计与实践](https://github.com/HITSZ-OpenAuto/COMP2012) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#12)

- Kowyo 在 [计算机组成原理](https://github.com/HITSZ-OpenAuto/COMP2008) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#9)

- Kowyo 在 [数据结构与算法](https://github.com/HITSZ-OpenAuto/COMP2052) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#10)

- Kowyo 在 [计算机系统](https://github.com/HITSZ-OpenAuto/COMP3052) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#12)

- Kowyo 在 [数字逻辑设计](https://github.com/HITSZ-OpenAuto/COMP2051) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#18)

- Kowyo 在 [离散数学](https://github.com/HITSZ-OpenAuto/COMP2030) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#12)

- Kowyo 在 [优化算法](https://github.com/HITSZ-OpenAuto/MATH4002) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#8)

- Kowyo 在 [固体力学](https://github.com/HITSZ-OpenAuto/MECH2022) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#8)

- Kowyo 在 [设计与制造 A](https://github.com/HITSZ-OpenAuto/MECH2019) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#10)

- Kowyo 在 [电力电子技术](https://github.com/HITSZ-OpenAuto/EE3002) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#11)

- Kowyo 在 [电力系统分析](https://github.com/HITSZ-OpenAuto/EE3015) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#12)

- Kowyo 在 [电机学](https://github.com/HITSZ-OpenAuto/EE3001) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#13)

- Kowyo 在 [电磁场](https://github.com/HITSZ-OpenAuto/EE2003) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#12)

- Kowyo 在 [矩阵分析](https://github.com/HITSZ-OpenAuto/MATH4001) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#14)

- Kowyo 在 [习近平新时代中国特色社会主义思想概论](https://github.com/HITSZ-OpenAuto/GEIP1017) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#18)

- Kowyo 在 [思想道德与法治](https://github.com/HITSZ-OpenAuto/GEIP1015) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#16)

- Kowyo 在 [中国科技史话](https://github.com/HITSZ-OpenAuto/SEIN1040) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#13)

- Kowyo 在 [普通天文学](https://github.com/HITSZ-OpenAuto/SPST1004) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#15)

- Kowyo 在 [工程训练（金工实习）](https://github.com/HITSZ-OpenAuto/ENGG1002) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#15)

- Kowyo 在 [工程训练（电子工艺实习）](https://github.com/HITSZ-OpenAuto/ENGG1003) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#17)

- Kowyo 在 [高等电路与电子分析](https://github.com/HITSZ-OpenAuto/EE2004) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#18)

- Kowyo 在 [移动机器人导论](https://github.com/HITSZ-OpenAuto/AUTO3012) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#16)

- Kowyo 在 [写作与沟通](https://github.com/HITSZ-OpenAuto/WRIT0001) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#17)

- Kowyo 在 [机器学习概论](https://github.com/HITSZ-OpenAuto/AUTO3019) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#16)

- Kowyo 在 [日语 I](https://github.com/HITSZ-OpenAuto/WOCD1008) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#14)

- Kowyo 在 [运动控制系统](https://github.com/HITSZ-OpenAuto/AUTO3011) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#17)

- Kowyo 在 [模式识别](https://github.com/HITSZ-OpenAuto/AUTO5024) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#20)

- Kowyo 在 [嵌入式系统](https://github.com/HITSZ-OpenAuto/AUTO3024) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#17)

- Kowyo 在 [系统辨识](https://github.com/HITSZ-OpenAuto/AUTO5002) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#16)

- Kowyo 在 [线性系统理论](https://github.com/HITSZ-OpenAuto/AUTO5001) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#18)

- Kowyo 在 [机器视觉](https://github.com/HITSZ-OpenAuto/AUTO3006) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#23)

- Kowyo 在 [凸优化与最优控制](https://github.com/HITSZ-OpenAuto/AUTO5023) 中提交了信息：ci: remove AUTO5023.toml (#21)

- Kowyo 在 [电路与电子技术实验](https://github.com/HITSZ-OpenAuto/EE1014) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#20)

- Kowyo 在 [电路与电子学](https://github.com/HITSZ-OpenAuto/EE1013) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#23)

- Kowyo 在 [电路 IA](https://github.com/HITSZ-OpenAuto/EE1011A) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#23)

- Kowyo 在 [自动控制理论 A](https://github.com/HITSZ-OpenAuto/AUTO3001A) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#36)

- Kowyo 在 [自动化领域专家系列讲座](https://github.com/HITSZ-OpenAuto/AUTO3022) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#19)

- Kowyo 在 [机械设计基础](https://github.com/HITSZ-OpenAuto/MECH2010) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#20)

- Kowyo 在 [微积分 B](https://github.com/HITSZ-OpenAuto/MATH1015B) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#26)

- Kowyo 在 [电路实验 IA](https://github.com/HITSZ-OpenAuto/EE1012A) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#19)

- Kowyo 在 [大学英语](https://github.com/HITSZ-OpenAuto/LANG100X) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#21)

- Kowyo 在 [大学物理](https://github.com/HITSZ-OpenAuto/PHYS1001) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#32)

- Kowyo 在 [电路实验 IB](https://github.com/HITSZ-OpenAuto/EE1012B) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#20)

- Kowyo 在 [经济学原理](https://github.com/HITSZ-OpenAuto/ECON2005F) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#22)

- Kowyo 在 [理论力学Ⅱ](https://github.com/HITSZ-OpenAuto/EMEC1002) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#23)

- Kowyo 在 [毛泽东思想和中国特色社会主义理论体系概论](https://github.com/HITSZ-OpenAuto/GEIP1018) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#24)

- Kowyo 在 [模拟电子技术实验](https://github.com/HITSZ-OpenAuto/EE1008) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#20)

- Kowyo 在 [数字电子技术实验](https://github.com/HITSZ-OpenAuto/EE1010) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#20)

- Kowyo 在 [控制理论中的代数基础](https://github.com/HITSZ-OpenAuto/AUTO2006) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#23)

- Kowyo 在 [DSP 的原理与应用](https://github.com/HITSZ-OpenAuto/EE3005) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#18)

- Kowyo 在 [代数与几何](https://github.com/HITSZ-OpenAuto/MATH1002) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#32)

- Kowyo 在 [自动控制实践 A 实验](https://github.com/HITSZ-OpenAuto/AUTO3016) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#29)

- Kowyo 在 [C++ 语言程序设计](https://github.com/HITSZ-OpenAuto/COMP2014) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#20)

- Kowyo 在 [程序设计思维与实践](https://github.com/HITSZ-OpenAuto/COMP1011) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#24)

- Kowyo 在 [数学规划与数值优化](https://github.com/HITSZ-OpenAuto/AUTO3028) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#21)

- Kowyo 在 [数据结构与算法](https://github.com/HITSZ-OpenAuto/COMP2050) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#20)

- Kowyo 在 [概率论与数理统计](https://github.com/HITSZ-OpenAuto/MATH1004) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#37)

- Kowyo 在 [数字图像处理](https://github.com/HITSZ-OpenAuto/AUTO3003) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#30)

- Kowyo 在 [信号分析与处理](https://github.com/HITSZ-OpenAuto/AUTO2005) 中提交了信息：ci: remove AUTO2005.toml (#39)

- Kowyo 在 [大学化学 III](https://github.com/HITSZ-OpenAuto/CHEM1012) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#21)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/course-template) 中提交了信息：ci: remove readme.yaml (#24)

- Kowyo 在 [大学物理实验](https://github.com/HITSZ-OpenAuto/PHYS1002) 中提交了信息：[automated-generated-PR] ci: remove obsolete metadata/example files (#67)

- Jiao Ziang 在 [运动控制系统](https://github.com/HITSZ-OpenAuto/AUTO3011) 中提交了信息：ci: Add automatic format and update workflow for normal repos

- Jiao Ziang 在 [机器视觉](https://github.com/HITSZ-OpenAuto/AUTO3006) 中提交了信息：ci: Add automatic format and update workflow for normal repos

- Jiao Ziang 在 [数字图像处理](https://github.com/HITSZ-OpenAuto/AUTO3003) 中提交了信息：ci: Add automatic format and update workflow for normal repos

- Jiao Ziang 在 [自动控制理论 A](https://github.com/HITSZ-OpenAuto/AUTO3001A) 中提交了信息：ci: Add automatic format and update workflow for normal repos

- Jiao Ziang 在 [控制理论中的代数基础](https://github.com/HITSZ-OpenAuto/AUTO2006) 中提交了信息：ci: Add automatic format and update workflow for normal repos

- Jiao Ziang 在 [自动控制理论 A](https://github.com/HITSZ-OpenAuto/AUTO3001A) 中提交了信息：ci: Add automatic format and update workflow for normal repos

- Jiao Ziang 在 [控制理论中的代数基础](https://github.com/HITSZ-OpenAuto/AUTO2006) 中提交了信息：ci: Add automatic format and update workflow for normal repos

- Jiao Ziang 在 [写作与沟通](https://github.com/HITSZ-OpenAuto/WRIT0001) 中提交了信息：Update README.md for WRIT0001

- Jiao Ziang 在 [写作与沟通](https://github.com/HITSZ-OpenAuto/WRIT0001) 中提交了信息：Update readme.toml for WRIT0001

- Jiao Ziang 在 [日语 I](https://github.com/HITSZ-OpenAuto/WOCD1008) 中提交了信息：Update README.md for WOCD1008

- Jiao Ziang 在 [日语 I](https://github.com/HITSZ-OpenAuto/WOCD1008) 中提交了信息：Update readme.toml for WOCD1008

- Jiao Ziang 在 [普通天文学](https://github.com/HITSZ-OpenAuto/SPST1004) 中提交了信息：Update README.md for SPST1004

- Jiao Ziang 在 [普通天文学](https://github.com/HITSZ-OpenAuto/SPST1004) 中提交了信息：Update readme.toml for SPST1004

- Jiao Ziang 在 [中国科技史话](https://github.com/HITSZ-OpenAuto/SEIN1040) 中提交了信息：Update README.md for SEIN1040

- Jiao Ziang 在 [中国科技史话](https://github.com/HITSZ-OpenAuto/SEIN1040) 中提交了信息：Update readme.toml for SEIN1040

- Jiao Ziang 在 [大学物理实验](https://github.com/HITSZ-OpenAuto/PHYS1002) 中提交了信息：Update README.md for PHYS1002

- Jiao Ziang 在 [大学物理实验](https://github.com/HITSZ-OpenAuto/PHYS1002) 中提交了信息：Update readme.toml for PHYS1002

- Jiao Ziang 在 [大学物理](https://github.com/HITSZ-OpenAuto/PHYS1001) 中提交了信息：Update README.md for PHYS1001

- Jiao Ziang 在 [大学物理](https://github.com/HITSZ-OpenAuto/PHYS1001) 中提交了信息：Update readme.toml for PHYS1001

- Jiao Ziang 在 [机器人学基础](https://github.com/HITSZ-OpenAuto/MECH3060) 中提交了信息：Update README.md for MECH3060

- Jiao Ziang 在 [机器人学基础](https://github.com/HITSZ-OpenAuto/MECH3060) 中提交了信息：Update readme.toml for MECH3060

- Jiao Ziang 在 [设计与制造 C](https://github.com/HITSZ-OpenAuto/MECH3041) 中提交了信息：Update README.md for MECH3041

- Jiao Ziang 在 [设计与制造 C](https://github.com/HITSZ-OpenAuto/MECH3041) 中提交了信息：Update readme.toml for MECH3041

- Jiao Ziang 在 [机电系统控制基础](https://github.com/HITSZ-OpenAuto/MECH3005) 中提交了信息：Update README.md for MECH3005

- Jiao Ziang 在 [机电系统控制基础](https://github.com/HITSZ-OpenAuto/MECH3005) 中提交了信息：Update readme.toml for MECH3005

- Jiao Ziang 在 [固体力学](https://github.com/HITSZ-OpenAuto/MECH2022) 中提交了信息：Update README.md for MECH2022

- Jiao Ziang 在 [固体力学](https://github.com/HITSZ-OpenAuto/MECH2022) 中提交了信息：Update readme.toml for MECH2022

- Jiao Ziang 在 [设计与制造 B](https://github.com/HITSZ-OpenAuto/MECH2020) 中提交了信息：Update README.md for MECH2020

- Jiao Ziang 在 [设计与制造 B](https://github.com/HITSZ-OpenAuto/MECH2020) 中提交了信息：Update readme.toml for MECH2020

- Jiao Ziang 在 [设计与制造 A](https://github.com/HITSZ-OpenAuto/MECH2019) 中提交了信息：Update README.md for MECH2019

- Jiao Ziang 在 [设计与制造 A](https://github.com/HITSZ-OpenAuto/MECH2019) 中提交了信息：Update readme.toml for MECH2019

- Jiao Ziang 在 [机械设计基础](https://github.com/HITSZ-OpenAuto/MECH2010) 中提交了信息：Update README.md for MECH2010

- Jiao Ziang 在 [机械设计基础](https://github.com/HITSZ-OpenAuto/MECH2010) 中提交了信息：Update readme.toml for MECH2010

- Jiao Ziang 在 [优化算法](https://github.com/HITSZ-OpenAuto/MATH4002) 中提交了信息：Update README.md for MATH4002

- Jiao Ziang 在 [优化算法](https://github.com/HITSZ-OpenAuto/MATH4002) 中提交了信息：Update readme.toml for MATH4002

- Jiao Ziang 在 [矩阵分析](https://github.com/HITSZ-OpenAuto/MATH4001) 中提交了信息：Update README.md for MATH4001

- Jiao Ziang 在 [矩阵分析](https://github.com/HITSZ-OpenAuto/MATH4001) 中提交了信息：Update readme.toml for MATH4001

- Jiao Ziang 在 [微积分 B](https://github.com/HITSZ-OpenAuto/MATH1015B) 中提交了信息：Update README.md for MATH1015B

- Jiao Ziang 在 [微积分 B](https://github.com/HITSZ-OpenAuto/MATH1015B) 中提交了信息：Update readme.toml for MATH1015B

- Jiao Ziang 在 [概率论与数理统计](https://github.com/HITSZ-OpenAuto/MATH1004) 中提交了信息：Update README.md for MATH1004

- Jiao Ziang 在 [概率论与数理统计](https://github.com/HITSZ-OpenAuto/MATH1004) 中提交了信息：Update readme.toml for MATH1004

- Jiao Ziang 在 [代数与几何](https://github.com/HITSZ-OpenAuto/MATH1002) 中提交了信息：Update README.md for MATH1002

- Jiao Ziang 在 [代数与几何](https://github.com/HITSZ-OpenAuto/MATH1002) 中提交了信息：Update readme.toml for MATH1002

- Jiao Ziang 在 [大学英语](https://github.com/HITSZ-OpenAuto/LANG100X) 中提交了信息：Update README.md for LANG100X

- Jiao Ziang 在 [大学英语](https://github.com/HITSZ-OpenAuto/LANG100X) 中提交了信息：Update readme.toml for LANG100X

- Jiao Ziang 在 [新时代中国特色社会主义理论与实践](https://github.com/HITSZ-OpenAuto/GEIP4004) 中提交了信息：Update README.md for GEIP4004

- Jiao Ziang 在 [新时代中国特色社会主义理论与实践](https://github.com/HITSZ-OpenAuto/GEIP4004) 中提交了信息：Update readme.toml for GEIP4004

- Jiao Ziang 在 [毛泽东思想和中国特色社会主义理论体系概论](https://github.com/HITSZ-OpenAuto/GEIP1018) 中提交了信息：Update README.md for GEIP1018

- Jiao Ziang 在 [毛泽东思想和中国特色社会主义理论体系概论](https://github.com/HITSZ-OpenAuto/GEIP1018) 中提交了信息：Update readme.toml for GEIP1018

- Jiao Ziang 在 [习近平新时代中国特色社会主义思想概论](https://github.com/HITSZ-OpenAuto/GEIP1017) 中提交了信息：Update README.md for GEIP1017

- Jiao Ziang 在 [习近平新时代中国特色社会主义思想概论](https://github.com/HITSZ-OpenAuto/GEIP1017) 中提交了信息：Update readme.toml for GEIP1017

- Jiao Ziang 在 [思想道德与法治](https://github.com/HITSZ-OpenAuto/GEIP1015) 中提交了信息：Update README.md for GEIP1015

- Jiao Ziang 在 [思想道德与法治](https://github.com/HITSZ-OpenAuto/GEIP1015) 中提交了信息：Update readme.toml for GEIP1015

- Jiao Ziang 在 [工程训练（电子工艺实习）](https://github.com/HITSZ-OpenAuto/ENGG1003) 中提交了信息：Update README.md for ENGG1003

- Jiao Ziang 在 [工程训练（电子工艺实习）](https://github.com/HITSZ-OpenAuto/ENGG1003) 中提交了信息：Update readme.toml for ENGG1003

- Jiao Ziang 在 [工程训练（金工实习）](https://github.com/HITSZ-OpenAuto/ENGG1002) 中提交了信息：Update README.md for ENGG1002

- Jiao Ziang 在 [工程训练（金工实习）](https://github.com/HITSZ-OpenAuto/ENGG1002) 中提交了信息：Update readme.toml for ENGG1002

- Jiao Ziang 在 [理论力学Ⅱ](https://github.com/HITSZ-OpenAuto/EMEC1002) 中提交了信息：Update README.md for EMEC1002

- Jiao Ziang 在 [理论力学Ⅱ](https://github.com/HITSZ-OpenAuto/EMEC1002) 中提交了信息：Update readme.toml for EMEC1002

- Jiao Ziang 在 [专业综合实践](https://github.com/HITSZ-OpenAuto/EE304X) 中提交了信息：Update README.md for EE304X

- Jiao Ziang 在 [专业综合实践](https://github.com/HITSZ-OpenAuto/EE304X) 中提交了信息：Update readme.toml for EE304X

- Jiao Ziang 在 [电力系统分析](https://github.com/HITSZ-OpenAuto/EE3015) 中提交了信息：Update README.md for EE3015

- Jiao Ziang 在 [电力系统分析](https://github.com/HITSZ-OpenAuto/EE3015) 中提交了信息：Update readme.toml for EE3015

- Jiao Ziang 在 [DSP 的原理与应用](https://github.com/HITSZ-OpenAuto/EE3005) 中提交了信息：Update README.md for EE3005

- Jiao Ziang 在 [DSP 的原理与应用](https://github.com/HITSZ-OpenAuto/EE3005) 中提交了信息：Update readme.toml for EE3005

- Jiao Ziang 在 [电力电子技术](https://github.com/HITSZ-OpenAuto/EE3002) 中提交了信息：Update README.md for EE3002

- Jiao Ziang 在 [电力电子技术](https://github.com/HITSZ-OpenAuto/EE3002) 中提交了信息：Update readme.toml for EE3002

- Jiao Ziang 在 [电机学](https://github.com/HITSZ-OpenAuto/EE3001) 中提交了信息：Update README.md for EE3001

- Jiao Ziang 在 [电机学](https://github.com/HITSZ-OpenAuto/EE3001) 中提交了信息：Update readme.toml for EE3001

- Jiao Ziang 在 [高等电路与电子分析](https://github.com/HITSZ-OpenAuto/EE2004) 中提交了信息：Update README.md for EE2004

- Jiao Ziang 在 [高等电路与电子分析](https://github.com/HITSZ-OpenAuto/EE2004) 中提交了信息：Update readme.toml for EE2004

- Jiao Ziang 在 [电磁场](https://github.com/HITSZ-OpenAuto/EE2003) 中提交了信息：Update README.md for EE2003

- Jiao Ziang 在 [电磁场](https://github.com/HITSZ-OpenAuto/EE2003) 中提交了信息：Update readme.toml for EE2003

- Jiao Ziang 在 [电路与电子学 I](https://github.com/HITSZ-OpenAuto/EE1018) 中提交了信息：Update README.md for EE1018

- Jiao Ziang 在 [电路与电子学 I](https://github.com/HITSZ-OpenAuto/EE1018) 中提交了信息：Update readme.toml for EE1018

- Jiao Ziang 在 [电路与电子技术实验](https://github.com/HITSZ-OpenAuto/EE1014) 中提交了信息：Update README.md for EE1014

- Jiao Ziang 在 [电路与电子技术实验](https://github.com/HITSZ-OpenAuto/EE1014) 中提交了信息：Update readme.toml for EE1014

- Jiao Ziang 在 [电路与电子学](https://github.com/HITSZ-OpenAuto/EE1013) 中提交了信息：Update README.md for EE1013

- Jiao Ziang 在 [电路与电子学](https://github.com/HITSZ-OpenAuto/EE1013) 中提交了信息：Update readme.toml for EE1013

- Jiao Ziang 在 [电路实验 IB](https://github.com/HITSZ-OpenAuto/EE1012B) 中提交了信息：Update README.md for EE1012B

- Jiao Ziang 在 [电路实验 IB](https://github.com/HITSZ-OpenAuto/EE1012B) 中提交了信息：Update readme.toml for EE1012B

- Jiao Ziang 在 [电路实验 IA](https://github.com/HITSZ-OpenAuto/EE1012A) 中提交了信息：Update README.md for EE1012A

- Jiao Ziang 在 [电路实验 IA](https://github.com/HITSZ-OpenAuto/EE1012A) 中提交了信息：Update readme.toml for EE1012A

- Jiao Ziang 在 [电路 IA](https://github.com/HITSZ-OpenAuto/EE1011A) 中提交了信息：Update README.md for EE1011A

- Jiao Ziang 在 [电路 IA](https://github.com/HITSZ-OpenAuto/EE1011A) 中提交了信息：Update readme.toml for EE1011A

- Jiao Ziang 在 [数字电子技术实验](https://github.com/HITSZ-OpenAuto/EE1010) 中提交了信息：Update README.md for EE1010

- Jiao Ziang 在 [数字电子技术实验](https://github.com/HITSZ-OpenAuto/EE1010) 中提交了信息：Update readme.toml for EE1010

- Jiao Ziang 在 [模拟电子技术实验](https://github.com/HITSZ-OpenAuto/EE1008) 中提交了信息：Update README.md for EE1008

- Jiao Ziang 在 [模拟电子技术实验](https://github.com/HITSZ-OpenAuto/EE1008) 中提交了信息：Update readme.toml for EE1008

- Jiao Ziang 在 [经济学原理](https://github.com/HITSZ-OpenAuto/ECON2005F) 中提交了信息：Update README.md for ECON2005F

- Jiao Ziang 在 [经济学原理](https://github.com/HITSZ-OpenAuto/ECON2005F) 中提交了信息：Update readme.toml for ECON2005F

- Jiao Ziang 在 [软件构造实践](https://github.com/HITSZ-OpenAuto/COMP3060) 中提交了信息：Update README.md for COMP3060

- Jiao Ziang 在 [软件构造实践](https://github.com/HITSZ-OpenAuto/COMP3060) 中提交了信息：Update readme.toml for COMP3060

- Jiao Ziang 在 [软件构造](https://github.com/HITSZ-OpenAuto/COMP3059) 中提交了信息：Update README.md for COMP3059

- Jiao Ziang 在 [软件构造](https://github.com/HITSZ-OpenAuto/COMP3059) 中提交了信息：Update readme.toml for COMP3059

- Jiao Ziang 在 [网络与系统安全](https://github.com/HITSZ-OpenAuto/COMP3054) 中提交了信息：Update README.md for COMP3054

- Jiao Ziang 在 [网络与系统安全](https://github.com/HITSZ-OpenAuto/COMP3054) 中提交了信息：Update readme.toml for COMP3054

- Jiao Ziang 在 [汇编语言与接口技术](https://github.com/HITSZ-OpenAuto/COMP3053) 中提交了信息：Update README.md for COMP3053

- Jiao Ziang 在 [汇编语言与接口技术](https://github.com/HITSZ-OpenAuto/COMP3053) 中提交了信息：Update readme.toml for COMP3053

- Jiao Ziang 在 [计算机系统](https://github.com/HITSZ-OpenAuto/COMP3052) 中提交了信息：Update README.md for COMP3052

- Jiao Ziang 在 [计算机系统](https://github.com/HITSZ-OpenAuto/COMP3052) 中提交了信息：Update readme.toml for COMP3052

- Jiao Ziang 在 [计算机体系结构](https://github.com/HITSZ-OpenAuto/COMP3044) 中提交了信息：Update README.md for COMP3044

- Jiao Ziang 在 [计算机体系结构](https://github.com/HITSZ-OpenAuto/COMP3044) 中提交了信息：Update readme.toml for COMP3044

- Jiao Ziang 在 [深度学习体系结构](https://github.com/HITSZ-OpenAuto/COMP3043) 中提交了信息：Update README.md for COMP3043

- Jiao Ziang 在 [深度学习体系结构](https://github.com/HITSZ-OpenAuto/COMP3043) 中提交了信息：Update readme.toml for COMP3043

- Jiao Ziang 在 [智能证券投资](https://github.com/HITSZ-OpenAuto/COMP3042) 中提交了信息：Update README.md for COMP3042

- Jiao Ziang 在 [智能证券投资](https://github.com/HITSZ-OpenAuto/COMP3042) 中提交了信息：Update readme.toml for COMP3042

- Jiao Ziang 在 [密码学基础](https://github.com/HITSZ-OpenAuto/COMP3040) 中提交了信息：Update README.md for COMP3040

- Jiao Ziang 在 [密码学基础](https://github.com/HITSZ-OpenAuto/COMP3040) 中提交了信息：Update readme.toml for COMP3040

- Jiao Ziang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3039) 中提交了信息：Update README.md for COMP3039

- Jiao Ziang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3039) 中提交了信息：Update readme.toml for COMP3039

- Jiao Ziang 在 [信息检索](https://github.com/HITSZ-OpenAuto/COMP3030) 中提交了信息：Update README.md for COMP3030

- Jiao Ziang 在 [信息检索](https://github.com/HITSZ-OpenAuto/COMP3030) 中提交了信息：Update readme.toml for COMP3030

- Jiao Ziang 在 [计算机视觉](https://github.com/HITSZ-OpenAuto/COMP3029) 中提交了信息：Update README.md for COMP3029

- Jiao Ziang 在 [计算机视觉](https://github.com/HITSZ-OpenAuto/COMP3029) 中提交了信息：Update readme.toml for COMP3029

- Jiao Ziang 在 [软件体系结构](https://github.com/HITSZ-OpenAuto/COMP3028) 中提交了信息：Update README.md for COMP3028

- Jiao Ziang 在 [软件体系结构](https://github.com/HITSZ-OpenAuto/COMP3028) 中提交了信息：Update readme.toml for COMP3028

- Jiao Ziang 在 [自然语言处理](https://github.com/HITSZ-OpenAuto/COMP3021) 中提交了信息：Update README.md for COMP3021

- Jiao Ziang 在 [自然语言处理](https://github.com/HITSZ-OpenAuto/COMP3021) 中提交了信息：Update readme.toml for COMP3021

- Jiao Ziang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3019) 中提交了信息：Update README.md for COMP3019

- Jiao Ziang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3019) 中提交了信息：Update readme.toml for COMP3019

- Jiao Ziang 在 [图像处理](https://github.com/HITSZ-OpenAuto/COMP3018) 中提交了信息：Update README.md for COMP3018

- Jiao Ziang 在 [图像处理](https://github.com/HITSZ-OpenAuto/COMP3018) 中提交了信息：Update readme.toml for COMP3018

- Jiao Ziang 在 [服务计算](https://github.com/HITSZ-OpenAuto/COMP3017) 中提交了信息：Update README.md for COMP3017

- Jiao Ziang 在 [服务计算](https://github.com/HITSZ-OpenAuto/COMP3017) 中提交了信息：Update readme.toml for COMP3017

- Jiao Ziang 在 [编译原理](https://github.com/HITSZ-OpenAuto/COMP3013) 中提交了信息：Update README.md for COMP3013

- Jiao Ziang 在 [编译原理](https://github.com/HITSZ-OpenAuto/COMP3013) 中提交了信息：Update readme.toml for COMP3013

- Jiao Ziang 在 [计算机体系结构](https://github.com/HITSZ-OpenAuto/COMP3011) 中提交了信息：Update README.md for COMP3011

- Jiao Ziang 在 [计算机体系结构](https://github.com/HITSZ-OpenAuto/COMP3011) 中提交了信息：Update readme.toml for COMP3011

- Jiao Ziang 在 [数据库系统](https://github.com/HITSZ-OpenAuto/COMP3010) 中提交了信息：Update README.md for COMP3010

- Jiao Ziang 在 [数据库系统](https://github.com/HITSZ-OpenAuto/COMP3010) 中提交了信息：Update readme.toml for COMP3010

- Jiao Ziang 在 [大数据导论](https://github.com/HITSZ-OpenAuto/COMP3009) 中提交了信息：Update README.md for COMP3009

- Jiao Ziang 在 [大数据导论](https://github.com/HITSZ-OpenAuto/COMP3009) 中提交了信息：Update readme.toml for COMP3009

- Jiao Ziang 在 [模式识别](https://github.com/HITSZ-OpenAuto/COMP3007) 中提交了信息：Update README.md for COMP3007

- Jiao Ziang 在 [模式识别](https://github.com/HITSZ-OpenAuto/COMP3007) 中提交了信息：Update readme.toml for COMP3007

- Jiao Ziang 在 [机器学习概论](https://github.com/HITSZ-OpenAuto/COMP3006) 中提交了信息：Update README.md for COMP3006

- Jiao Ziang 在 [机器学习概论](https://github.com/HITSZ-OpenAuto/COMP3006) 中提交了信息：Update readme.toml for COMP3006

- Jiao Ziang 在 [人工智能](https://github.com/HITSZ-OpenAuto/COMP3005) 中提交了信息：Update README.md for COMP3005

- Jiao Ziang 在 [人工智能](https://github.com/HITSZ-OpenAuto/COMP3005) 中提交了信息：Update readme.toml for COMP3005

- Jiao Ziang 在 [形式语言与自动机](https://github.com/HITSZ-OpenAuto/COMP3004) 中提交了信息：Update README.md for COMP3004

- Jiao Ziang 在 [形式语言与自动机](https://github.com/HITSZ-OpenAuto/COMP3004) 中提交了信息：Update readme.toml for COMP3004

- Jiao Ziang 在 [软件工程](https://github.com/HITSZ-OpenAuto/COMP3002) 中提交了信息：Update README.md for COMP3002

- Jiao Ziang 在 [软件工程](https://github.com/HITSZ-OpenAuto/COMP3002) 中提交了信息：Update readme.toml for COMP3002

- Jiao Ziang 在 [操作系统](https://github.com/HITSZ-OpenAuto/COMP3001) 中提交了信息：Update README.md for COMP3001

- Jiao Ziang 在 [操作系统](https://github.com/HITSZ-OpenAuto/COMP3001) 中提交了信息：Update readme.toml for COMP3001

- Jiao Ziang 在 [数据结构与算法](https://github.com/HITSZ-OpenAuto/COMP2052) 中提交了信息：Update README.md for COMP2052

- Jiao Ziang 在 [数据结构与算法](https://github.com/HITSZ-OpenAuto/COMP2052) 中提交了信息：Update readme.toml for COMP2052

- Jiao Ziang 在 [数字逻辑设计](https://github.com/HITSZ-OpenAuto/COMP2051) 中提交了信息：Update README.md for COMP2051

- Jiao Ziang 在 [数字逻辑设计](https://github.com/HITSZ-OpenAuto/COMP2051) 中提交了信息：Update readme.toml for COMP2051

- Jiao Ziang 在 [数据结构与算法](https://github.com/HITSZ-OpenAuto/COMP2050) 中提交了信息：Update README.md for COMP2050

- Jiao Ziang 在 [数据结构与算法](https://github.com/HITSZ-OpenAuto/COMP2050) 中提交了信息：Update readme.toml for COMP2050

- Jiao Ziang 在 [离散数学](https://github.com/HITSZ-OpenAuto/COMP2030) 中提交了信息：Update README.md for COMP2030

- Jiao Ziang 在 [离散数学](https://github.com/HITSZ-OpenAuto/COMP2030) 中提交了信息：Update readme.toml for COMP2030

- Jiao Ziang 在 [面向领域的计算机系统设计与开发实践](https://github.com/HITSZ-OpenAuto/COMP2029) 中提交了信息：Update README.md for COMP2029

- Jiao Ziang 在 [面向领域的计算机系统设计与开发实践](https://github.com/HITSZ-OpenAuto/COMP2029) 中提交了信息：Update readme.toml for COMP2029

- Jiao Ziang 在 [C++ 语言程序设计](https://github.com/HITSZ-OpenAuto/COMP2014) 中提交了信息：Update README.md for COMP2014

- Jiao Ziang 在 [C++ 语言程序设计](https://github.com/HITSZ-OpenAuto/COMP2014) 中提交了信息：Update readme.toml for COMP2014

- Jiao Ziang 在 [计算机设计与实践](https://github.com/HITSZ-OpenAuto/COMP2012) 中提交了信息：Update README.md for COMP2012

- Jiao Ziang 在 [计算机设计与实践](https://github.com/HITSZ-OpenAuto/COMP2012) 中提交了信息：Update readme.toml for COMP2012

- Jiao Ziang 在 [近世代数](https://github.com/HITSZ-OpenAuto/COMP2010) 中提交了信息：Update README.md for COMP2010

- Jiao Ziang 在 [近世代数](https://github.com/HITSZ-OpenAuto/COMP2010) 中提交了信息：Update readme.toml for COMP2010

- Jiao Ziang 在 [计算机组成原理](https://github.com/HITSZ-OpenAuto/COMP2008) 中提交了信息：Update README.md for COMP2008

- Jiao Ziang 在 [计算机组成原理](https://github.com/HITSZ-OpenAuto/COMP2008) 中提交了信息：Update readme.toml for COMP2008

- Jiao Ziang 在 [计算机专业导论](https://github.com/HITSZ-OpenAuto/COMP2001) 中提交了信息：Update README.md for COMP2001

- Jiao Ziang 在 [计算机专业导论](https://github.com/HITSZ-OpenAuto/COMP2001) 中提交了信息：Update readme.toml for COMP2001

- Jiao Ziang 在 [程序设计思维与实践](https://github.com/HITSZ-OpenAuto/COMP1011) 中提交了信息：Update README.md for COMP1011

- Jiao Ziang 在 [程序设计思维与实践](https://github.com/HITSZ-OpenAuto/COMP1011) 中提交了信息：Update readme.toml for COMP1011

- Jiao Ziang 在 [大学化学 III](https://github.com/HITSZ-OpenAuto/CHEM1012) 中提交了信息：Update README.md for CHEM1012

- Jiao Ziang 在 [大学化学 III](https://github.com/HITSZ-OpenAuto/CHEM1012) 中提交了信息：Update readme.toml for CHEM1012

- Jiao Ziang 在 [模式识别](https://github.com/HITSZ-OpenAuto/AUTO5024) 中提交了信息：Update README.md for AUTO5024

- Jiao Ziang 在 [模式识别](https://github.com/HITSZ-OpenAuto/AUTO5024) 中提交了信息：Update readme.toml for AUTO5024

- Jiao Ziang 在 [系统辨识](https://github.com/HITSZ-OpenAuto/AUTO5002) 中提交了信息：Update README.md for AUTO5002

- Jiao Ziang 在 [系统辨识](https://github.com/HITSZ-OpenAuto/AUTO5002) 中提交了信息：Update readme.toml for AUTO5002

- Jiao Ziang 在 [线性系统理论](https://github.com/HITSZ-OpenAuto/AUTO5001) 中提交了信息：Update README.md for AUTO5001

- Jiao Ziang 在 [线性系统理论](https://github.com/HITSZ-OpenAuto/AUTO5001) 中提交了信息：Update readme.toml for AUTO5001

- Jiao Ziang 在 [数学规划与数值优化](https://github.com/HITSZ-OpenAuto/AUTO3028) 中提交了信息：Update README.md for AUTO3028

- Jiao Ziang 在 [数学规划与数值优化](https://github.com/HITSZ-OpenAuto/AUTO3028) 中提交了信息：Update readme.toml for AUTO3028

- Jiao Ziang 在 [嵌入式系统](https://github.com/HITSZ-OpenAuto/AUTO3024) 中提交了信息：Update README.md for AUTO3024

- Jiao Ziang 在 [嵌入式系统](https://github.com/HITSZ-OpenAuto/AUTO3024) 中提交了信息：Update readme.toml for AUTO3024

- Jiao Ziang 在 [自动化领域专家系列讲座](https://github.com/HITSZ-OpenAuto/AUTO3022) 中提交了信息：Update README.md for AUTO3022

- Jiao Ziang 在 [自动化领域专家系列讲座](https://github.com/HITSZ-OpenAuto/AUTO3022) 中提交了信息：Update readme.toml for AUTO3022

- Jiao Ziang 在 [机器学习概论](https://github.com/HITSZ-OpenAuto/AUTO3019) 中提交了信息：Update README.md for AUTO3019

- Jiao Ziang 在 [机器学习概论](https://github.com/HITSZ-OpenAuto/AUTO3019) 中提交了信息：Update readme.toml for AUTO3019

- Jiao Ziang 在 [自动控制实践 A 实验](https://github.com/HITSZ-OpenAuto/AUTO3016) 中提交了信息：Update README.md for AUTO3016

- Jiao Ziang 在 [自动控制实践 A 实验](https://github.com/HITSZ-OpenAuto/AUTO3016) 中提交了信息：Update readme.toml for AUTO3016

- Jiao Ziang 在 [移动机器人导论](https://github.com/HITSZ-OpenAuto/AUTO3012) 中提交了信息：Update README.md for AUTO3012

- Jiao Ziang 在 [移动机器人导论](https://github.com/HITSZ-OpenAuto/AUTO3012) 中提交了信息：Update readme.toml for AUTO3012

- Jiao Ziang 在 [运动控制系统](https://github.com/HITSZ-OpenAuto/AUTO3011) 中提交了信息：Update README.md for AUTO3011

- Jiao Ziang 在 [运动控制系统](https://github.com/HITSZ-OpenAuto/AUTO3011) 中提交了信息：Update readme.toml for AUTO3011

- Jiao Ziang 在 [机器视觉](https://github.com/HITSZ-OpenAuto/AUTO3006) 中提交了信息：Update README.md for AUTO3006

- Jiao Ziang 在 [机器视觉](https://github.com/HITSZ-OpenAuto/AUTO3006) 中提交了信息：Update readme.toml for AUTO3006

- Jiao Ziang 在 [数字图像处理](https://github.com/HITSZ-OpenAuto/AUTO3003) 中提交了信息：Update README.md for AUTO3003

- Jiao Ziang 在 [数字图像处理](https://github.com/HITSZ-OpenAuto/AUTO3003) 中提交了信息：Update readme.toml for AUTO3003

- Jiao Ziang 在 [自动控制理论 A](https://github.com/HITSZ-OpenAuto/AUTO3001A) 中提交了信息：Update README.md for AUTO3001A

- Jiao Ziang 在 [自动控制理论 A](https://github.com/HITSZ-OpenAuto/AUTO3001A) 中提交了信息：Update readme.toml for AUTO3001A

- Jiao Ziang 在 [控制理论中的代数基础](https://github.com/HITSZ-OpenAuto/AUTO2006) 中提交了信息：Update README.md for AUTO2006

- Jiao Ziang 在 [控制理论中的代数基础](https://github.com/HITSZ-OpenAuto/AUTO2006) 中提交了信息：Update readme.toml for AUTO2006

### 周五 (1.30)

- Jiao Ziang 在 [凸优化与最优控制](https://github.com/HITSZ-OpenAuto/AUTO5023) 中提交了信息：docs: add structured course info (AUTO5023.toml) (#20)
