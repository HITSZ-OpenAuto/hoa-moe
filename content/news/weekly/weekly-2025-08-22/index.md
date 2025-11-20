---
authors:
  - image: https://github.com/openai.png
    link: https://github.com/openai
    name: ChatGPT
date: "2025-08-29"
draft: false
excludeSearch: false
title: AUTO 周报 2025-08-22 - 2025-08-29
---

## 本周更新摘要

- 示例：大学物理实验 / COMP 系列
  - 大量实验课仓库合并/新增了来自 OpenCS 的教学内容（文档、示例、练习等），涉及多门课程（代表：COMP2010、COMP3001/3002/3003/3004/3005/3006/3007/3009/3010/3011/3013/3017/3018/3019/3021/3028/3029/3030/3042/3052/3053/3054/3059 等）。部分仓库为合并（merge）或以 PR 形式引入内容。
  - 重点变更：COMP2051、COMP2030 完成 OpenCS 内容迁移并补充了 23 级相关更新；COMP3006 修正学分；COMP3018 修改了成绩构成。
  - 多次由 mircecilia / cecilia / JiaoZiang 等提交合并或新增文档。

- CI / 仓库模板与自动化
  - 大量课程（EE、AUTO、MATH、PHYS、GEIP、LANG、PE、WRIT、MOOC 等）统一采用了“可复用的 CI workflow”，以规范与统一持续集成/自动化流程。
  - course-template 与若干课程收到 automated-generated PR：更新了 worktree.json 的生成逻辑（示例：PHYS1002、COMP2050、AUTO3007、EE1011B、MATH1004、MATH1005、AUTO3004、AUTO3003、AUTO2005、CHEM1012、AUTO3002A 等）。

- 仓库管理相关
  - repos-management：重构移除未使用的 personal access token sourcing，并简化 PR 标记定义（#9）；同时修复 workflow 中的 $ 转义问题（#8）。

- 其他
  - 若干仓库进行了小范围文档修改或格式调整（README 删除、文件重命名、格式微调等），属琐碎维护类更新。

（注：以上为本周主要亮点，合并/批量性更新以代表性课程为例列出。）

## 更新内容

### 周五 (8.29)

- Kowyo 在 [repos-management](https://github.com/HITSZ-OpenAuto/repos-management) 中提交了信息：refactor: remove unused personal access token sourcing and streamline PR marker definition (#9)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3005) 中提交了信息：ci: use a unified reusable workflow (#4)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3042) 中提交了信息：ci: use a unified reusable workflow (#5)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3039) 中提交了信息：ci: use a unified reusable workflow (#1)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3054) 中提交了信息：ci: use a unified reusable workflow (#3)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3021) 中提交了信息：ci: use a unified reusable workflow (#3)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3029) 中提交了信息：ci: use a unified reusable workflow (#2)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3019) 中提交了信息：ci: use a unified reusable workflow (#3)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3018) 中提交了信息：ci: use a unified reusable workflow (#2)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3017) 中提交了信息：ci: use a unified reusable workflow (#2)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3028) 中提交了信息：ci: use a unified reusable workflow (#3)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3030) 中提交了信息：ci: use a unified reusable workflow (#1)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3006) 中提交了信息：ci: use a unified reusable workflow (#2)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3053) 中提交了信息：ci: use a unified reusable workflow (#2)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3002) 中提交了信息：ci: use a unified reusable workflow (#2)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3009) 中提交了信息：ci: use a unified reusable workflow (#2)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3044) 中提交了信息：ci: use a unified reusable workflow (#1)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3007) 中提交了信息：ci: use a unified reusable workflow (#3)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3040) 中提交了信息：ci: use a unified reusable workflow (#2)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3004) 中提交了信息：ci: use a unified reusable workflow (#2)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3011) 中提交了信息：ci: use a unified reusable workflow (#2)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP2010) 中提交了信息：ci: use a unified reusable workflow (#2)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP2029) 中提交了信息：ci: use a unified reusable workflow (#1)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3060) 中提交了信息：ci: use a unified reusable workflow (#1)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3010) 中提交了信息：ci: use a unified reusable workflow (#2)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3013) 中提交了信息：ci: use a unified reusable workflow (#2)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3001) 中提交了信息：ci: use a unified reusable workflow (#2)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3003) 中提交了信息：ci: use a unified reusable workflow (#3)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3059) 中提交了信息：ci: use a unified reusable workflow (#1)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP2012) 中提交了信息：ci: use a unified reusable workflow (#2)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP2008) 中提交了信息：ci: use a unified reusable workflow (#1)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP2052) 中提交了信息：ci: use a unified reusable workflow (#1)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3052) 中提交了信息：ci: use a unified reusable workflow (#3)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP2051) 中提交了信息：ci: use a unified reusable workflow (#2)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP2030) 中提交了信息：ci: use a unified reusable workflow (#2)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/MATH4002) 中提交了信息：ci: use a unified reusable workflow (#1)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/MECH2022) 中提交了信息：ci: use a unified reusable workflow (#1)

- IcyDesert 在 [设计与制造 A](https://github.com/HITSZ-OpenAuto/MECH2019) 中提交了信息：ci: use a unified reusable workflow (#3)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/EE3002) 中提交了信息：ci: use a unified reusable workflow (#4)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/EE3015) 中提交了信息：ci: use a unified reusable workflow (#5)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/EE3001) 中提交了信息：ci: use a unified reusable workflow (#5)

- IcyDesert 在 [电磁场](https://github.com/HITSZ-OpenAuto/EE2003) 中提交了信息：ci: use a unified reusable workflow (#4)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/MATH4001) 中提交了信息：ci: use a unified reusable workflow (#5)

- IcyDesert 在 [习近平新时代中国特色社会主义思想概论](https://github.com/HITSZ-OpenAuto/GEIP1017) 中提交了信息：ci: use a unified reusable workflow (#8)

- IcyDesert 在 [思想道德与法治](https://github.com/HITSZ-OpenAuto/GEIP1015) 中提交了信息：ci: use a unified reusable workflow (#9)

- IcyDesert 在 [中国科技史话](https://github.com/HITSZ-OpenAuto/SEIN1040) 中提交了信息：ci: use a unified reusable workflow (#5)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/course-template) 中提交了信息： [automated-generated-PR] ci: updated worktree.json generation (#15)

- IcyDesert 在 [跨专业选修课程体系](https://github.com/HITSZ-OpenAuto/CrossSpecialty) 中提交了信息：ci: use a unified reusable workflow (#7)

- IcyDesert 在 [普通天文学](https://github.com/HITSZ-OpenAuto/SPST1004) 中提交了信息：ci: use a unified reusable workflow (#7)

- IcyDesert 在 [工程训练（金工实习）](https://github.com/HITSZ-OpenAuto/ENGG1002) 中提交了信息：ci: use a unified reusable workflow (#7)

- IcyDesert 在 [工程训练（电子工艺实习）](https://github.com/HITSZ-OpenAuto/ENGG1003) 中提交了信息：ci: use a unified reusable workflow (#9)

- IcyDesert 在 [高等电路与电子分析](https://github.com/HITSZ-OpenAuto/EE2004) 中提交了信息：ci: use a unified reusable workflow (#9)

- IcyDesert 在 [数值分析](https://github.com/HITSZ-OpenAuto/MATH4004) 中提交了信息：ci: use a unified reusable workflow (#7)

- IcyDesert 在 [移动机器人导论](https://github.com/HITSZ-OpenAuto/AUTO3012) 中提交了信息：ci: use a unified reusable workflow (#8)

- IcyDesert 在 [文理通识课程体系](https://github.com/HITSZ-OpenAuto/GeneralKnowledge) 中提交了信息：ci: use a unified reusable workflow (#12)

- IcyDesert 在 [写作与沟通](https://github.com/HITSZ-OpenAuto/WRIT0001) 中提交了信息：ci: use a unified reusable workflow (#7)

- IcyDesert 在 [大学物理实验](https://github.com/HITSZ-OpenAuto/PHYS1002) 中提交了信息： [automated-generated-PR] ci: updated worktree.json generation (#56)

- IcyDesert 在 [机器学习概论](https://github.com/HITSZ-OpenAuto/AUTO3019) 中提交了信息：ci: use a unified reusable workflow (#8)

- IcyDesert 在 [日语 I](https://github.com/HITSZ-OpenAuto/WOCD1008) 中提交了信息：ci: use a unified reusable workflow (#6)

- IcyDesert 在 [运动控制系统](https://github.com/HITSZ-OpenAuto/AUTO3011) 中提交了信息：ci: use a unified reusable workflow (#9)

- IcyDesert 在 [模式识别](https://github.com/HITSZ-OpenAuto/AUTO5024) 中提交了信息：ci: use a unified reusable workflow (#11)

- IcyDesert 在 [嵌入式系统](https://github.com/HITSZ-OpenAuto/AUTO3024) 中提交了信息：ci: use a unified reusable workflow (#8)

- IcyDesert 在 [非线性与自适应控制](https://github.com/HITSZ-OpenAuto/AUTO5005) 中提交了信息：ci: use a unified reusable workflow (#8)

- IcyDesert 在 [系统辨识](https://github.com/HITSZ-OpenAuto/AUTO5002) 中提交了信息：ci: use a unified reusable workflow (#6)

- IcyDesert 在 [线性系统理论](https://github.com/HITSZ-OpenAuto/AUTO5001) 中提交了信息：ci: use a unified reusable workflow (#9)

- IcyDesert 在 [毕业设计](https://github.com/HITSZ-OpenAuto/AUTO3099) 中提交了信息：ci: use a unified reusable workflow (#13)

- IcyDesert 在 [机器视觉](https://github.com/HITSZ-OpenAuto/AUTO3006) 中提交了信息：ci: use a unified reusable workflow (#14)

- IcyDesert 在 [自动控制实践 B](https://github.com/HITSZ-OpenAuto/AUTO3002B) 中提交了信息：ci: use a unified reusable workflow (#18)

- IcyDesert 在 [自动控制理论 B](https://github.com/HITSZ-OpenAuto/AUTO3001B) 中提交了信息：ci: use a unified reusable workflow (#19)

- IcyDesert 在 [凸优化与最优控制](https://github.com/HITSZ-OpenAuto/AUTO5023) 中提交了信息：ci: use a unified reusable workflow (#11)

- IcyDesert 在 [创新训练课 A](https://github.com/HITSZ-OpenAuto/AUTO2003A) 中提交了信息：ci: use a unified reusable workflow (#8)

- IcyDesert 在 [电路与电子技术实验](https://github.com/HITSZ-OpenAuto/EE1014) 中提交了信息：ci: use a unified reusable workflow (#11)

- IcyDesert 在 [体育](https://github.com/HITSZ-OpenAuto/PE100X) 中提交了信息：ci: use a unified reusable workflow (#20)

- IcyDesert 在 [电路与电子学](https://github.com/HITSZ-OpenAuto/EE1013) 中提交了信息：ci: use a unified reusable workflow (#13)

- IcyDesert 在 [微积分 A](https://github.com/HITSZ-OpenAuto/MATH1015A) 中提交了信息：ci: use a unified reusable workflow (#19)

- IcyDesert 在 [电路 IA](https://github.com/HITSZ-OpenAuto/EE1011A) 中提交了信息：ci: use a unified reusable workflow (#14)

- IcyDesert 在 [自动控制理论 A](https://github.com/HITSZ-OpenAuto/AUTO3001A) 中提交了信息：ci: use a unified reusable workflow (#24)

- IcyDesert 在 [最优估计](https://github.com/HITSZ-OpenAuto/AUTO5013) 中提交了信息：ci: use a unified reusable workflow (#11)

- IcyDesert 在 [自动化领域专家系列讲座](https://github.com/HITSZ-OpenAuto/AUTO3022) 中提交了信息：ci: use a unified reusable workflow (#9)

- IcyDesert 在 [MOOC](https://github.com/HITSZ-OpenAuto/MOOC) 中提交了信息：ci: use a unified reusable workflow (#15)

- IcyDesert 在 [电路实验 IA](https://github.com/HITSZ-OpenAuto/EE1012A) 中提交了信息：ci: use a unified reusable workflow (#10)

- IcyDesert 在 [大学英语](https://github.com/HITSZ-OpenAuto/LANG100X) 中提交了信息：ci: use a unified reusable workflow (#12)

- IcyDesert 在 [大学物理](https://github.com/HITSZ-OpenAuto/PHYS1001) 中提交了信息：ci: use a unified reusable workflow (#18)

- IcyDesert 在 [创新训练课 B](https://github.com/HITSZ-OpenAuto/AUTO2003B) 中提交了信息：ci: use a unified reusable workflow (#15)

- IcyDesert 在 [中国近现代史纲要](https://github.com/HITSZ-OpenAuto/GEIP1016) 中提交了信息：ci: use a unified reusable workflow (#15)

- IcyDesert 在 [马克思主义基本原理](https://github.com/HITSZ-OpenAuto/GEIP1011) 中提交了信息：ci: use a unified reusable workflow (#26)

- IcyDesert 在 [电路实验 IB](https://github.com/HITSZ-OpenAuto/EE1012B) 中提交了信息：ci: use a unified reusable workflow (#12)

- IcyDesert 在 [自动化认知与实践](https://github.com/HITSZ-OpenAuto/AUTO1001) 中提交了信息：ci: use a unified reusable workflow (#24)

- IcyDesert 在 [经济学原理](https://github.com/HITSZ-OpenAuto/ECON2005F) 中提交了信息：ci: use a unified reusable workflow (#8)

- IcyDesert 在 [理论力学Ⅱ](https://github.com/HITSZ-OpenAuto/EMEC1002) 中提交了信息：ci: use a unified reusable workflow (#14)

- IcyDesert 在 [毛泽东思想和中国特色社会主义理论体系概论](https://github.com/HITSZ-OpenAuto/GEIP1018) 中提交了信息：ci: use a unified reusable workflow (#12)

- IcyDesert 在 [模拟电子技术实验](https://github.com/HITSZ-OpenAuto/EE1008) 中提交了信息：ci: use a unified reusable workflow (#10)

- IcyDesert 在 [数字电子技术实验](https://github.com/HITSZ-OpenAuto/EE1010) 中提交了信息：ci: use a unified reusable workflow (#10)

- IcyDesert 在 [数字电子技术基础](https://github.com/HITSZ-OpenAuto/EE1009) 中提交了信息：ci: use a unified reusable workflow (#20)

- IcyDesert 在 [模拟电子技术基础](https://github.com/HITSZ-OpenAuto/EE1007) 中提交了信息：ci: use a unified reusable workflow (#18)

- IcyDesert 在 [控制理论中的代数基础](https://github.com/HITSZ-OpenAuto/AUTO2006) 中提交了信息：ci: use a unified reusable workflow (#14)

- IcyDesert 在 [DSP 的原理与应用](https://github.com/HITSZ-OpenAuto/EE3005) 中提交了信息：ci: use a unified reusable workflow (#8)

- IcyDesert 在 [代数与几何](https://github.com/HITSZ-OpenAuto/MATH1002) 中提交了信息：ci: use a unified reusable workflow (#20)

- IcyDesert 在 [自动控制实践 A 实验](https://github.com/HITSZ-OpenAuto/AUTO3016) 中提交了信息：ci: use a unified reusable workflow (#19)

- IcyDesert 在 [机器人学导论](https://github.com/HITSZ-OpenAuto/AUTO3005) 中提交了信息：ci: use a unified reusable workflow (#17)

- IcyDesert 在 [C++ 语言程序设计](https://github.com/HITSZ-OpenAuto/COMP2014) 中提交了信息：ci: use a unified reusable workflow (#11)

- IcyDesert 在 [程序设计思维与实践](https://github.com/HITSZ-OpenAuto/COMP1011) 中提交了信息：ci: use a unified reusable workflow (#14)

- IcyDesert 在 [数学规划与数值优化](https://github.com/HITSZ-OpenAuto/AUTO3028) 中提交了信息： [automated-generated-PR] ci: updated worktree.json generation (#11)

- IcyDesert 在 [数据结构与算法](https://github.com/HITSZ-OpenAuto/COMP2050) 中提交了信息： [automated-generated-PR] ci: updated worktree.json generation (#10)

- IcyDesert 在 [过程控制系统](https://github.com/HITSZ-OpenAuto/AUTO3007) 中提交了信息： [automated-generated-PR] ci: updated worktree.json generation (#22)

- IcyDesert 在 [电路 IB](https://github.com/HITSZ-OpenAuto/EE1011B) 中提交了信息： [automated-generated-PR] ci: updated worktree.json generation (#18)

- IcyDesert 在 [概率论与数理统计](https://github.com/HITSZ-OpenAuto/MATH1004) 中提交了信息： [automated-generated-PR] ci: updated worktree.json generation (#22)

- IcyDesert 在 [复变函数与积分变换](https://github.com/HITSZ-OpenAuto/MATH1005) 中提交了信息： [automated-generated-PR] ci: updated worktree.json generation (#23)

- IcyDesert 在 [系统建模与仿真](https://github.com/HITSZ-OpenAuto/AUTO3004) 中提交了信息： [automated-generated-PR] ci: updated worktree.json generation (#17)

- IcyDesert 在 [数字图像处理](https://github.com/HITSZ-OpenAuto/AUTO3003) 中提交了信息： [automated-generated-PR] ci: updated worktree.json generation (#19)

- IcyDesert 在 [信号分析与处理](https://github.com/HITSZ-OpenAuto/AUTO2005) 中提交了信息： [automated-generated-PR] ci: updated worktree.json generation (#26)

- IcyDesert 在 [大学化学 III](https://github.com/HITSZ-OpenAuto/CHEM1012) 中提交了信息： [automated-generated-PR] ci: updated worktree.json generation (#9)

- IcyDesert 在 [自动控制实践 A](https://github.com/HITSZ-OpenAuto/AUTO3002A) 中提交了信息： [automated-generated-PR] ci: updated worktree.json generation (#35)

- IcyDesert 在 [repos-management](https://github.com/HITSZ-OpenAuto/repos-management) 中提交了信息：fix: escape $ in workflow file (#8)

- IcyDesert 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/course-template) 中提交了信息：ci: use a unified reusable workflow (#13)

### 周一 (8.25)

- WDGaster 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP2051) 中提交了信息：迁移实验

- W·D·Gaster 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP2051) 中提交了信息：迁移 OpenCS 仓库对应内容并补充 23 级相关变化

- W·D·Gaster 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP2030) 中提交了信息：迁移 OpenCS 仓库对应内容并补充 23 级相关变化

- cecilia 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3017) 中提交了信息：add new content from OpenCS (#1)

- cecilia 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3019) 中提交了信息：add new content from OpenCS (#2)

- cecilia 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3003) 中提交了信息：add new content from OpenCS (#2)

- cecilia 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3029) 中提交了信息：Merge pull request #1 from mircecilia/main

- cecilia 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3028) 中提交了信息：Merge pull request #2 from mircecilia/main

- cecilia 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3054) 中提交了信息：Merge pull request #2 from mircecilia/main

- cecilia 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3021) 中提交了信息：add new content from OpenCS (#2)

- cecilia 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3042) 中提交了信息：Merge pull request #4 from mircecilia/main

- cecilia 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3052) 中提交了信息：add new content from OpenCS (#2)

- cecilia 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3005) 中提交了信息：add new content from OpenCS (#3)

### 周日 (8.24)

- cecilia 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3028) 中提交了信息：add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP2010) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP2010) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP2010) 中提交了信息：docs:add new content from OpenCS

- cecilia 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3054) 中提交了信息：add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP2010) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP2010) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP2010) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP2010) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP2010) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP2010) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3004) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3004) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP2010) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3053) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3053) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3053) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3053) 中提交了信息：docs:add new content from OpenCS

- cecilia 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3042) 中提交了信息：add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3007) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3002) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3002) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3002) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3011) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3011) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3011) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3013) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3013) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3013) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3013) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3013) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3013) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3013) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3006) 中提交了信息：docs:修改错误的学分

### 周六 (8.23)

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3006) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3006) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3010) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3010) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3010) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3010) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3010) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3010) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3010) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3010) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3005) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3001) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3001) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3001) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3001) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3001) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3001) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3001) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3040) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3018) 中提交了信息：docs:更改分数构成

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3009) 中提交了信息：docs:add new content from OpenCS

- JiaoZiang 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3018) 中提交了信息：docs:add new content from OpenCS
