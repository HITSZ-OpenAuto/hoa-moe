---
authors:
  - image: https://github.com/openai.png
    link: https://github.com/openai
    name: ChatGPT
date: "2025-11-28"
draft: false
excludeSearch: false
title: AUTO 周报 2025-11-21 - 2025-11-28
---

## 本周更新摘要

- 新建/拆分课程仓库
  - 电气专业选修课（EE30XX）新建并完成初始提交。
  - 自动化专业导论（AUTO2001）新建仓库并提交初始内容。
  - 计算机专业导论（COMP2001）新建并已迁移 OpenCS 的计算机导论内容并补充说明。
  - 电路与电子学 I（EE1018）从原仓库拆分为独立仓库（Initial commit），并将 OpenCS 中电工/电子相关资料迁移至该仓库；同时对电路与电子学（EE1013）中 24 级内容做相应拆分调整。

- 新增教材/习题/笔记/资源
  - AUTO1001（自动化认知与实践）：删除电子书，新增课程论文和 21 秋期末考试答案。
  - MATH4004（数值分析）：添加 2025 年深圳试题。
  - AUTO3001A（自动控制理论 A）：新增 2025 年自控 A 的笔记。
  - MATH1005（复变函数与积分变换）：上传 2025 年复变函数思维导图。
  - COMP3006（机器学习概论）：上传 23 级期末回忆版试题/资料；COMP3006 也有课程信息更新。
  - AUTO3011（运动控制系统）：添加作者个人作业与实验资料并更新 README。
  - MATH4001（矩阵分析）：添加若干年考试题。
  - hoa-spec：新增 hoa 3.0 的元数据。
  - MOOC 仓库：整理 README 结构并新增思政实践网课链接、刷课脚本及使用教程。

- 工具链与自动化改进
  - repos-management：多次更新（自动同步仓库列表）并增强工作流功能（加入并发处理、关闭 PR 的功能、修正提交信息用 PR 标题、更新文档等）。
  - auto-metadata / n8nAutoMetadata：新增完整的自动元数据流水线与 n8n 工作流文件，完善自动化元数据处理能力。

- 大规模 CI / 文档调整
  - 由 Kowyo 统一对大量课程仓库禁用定时触发（ci: disable scheduled trigger），以减少不必要的定时 CI 运行（涉及数十个课程仓库）。
  - 多门课程（以计算机与电气类为主）进行了课程信息或说明文档的更新与文档命名规范化（例如 COMP3005、COMP3021、COMP3029、COMP3018 等）。

- 其他杂项（简要）
  - 若干仓库进行了格式修正、README/文件删改及少量命名/样式调整，为日常维护类更新。

## 更新内容

### 周五 (11.28)

- W. D. Gaster 在 [电路与电子学 I](https://github.com/HITSZ-OpenAuto/EE1018) 中提交了信息：修改格式错误

- W. D. Gaster 在 [计算机专业导论](https://github.com/HITSZ-OpenAuto/COMP2001) 中提交了信息：修改开课学期

- W. D. Gaster 在 [电路与电子学 I](https://github.com/HITSZ-OpenAuto/EE1018) 中提交了信息：修改课程信息

- W. D. Gaster 在 [电气专业选修课](https://github.com/HITSZ-OpenAuto/EE30XX) 中提交了信息：新仓库上新

- W. D. Gaster 在 [电气专业选修课](https://github.com/HITSZ-OpenAuto/EE30XX) 中提交了信息：新建电气选修课仓库

- GitHub Actions 在 [repos-management](https://github.com/HITSZ-OpenAuto/repos-management) 中提交了信息：ci: update repositories list [automated]

- W. D. Gaster 在 [电气专业选修课](https://github.com/HITSZ-OpenAuto/EE30XX) 中提交了信息：Initial commit

- W. D. Gaster 在 [自动化专业导论](https://github.com/HITSZ-OpenAuto/AUTO2001) 中提交了信息：新建自动化导论的仓库

- GitHub Actions 在 [repos-management](https://github.com/HITSZ-OpenAuto/repos-management) 中提交了信息：ci: update repositories list [automated]

- W. D. Gaster 在 [自动化专业导论](https://github.com/HITSZ-OpenAuto/AUTO2001) 中提交了信息：Initial commit

- W. D. Gaster 在 [计算机专业导论](https://github.com/HITSZ-OpenAuto/COMP2001) 中提交了信息：迁移 OpenCS 的计算机导论内容并做说明

- GitHub Actions 在 [repos-management](https://github.com/HITSZ-OpenAuto/repos-management) 中提交了信息：ci: update repositories list [automated]

- W. D. Gaster 在 [计算机专业导论](https://github.com/HITSZ-OpenAuto/COMP2001) 中提交了信息：Initial commit

- W. D. Gaster 在 [电路与电子学 I](https://github.com/HITSZ-OpenAuto/EE1018) 中提交了信息：新课程仓库拆分上新

- W. D. Gaster 在 [电路与电子学 I](https://github.com/HITSZ-OpenAuto/EE1018) 中提交了信息：新仓库拆分上新

- W. D. Gaster 在 [电路与电子学 I](https://github.com/HITSZ-OpenAuto/EE1018) 中提交了信息：将电路与电子学 I 课程从电路与电子学 II 中拆分出来独立仓库，并将 OpenCS 的电工与电子技术相关资料进行迁移。

- W. D. Gaster 在 [电路与电子学](https://github.com/HITSZ-OpenAuto/EE1013) 中提交了信息：修改 24 级电路与电子学 II 的内容，将 I 和 III 内容独立

- GitHub Actions 在 [repos-management](https://github.com/HITSZ-OpenAuto/repos-management) 中提交了信息：ci: update repositories list [automated]

- W. D. Gaster 在 [电路与电子学 I](https://github.com/HITSZ-OpenAuto/EE1018) 中提交了信息：Initial commit

- W. D. Gaster 在 [电磁场](https://github.com/HITSZ-OpenAuto/EE2003) 中提交了信息：更新课程信息

- W. D. Gaster 在 [面向领域的计算机系统设计与开发实践](https://github.com/HITSZ-OpenAuto/COMP2029) 中提交了信息：更新课程信息

- W. D. Gaster 在 [机器学习概论](https://github.com/HITSZ-OpenAuto/COMP3006) 中提交了信息：修改课程信息

- W. D. Gaster 在 [智能证券投资](https://github.com/HITSZ-OpenAuto/COMP3042) 中提交了信息：修改课程信息

- W. D. Gaster 在 [网络与系统安全](https://github.com/HITSZ-OpenAuto/COMP3054) 中提交了信息：修改课程信息

- W. D. Gaster 在 [自然语言处理](https://github.com/HITSZ-OpenAuto/COMP3021) 中提交了信息：修改课程信息

- W. D. Gaster 在 [计算机视觉](https://github.com/HITSZ-OpenAuto/COMP3029) 中提交了信息：修改课程信息

- W. D. Gaster 在 [图像处理](https://github.com/HITSZ-OpenAuto/COMP3018) 中提交了信息：修改课程信息

- W. D. Gaster 在 [服务计算](https://github.com/HITSZ-OpenAuto/COMP3017) 中提交了信息：修改课程信息

- W. D. Gaster 在 [软件体系结构](https://github.com/HITSZ-OpenAuto/COMP3028) 中提交了信息：修改课程信息

- W. D. Gaster 在 [信息检索](https://github.com/HITSZ-OpenAuto/COMP3030) 中提交了信息：修改课程信息

- W. D. Gaster 在 [汇编语言与接口技术](https://github.com/HITSZ-OpenAuto/COMP3053) 中提交了信息：修改课程信息

- W. D. Gaster 在 [软件工程](https://github.com/HITSZ-OpenAuto/COMP3002) 中提交了信息：修改课程信息

- W. D. Gaster 在 [大数据导论](https://github.com/HITSZ-OpenAuto/COMP3009) 中提交了信息：修改课程信息

- W. D. Gaster 在 [计算机体系结构](https://github.com/HITSZ-OpenAuto/COMP3044) 中提交了信息：修改课程信息

- W. D. Gaster 在 [模式识别](https://github.com/HITSZ-OpenAuto/COMP3007) 中提交了信息：修改课程信息

- W. D. Gaster 在 [计算机体系结构](https://github.com/HITSZ-OpenAuto/COMP3011) 中提交了信息：修改课程信息

- W. D. Gaster 在 [密码学基础](https://github.com/HITSZ-OpenAuto/COMP3040) 中提交了信息：修改课程信息

- W. D. Gaster 在 [形式语言与自动机](https://github.com/HITSZ-OpenAuto/COMP3004) 中提交了信息：修改课程信息

- W. D. Gaster 在 [计算机体系结构](https://github.com/HITSZ-OpenAuto/COMP3011) 中提交了信息：修改课程信息

- GitHub Actions 在 [repos-management](https://github.com/HITSZ-OpenAuto/repos-management) 中提交了信息：ci: update repositories list [automated]

- Jiao 在 [auto-metadata](https://github.com/HITSZ-OpenAuto/auto-metadata) 中提交了信息：feat: full auto-metadata pipeline

### 周四 (11.27)

- W. D. Gaster 在 [人工智能](https://github.com/HITSZ-OpenAuto/COMP3005) 中提交了信息：添加课程信息

### 周二 (11.25)

- cecilia 在 [人工智能](https://github.com/HITSZ-OpenAuto/COMP3005) 中提交了信息：standardize the name of document (#9)

- cecilia 在 [计算机网络](https://github.com/HITSZ-OpenAuto/COMP3003) 中提交了信息：standardize the name of document (#9)

- Maxwell Jay 在 [毛泽东思想和中国特色社会主义理论体系概论](https://github.com/HITSZ-OpenAuto/GEIP1018) 中提交了信息：修复仓库内 2022 年笔记命名错误问题 (#19)

### 周一 (11.24)

- Jiao Ziang 在 [n8nAutoMetadata](https://github.com/HITSZ-OpenAuto/n8nAutoMetadata) 中提交了信息：增加 n8n 工作流文件

- 345ljh 在 [数值分析](https://github.com/HITSZ-OpenAuto/MATH4004) 中提交了信息：添加 2025 年深圳试题 (#11)

- Junda Wu 在 [自动化认知与实践](https://github.com/HITSZ-OpenAuto/AUTO1001) 中提交了信息：删除电子书；增加课程论文和 21 秋期末考试答案 (#27)

- zhuqi000 在 [自动控制理论 A](https://github.com/HITSZ-OpenAuto/AUTO3001A) 中提交了信息：增加 2025 自控 A 的笔记 (#28)

- Rsir 在 [复变函数与积分变换](https://github.com/HITSZ-OpenAuto/MATH1005) 中提交了信息：上传 2025 复变函数思维导图 (#32)

- Kowyo 在 [机器学习概论](https://github.com/HITSZ-OpenAuto/AUTO3019) 中提交了信息：ci: disable scheduled trigger (#12)

- Kowyo 在 [电路 IA](https://github.com/HITSZ-OpenAuto/EE1011A) 中提交了信息：ci: disable scheduled trigger (#19)

### 周日 (11.23)

- OliverWu515 在 [运动控制系统](https://github.com/HITSZ-OpenAuto/AUTO3011) 中提交了信息：添加本人作业、实验等资料，更新 readme

- OliverWu515 在 [矩阵分析](https://github.com/HITSZ-OpenAuto/MATH4001) 中提交了信息：Merge branch 'main' of https://github.com/HITSZ-OpenAuto/MATH4001

- OliverWu515 在 [矩阵分析](https://github.com/HITSZ-OpenAuto/MATH4001) 中提交了信息：添加若干年考试题

### 周六 (11.22)

- Kowyo 在 [MOOC](https://github.com/HITSZ-OpenAuto/MOOC) 中提交了信息：整理 README 的结构和格式 (#21)

- Jiayi-hit 在 [机器学习概论](https://github.com/HITSZ-OpenAuto/COMP3006) 中提交了信息：上传机器学习 23 级期末回忆版 (#5)

- OliverWu515 在 [hoa-spec](https://github.com/HITSZ-OpenAuto/hoa-spec) 中提交了信息：init: add metadata of hoa 3.0

- HitTheStars 在 [MOOC](https://github.com/HITSZ-OpenAuto/MOOC) 中提交了信息：加入了思政实践网课的链接以及相关描述，添加了它的刷课脚本和使用教程。 (#17)

- Kowyo 在 [MOOC](https://github.com/HITSZ-OpenAuto/MOOC) 中提交了信息：ci: disable scheduled trigger (#20)

- Kowyo 在 [新时代中国特色社会主义理论与实践](https://github.com/HITSZ-OpenAuto/GEIP4004) 中提交了信息：[automated-generated-pr] ci: disable scheduled trigger (#1)

- Kowyo 在 [专业综合实践](https://github.com/HITSZ-OpenAuto/EE304X) 中提交了信息：ci: disable scheduled trigger (#3)

- Kowyo 在 [深度学习体系结构](https://github.com/HITSZ-OpenAuto/COMP3043) 中提交了信息：ci: disable scheduled trigger (#4)

- Kowyo 在 [人工智能](https://github.com/HITSZ-OpenAuto/COMP3005) 中提交了信息：ci: disable scheduled trigger (#8)

- Kowyo 在 [智能证券投资](https://github.com/HITSZ-OpenAuto/COMP3042) 中提交了信息：ci: disable scheduled trigger (#9)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3039) 中提交了信息：[automated-generated-pr] ci: disable scheduled trigger (#5)

- Kowyo 在 [网络与系统安全](https://github.com/HITSZ-OpenAuto/COMP3054) 中提交了信息：ci: disable scheduled trigger (#8)

- Kowyo 在 [自然语言处理](https://github.com/HITSZ-OpenAuto/COMP3021) 中提交了信息：ci: disable scheduled trigger (#7)

- Kowyo 在 [计算机视觉](https://github.com/HITSZ-OpenAuto/COMP3029) 中提交了信息：ci: disable scheduled trigger (#6)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3019) 中提交了信息：[automated-generated-pr] ci: disable scheduled trigger (#5)

- Kowyo 在 [图像处理](https://github.com/HITSZ-OpenAuto/COMP3018) 中提交了信息：[automated-generated-pr] ci: disable scheduled trigger (#5)

- Kowyo 在 [服务计算](https://github.com/HITSZ-OpenAuto/COMP3017) 中提交了信息：ci: disable scheduled trigger (#7)

- Kowyo 在 [软件体系结构](https://github.com/HITSZ-OpenAuto/COMP3028) 中提交了信息：[automated-generated-pr] ci: disable scheduled trigger (#7)

- Kowyo 在 [信息检索](https://github.com/HITSZ-OpenAuto/COMP3030) 中提交了信息：ci: disable scheduled trigger (#6)

- Kowyo 在 [机器学习概论](https://github.com/HITSZ-OpenAuto/COMP3006) 中提交了信息：[automated-generated-pr] ci: disable scheduled trigger (#6)

- Kowyo 在 [汇编语言与接口技术](https://github.com/HITSZ-OpenAuto/COMP3053) 中提交了信息：[automated-generated-pr] ci: disable scheduled trigger (#5)

- Kowyo 在 [软件工程](https://github.com/HITSZ-OpenAuto/COMP3002) 中提交了信息：ci: disable scheduled trigger (#6)

- Kowyo 在 [大数据导论](https://github.com/HITSZ-OpenAuto/COMP3009) 中提交了信息：ci: disable scheduled trigger (#6)

- Kowyo 在 [计算机体系结构](https://github.com/HITSZ-OpenAuto/COMP3044) 中提交了信息：ci: disable scheduled trigger (#6)

- Kowyo 在 [模式识别](https://github.com/HITSZ-OpenAuto/COMP3007) 中提交了信息：ci: disable scheduled trigger (#7)

- Kowyo 在 [密码学基础](https://github.com/HITSZ-OpenAuto/COMP3040) 中提交了信息：ci: disable scheduled trigger (#6)

- Kowyo 在 [形式语言与自动机](https://github.com/HITSZ-OpenAuto/COMP3004) 中提交了信息：ci: disable scheduled trigger (#7)

- Kowyo 在 [计算机体系结构](https://github.com/HITSZ-OpenAuto/COMP3011) 中提交了信息：[automated-generated-pr] ci: disable scheduled trigger (#6)

- Kowyo 在 [近世代数](https://github.com/HITSZ-OpenAuto/COMP2010) 中提交了信息：ci: disable scheduled trigger (#7)

- Kowyo 在 [面向领域的计算机系统设计与开发实践](https://github.com/HITSZ-OpenAuto/COMP2029) 中提交了信息：ci: disable scheduled trigger (#7)

- Kowyo 在 [软件构造实践](https://github.com/HITSZ-OpenAuto/COMP3060) 中提交了信息：[automated-generated-pr] ci: disable scheduled trigger (#6)

- Kowyo 在 [数据库系统](https://github.com/HITSZ-OpenAuto/COMP3010) 中提交了信息：[automated-generated-pr] ci: disable scheduled trigger (#6)

- Kowyo 在 [编译原理](https://github.com/HITSZ-OpenAuto/COMP3013) 中提交了信息：ci: disable scheduled trigger (#7)

- Kowyo 在 [操作系统](https://github.com/HITSZ-OpenAuto/COMP3001) 中提交了信息：ci: disable scheduled trigger (#7)

- Kowyo 在 [计算机网络](https://github.com/HITSZ-OpenAuto/COMP3003) 中提交了信息：[automated-generated-pr] ci: disable scheduled trigger (#8)

- Kowyo 在 [软件构造](https://github.com/HITSZ-OpenAuto/COMP3059) 中提交了信息：ci: disable scheduled trigger (#9)

- Kowyo 在 [计算机设计与实践](https://github.com/HITSZ-OpenAuto/COMP2012) 中提交了信息：ci: disable scheduled trigger (#9)

- Kowyo 在 [计算机组成原理](https://github.com/HITSZ-OpenAuto/COMP2008) 中提交了信息：[automated-generated-pr] ci: disable scheduled trigger (#6)

- Kowyo 在 [数据结构与算法](https://github.com/HITSZ-OpenAuto/COMP2052) 中提交了信息：ci: disable scheduled trigger (#7)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3052) 中提交了信息：[automated-generated-pr] ci: disable scheduled trigger (#9)

- Kowyo 在 [数字逻辑设计](https://github.com/HITSZ-OpenAuto/COMP2051) 中提交了信息：ci: disable scheduled trigger (#7)

- Kowyo 在 [离散数学](https://github.com/HITSZ-OpenAuto/COMP2030) 中提交了信息：ci: disable scheduled trigger (#7)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/MATH4002) 中提交了信息：[automated-generated-pr] ci: disable scheduled trigger (#5)

- Kowyo 在 [固体力学](https://github.com/HITSZ-OpenAuto/MECH2022) 中提交了信息：[automated-generated-pr] ci: disable scheduled trigger (#5)

- Kowyo 在 [设计与制造 A](https://github.com/HITSZ-OpenAuto/MECH2019) 中提交了信息：[automated-generated-pr] ci: disable scheduled trigger (#7)

- Kowyo 在 [电力电子技术](https://github.com/HITSZ-OpenAuto/EE3002) 中提交了信息：[automated-generated-pr] ci: disable scheduled trigger (#8)

- Kowyo 在 [电力系统分析](https://github.com/HITSZ-OpenAuto/EE3015) 中提交了信息：[automated-generated-pr] ci: disable scheduled trigger (#9)

- Kowyo 在 [电机学](https://github.com/HITSZ-OpenAuto/EE3001) 中提交了信息：ci: disable scheduled trigger (#10)

- Kowyo 在 [电磁场](https://github.com/HITSZ-OpenAuto/EE2003) 中提交了信息：ci: disable scheduled trigger (#9)

- Kowyo 在 [矩阵分析](https://github.com/HITSZ-OpenAuto/MATH4001) 中提交了信息：ci: disable scheduled trigger (#11)

- Kowyo 在 [习近平新时代中国特色社会主义思想概论](https://github.com/HITSZ-OpenAuto/GEIP1017) 中提交了信息：ci: disable scheduled trigger (#14)

- Kowyo 在 [思想道德与法治](https://github.com/HITSZ-OpenAuto/GEIP1015) 中提交了信息：[automated-generated-pr] ci: disable scheduled trigger (#13)

- Kowyo 在 [中国科技史话](https://github.com/HITSZ-OpenAuto/SEIN1040) 中提交了信息：ci: disable scheduled trigger (#10)

- Kowyo 在 [跨专业选修课程体系](https://github.com/HITSZ-OpenAuto/CrossSpecialty) 中提交了信息：ci: disable scheduled trigger (#12)

- Kowyo 在 [普通天文学](https://github.com/HITSZ-OpenAuto/SPST1004) 中提交了信息：[automated-generated-pr] ci: disable scheduled trigger (#11)

- Kowyo 在 [工程训练（金工实习）](https://github.com/HITSZ-OpenAuto/ENGG1002) 中提交了信息：ci: disable scheduled trigger (#12)

- Kowyo 在 [工程训练（电子工艺实习）](https://github.com/HITSZ-OpenAuto/ENGG1003) 中提交了信息：ci: disable scheduled trigger (#14)

- Kowyo 在 [高等电路与电子分析](https://github.com/HITSZ-OpenAuto/EE2004) 中提交了信息：ci: disable scheduled trigger (#14)

- Kowyo 在 [数值分析](https://github.com/HITSZ-OpenAuto/MATH4004) 中提交了信息：ci: disable scheduled trigger (#14)

- Kowyo 在 [移动机器人导论](https://github.com/HITSZ-OpenAuto/AUTO3012) 中提交了信息：[automated-generated-pr] ci: disable scheduled trigger (#12)

- Kowyo 在 [文理通识课程体系](https://github.com/HITSZ-OpenAuto/GeneralKnowledge) 中提交了信息：ci: disable scheduled trigger (#16)

- Kowyo 在 [写作与沟通](https://github.com/HITSZ-OpenAuto/WRIT0001) 中提交了信息：ci: disable scheduled trigger (#13)

- Kowyo 在 [日语 I](https://github.com/HITSZ-OpenAuto/WOCD1008) 中提交了信息：[automated-generated-pr] ci: disable scheduled trigger (#10)

- Kowyo 在 [运动控制系统](https://github.com/HITSZ-OpenAuto/AUTO3011) 中提交了信息：[automated-generated-pr] ci: disable scheduled trigger (#13)

- Kowyo 在 [模式识别](https://github.com/HITSZ-OpenAuto/AUTO5024) 中提交了信息：[automated-generated-pr] ci: disable scheduled trigger (#15)

- Kowyo 在 [嵌入式系统](https://github.com/HITSZ-OpenAuto/AUTO3024) 中提交了信息：[automated-generated-pr] ci: disable scheduled trigger (#12)

- Kowyo 在 [非线性与自适应控制](https://github.com/HITSZ-OpenAuto/AUTO5005) 中提交了信息：ci: disable scheduled trigger (#13)

- Kowyo 在 [系统辨识](https://github.com/HITSZ-OpenAuto/AUTO5002) 中提交了信息：[automated-generated-pr] ci: disable scheduled trigger (#12)

- Kowyo 在 [线性系统理论](https://github.com/HITSZ-OpenAuto/AUTO5001) 中提交了信息：ci: disable scheduled trigger (#14)

- Kowyo 在 [毕业设计](https://github.com/HITSZ-OpenAuto/AUTO3099) 中提交了信息：ci: disable scheduled trigger (#18)

- Kowyo 在 [机器视觉](https://github.com/HITSZ-OpenAuto/AUTO3006) 中提交了信息：ci: disable scheduled trigger (#19)

- Kowyo 在 [自动控制实践 B](https://github.com/HITSZ-OpenAuto/AUTO3002B) 中提交了信息：ci: disable scheduled trigger (#23)

- Kowyo 在 [自动控制理论 B](https://github.com/HITSZ-OpenAuto/AUTO3001B) 中提交了信息：[automated-generated-pr] ci: disable scheduled trigger (#25)

- Kowyo 在 [凸优化与最优控制](https://github.com/HITSZ-OpenAuto/AUTO5023) 中提交了信息：ci: disable scheduled trigger (#16)

- Kowyo 在 [创新训练课 A](https://github.com/HITSZ-OpenAuto/AUTO2003A) 中提交了信息：[automated-generated-pr] ci: disable scheduled trigger (#12)

- Kowyo 在 [电路与电子技术实验](https://github.com/HITSZ-OpenAuto/EE1014) 中提交了信息：ci: disable scheduled trigger (#16)

- Kowyo 在 [体育](https://github.com/HITSZ-OpenAuto/PE100X) 中提交了信息：ci: disable scheduled trigger (#25)

- Kowyo 在 [电路与电子学](https://github.com/HITSZ-OpenAuto/EE1013) 中提交了信息：ci: disable scheduled trigger (#19)

- Kowyo 在 [微积分 A](https://github.com/HITSZ-OpenAuto/MATH1015A) 中提交了信息：[automated-generated-pr] ci: disable scheduled trigger (#23)

- Kowyo 在 [自动控制理论 A](https://github.com/HITSZ-OpenAuto/AUTO3001A) 中提交了信息：ci: disable scheduled trigger (#31)

- Kowyo 在 [最优估计](https://github.com/HITSZ-OpenAuto/AUTO5013) 中提交了信息：ci: disable scheduled trigger (#16)

- Kowyo 在 [自动化领域专家系列讲座](https://github.com/HITSZ-OpenAuto/AUTO3022) 中提交了信息：ci: disable scheduled trigger (#14)

- Kowyo 在 [机械设计基础](https://github.com/HITSZ-OpenAuto/MECH2010) 中提交了信息：ci: disable scheduled trigger (#15)

- Kowyo 在 [微积分 B](https://github.com/HITSZ-OpenAuto/MATH1015B) 中提交了信息：ci: disable scheduled trigger (#20)

- Kowyo 在 [电路实验 IA](https://github.com/HITSZ-OpenAuto/EE1012A) 中提交了信息：[automated-generated-pr] ci: disable scheduled trigger (#14)

- Kowyo 在 [大学英语](https://github.com/HITSZ-OpenAuto/LANG100X) 中提交了信息：[automated-generated-pr] ci: disable scheduled trigger (#16)

- Kowyo 在 [大学物理](https://github.com/HITSZ-OpenAuto/PHYS1001) 中提交了信息：ci: disable scheduled trigger (#23)

- Kowyo 在 [创新训练课 B](https://github.com/HITSZ-OpenAuto/AUTO2003B) 中提交了信息：[automated-generated-pr] ci: disable scheduled trigger (#19)

- Kowyo 在 [中国近现代史纲要](https://github.com/HITSZ-OpenAuto/GEIP1016) 中提交了信息：ci: disable scheduled trigger (#20)

- Kowyo 在 [马克思主义基本原理](https://github.com/HITSZ-OpenAuto/GEIP1011) 中提交了信息：ci: disable scheduled trigger (#31)

- Kowyo 在 [电路实验 IB](https://github.com/HITSZ-OpenAuto/EE1012B) 中提交了信息：[automated-generated-pr] ci: disable scheduled trigger (#15)

- Kowyo 在 [自动化认知与实践](https://github.com/HITSZ-OpenAuto/AUTO1001) 中提交了信息：ci: disable scheduled trigger (#30)

- Kowyo 在 [经济学原理](https://github.com/HITSZ-OpenAuto/ECON2005F) 中提交了信息：[automated-generated-pr] ci: disable scheduled trigger (#12)

- Kowyo 在 [理论力学Ⅱ](https://github.com/HITSZ-OpenAuto/EMEC1002) 中提交了信息：[automated-generated-pr] ci: disable scheduled trigger (#18)

- Kowyo 在 [毛泽东思想和中国特色社会主义理论体系概论](https://github.com/HITSZ-OpenAuto/GEIP1018) 中提交了信息：ci: disable scheduled trigger (#17)

- Kowyo 在 [模拟电子技术实验](https://github.com/HITSZ-OpenAuto/EE1008) 中提交了信息：ci: disable scheduled trigger (#15)

- Kowyo 在 [数字电子技术实验](https://github.com/HITSZ-OpenAuto/EE1010) 中提交了信息：ci: disable scheduled trigger (#15)

- Kowyo 在 [数字电子技术基础](https://github.com/HITSZ-OpenAuto/EE1009) 中提交了信息：ci: disable scheduled trigger (#25)

- Kowyo 在 [模拟电子技术基础](https://github.com/HITSZ-OpenAuto/EE1007) 中提交了信息：ci: disable scheduled trigger (#23)

- Kowyo 在 [控制理论中的代数基础](https://github.com/HITSZ-OpenAuto/AUTO2006) 中提交了信息：[automated-generated-pr] ci: disable scheduled trigger (#18)

- Kowyo 在 [DSP 的原理与应用](https://github.com/HITSZ-OpenAuto/EE3005) 中提交了信息：ci: disable scheduled trigger (#13)

- Kowyo 在 [代数与几何](https://github.com/HITSZ-OpenAuto/MATH1002) 中提交了信息：ci: disable scheduled trigger (#25)

- Kowyo 在 [自动控制实践 A 实验](https://github.com/HITSZ-OpenAuto/AUTO3016) 中提交了信息：ci: disable scheduled trigger (#24)

- Kowyo 在 [机器人学导论](https://github.com/HITSZ-OpenAuto/AUTO3005) 中提交了信息：ci: disable scheduled trigger (#22)

- Kowyo 在 [C++ 语言程序设计](https://github.com/HITSZ-OpenAuto/COMP2014) 中提交了信息：[automated-generated-pr] ci: disable scheduled trigger (#15)

- Kowyo 在 [程序设计思维与实践](https://github.com/HITSZ-OpenAuto/COMP1011) 中提交了信息：ci: disable scheduled trigger (#19)

- Kowyo 在 [数学规划与数值优化](https://github.com/HITSZ-OpenAuto/AUTO3028) 中提交了信息：ci: disable scheduled trigger (#16)

- Kowyo 在 [数据结构与算法](https://github.com/HITSZ-OpenAuto/COMP2050) 中提交了信息：ci: disable scheduled trigger (#15)

- Kowyo 在 [过程控制系统](https://github.com/HITSZ-OpenAuto/AUTO3007) 中提交了信息：ci: disable scheduled trigger (#27)

- Kowyo 在 [电路 IB](https://github.com/HITSZ-OpenAuto/EE1011B) 中提交了信息：ci: disable scheduled trigger (#23)

- Kowyo 在 [概率论与数理统计](https://github.com/HITSZ-OpenAuto/MATH1004) 中提交了信息：ci: disable scheduled trigger (#27)

- Kowyo 在 [复变函数与积分变换](https://github.com/HITSZ-OpenAuto/MATH1005) 中提交了信息：ci: disable scheduled trigger (#31)

- Kowyo 在 [系统建模与仿真](https://github.com/HITSZ-OpenAuto/AUTO3004) 中提交了信息：ci: disable scheduled trigger (#22)

- Kowyo 在 [数字图像处理](https://github.com/HITSZ-OpenAuto/AUTO3003) 中提交了信息：ci: disable scheduled trigger (#24)

- Kowyo 在 [信号分析与处理](https://github.com/HITSZ-OpenAuto/AUTO2005) 中提交了信息：ci: disable scheduled trigger (#32)

- Kowyo 在 [大学化学 III](https://github.com/HITSZ-OpenAuto/CHEM1012) 中提交了信息：ci: disable scheduled trigger (#15)

- Kowyo 在 [自动控制实践 A](https://github.com/HITSZ-OpenAuto/AUTO3002A) 中提交了信息：ci: disable scheduled trigger (#43)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/course-template) 中提交了信息：ci: disable scheduled trigger (#22)

- Kowyo 在 [大学物理实验](https://github.com/HITSZ-OpenAuto/PHYS1002) 中提交了信息：ci: disable scheduled trigger (#62)

- Kowyo 在 [repos-management](https://github.com/HITSZ-OpenAuto/repos-management) 中提交了信息：feat: add concurrency to add_workflow

- Kowyo 在 [repos-management](https://github.com/HITSZ-OpenAuto/repos-management) 中提交了信息：feat: add concurrency to close_pr

- Kowyo 在 [repos-management](https://github.com/HITSZ-OpenAuto/repos-management) 中提交了信息：feat: add close pr

- Kowyo 在 [repos-management](https://github.com/HITSZ-OpenAuto/repos-management) 中提交了信息：fix: use PR_TITLE for commit message

- Kowyo 在 [repos-management](https://github.com/HITSZ-OpenAuto/repos-management) 中提交了信息：update docs

- Kowyo 在 [repos-management](https://github.com/HITSZ-OpenAuto/repos-management) 中提交了信息：chore: update pr description

### 周五 (11.21)

- IcyDesert 在 [repos-management](https://github.com/HITSZ-OpenAuto/repos-management) 中提交了信息：docs: add source of workflow file in add_workflow.sh
