---
authors:
  - image: https://github.com/openai.png
    link: https://github.com/openai
    name: ChatGPT
date: "2025-09-05"
draft: false
excludeSearch: false
title: AUTO 周报 2025-08-29 - 2025-09-05
---

## 本周更新摘要

- 平台/仓库管理（repos-management）
  - 更新与重构：CI 仓库列表由自动任务更新；移除未使用的 token 获取逻辑并精简 PR 标记；新增“删除文件夹”功能；修复工作流中的条件表达式转义问题。

- 大规模 CI 统一化与仓库清理（影响范围广）
  - 多数课程仓库采用了统一的可复用 GitHub Actions workflow，且有多次由自动化脚本更新 worktree.json。
  - 批量清理：大量仓库删除了无用的 '.hoa' 目录（例：多门 COMP、AUTO、EE、MATH、MECH、通识与体育等课程），属例行清理/CI 适配操作。

- 课程内容迁移与补充（OpenCS 内容合并）
  - 多门计算机相关课程已迁移/合并来自 OpenCS 的仓库内容（包括但不限于 COMP3030、COMP3043、COMP3059、COMP3060、COMP2012、COMP2008、COMP2052 等），完成教材/代码/课程仓库的整合。
  - 若干课程补充或更新了说明、学分与成绩构成（例如 COMP3030 修改学分；COMP3060 更新成绩构成；COMP2029 补充课程说明；COMP3052 更新课程信息）。

- 新建/初始化仓库与课程信息
  - 新仓/初始提交：EE304X（添加课程信息并初次提交）、COMP3043（初次提交）等，完成课程仓库搭建或内容初始化。

- 个别课程显著更新
  - 自动控制理论 A/B（AUTO3001A/B）：更新 Badge 样式，同时也受到统一 CI workflow 影响。
  - 文理通识课程体系（GeneralKnowledge）：新增“自救群共享文档/课程评价”板块。

- 其它零星改动
  - 少量 README 删除、文件重命名或格式微调等常规维护操作已合并，无需逐一列出。

（注：已将多条类似的 CI/清理/迁移操作合并汇总，便于快速查看本周主要变动。）

## 更新内容

### 周五 (9.5)

- Kowyo 在 [自动控制理论 B](https://github.com/HITSZ-OpenAuto/AUTO3001B) 中提交了信息：更新 Badge 样式 (#21)

- Kowyo 在 [自动控制理论 A](https://github.com/HITSZ-OpenAuto/AUTO3001A) 中提交了信息：更新 Badge 样式 (#26)

### 周四 (9.4)

- GitHub Actions 在 [repos-management](https://github.com/HITSZ-OpenAuto/repos-management) 中提交了信息：ci: update repositories list [automated]

- IcyDesert 在 [repos-management](https://github.com/HITSZ-OpenAuto/repos-management) 中提交了信息：fix: delete problematic equation in if-condition

- W·D·Gaster 在 [文理通识课程体系](https://github.com/HITSZ-OpenAuto/GeneralKnowledge) 中提交了信息：添加自救群共享文档部分课程评价 (#11)

- W·D·Gaster 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/EE304X) 中提交了信息：添加课程信息

- W·D·Gaster 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/EE304X) 中提交了信息：Initial commit

### 周三 (9.3)

- W·D·Gaster 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3030) 中提交了信息：修改学分

- W·D·Gaster 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3030) 中提交了信息：迁移 OpenCS 对应仓库内容

- GitHub Actions 在 [repos-management](https://github.com/HITSZ-OpenAuto/repos-management) 中提交了信息：ci: update repositories list [automated]

- W·D·Gaster 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3043) 中提交了信息：迁移 OpenCS 对应课程

- W·D·Gaster 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3043) 中提交了信息：Initial commit

- W·D·Gaster 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3044) 中提交了信息：更新相关内容

- W·D·Gaster 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP2029) 中提交了信息：补充课程相关说明

- W·D·Gaster 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3060) 中提交了信息：更新成绩构成

- W·D·Gaster 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3060) 中提交了信息：将 OpenCS 软 A 仓库迁移

### 周二 (9.2)

- W·D·Gaster 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3059) 中提交了信息：将 OpenCS 的面向对象的软件构造导论仓库迁移

- W·D·Gaster 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP2012) 中提交了信息：迁移 OpenCS 对应仓库

- W·D·Gaster 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP2008) 中提交了信息：迁移 OpenCS 对应仓库内容

- W·D·Gaster 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP2052) 中提交了信息：迁移对应仓库内容

### 周一 (9.1)

- cecilia 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3052) 中提交了信息：update COMP3052's information (#5)

- Kowyo 在 [repos-management](https://github.com/HITSZ-OpenAuto/repos-management) 中提交了信息：feat: add delete folder

### 周五 (8.29)

- IcyDesert 在 [微积分 B](https://github.com/HITSZ-OpenAuto/MATH1015B) 中提交了信息： [automated-generated-PR] ci: updated worktree.json generation (#15)

- IcyDesert 在 [机械设计基础](https://github.com/HITSZ-OpenAuto/MECH2010) 中提交了信息： [automated-generated-PR] ci: updated worktree.json generation (#10)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3005) 中提交了信息：ci: delete '.hoa' directory (#5)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3042) 中提交了信息：ci: delete '.hoa' directory (#6)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3039) 中提交了信息：ci: delete '.hoa' directory (#2)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3054) 中提交了信息：ci: delete '.hoa' directory (#4)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3021) 中提交了信息：ci: delete '.hoa' directory (#4)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3029) 中提交了信息：ci: delete '.hoa' directory (#3)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3019) 中提交了信息：ci: delete '.hoa' directory (#4)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3018) 中提交了信息：ci: delete '.hoa' directory (#3)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3017) 中提交了信息：ci: delete '.hoa' directory (#3)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3028) 中提交了信息：ci: delete '.hoa' directory (#4)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3030) 中提交了信息：ci: delete '.hoa' directory (#2)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3006) 中提交了信息：ci: delete '.hoa' directory (#3)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3053) 中提交了信息：ci: delete '.hoa' directory (#3)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3002) 中提交了信息：ci: delete '.hoa' directory (#3)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3009) 中提交了信息：ci: delete '.hoa' directory (#3)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3044) 中提交了信息：ci: delete '.hoa' directory (#2)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3007) 中提交了信息：ci: delete '.hoa' directory (#4)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3040) 中提交了信息：ci: delete '.hoa' directory (#3)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3004) 中提交了信息：ci: delete '.hoa' directory (#3)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3011) 中提交了信息：ci: delete '.hoa' directory (#3)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP2010) 中提交了信息：ci: delete '.hoa' directory (#3)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP2029) 中提交了信息：ci: delete '.hoa' directory (#2)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3060) 中提交了信息：ci: delete '.hoa' directory (#2)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3010) 中提交了信息：ci: delete '.hoa' directory (#3)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3013) 中提交了信息：ci: delete '.hoa' directory (#3)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3001) 中提交了信息：ci: delete '.hoa' directory (#3)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3003) 中提交了信息：ci: delete '.hoa' directory (#4)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3059) 中提交了信息：ci: delete '.hoa' directory (#2)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP2012) 中提交了信息：ci: delete '.hoa' directory (#3)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP2008) 中提交了信息：ci: delete '.hoa' directory (#2)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP2052) 中提交了信息：ci: delete '.hoa' directory (#2)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP3052) 中提交了信息：ci: delete '.hoa' directory (#4)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP2051) 中提交了信息：ci: delete '.hoa' directory (#3)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/COMP2030) 中提交了信息：ci: delete '.hoa' directory (#3)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/MATH4002) 中提交了信息：ci: delete '.hoa' directory (#2)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/MECH2022) 中提交了信息：ci: delete '.hoa' directory (#2)

- Kowyo 在 [设计与制造 A](https://github.com/HITSZ-OpenAuto/MECH2019) 中提交了信息：ci: delete '.hoa' directory (#4)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/EE3002) 中提交了信息：ci: delete '.hoa' directory (#5)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/EE3015) 中提交了信息：ci: delete '.hoa' directory (#6)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/EE3001) 中提交了信息：ci: delete '.hoa' directory (#6)

- Kowyo 在 [电磁场](https://github.com/HITSZ-OpenAuto/EE2003) 中提交了信息：ci: delete '.hoa' directory (#5)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/MATH4001) 中提交了信息：ci: delete '.hoa' directory (#6)

- Kowyo 在 [习近平新时代中国特色社会主义思想概论](https://github.com/HITSZ-OpenAuto/GEIP1017) 中提交了信息：ci: delete '.hoa' directory (#9)

- Kowyo 在 [思想道德与法治](https://github.com/HITSZ-OpenAuto/GEIP1015) 中提交了信息：ci: delete '.hoa' directory (#10)

- Kowyo 在 [中国科技史话](https://github.com/HITSZ-OpenAuto/SEIN1040) 中提交了信息：ci: delete '.hoa' directory (#6)

- Kowyo 在 [跨专业选修课程体系](https://github.com/HITSZ-OpenAuto/CrossSpecialty) 中提交了信息：ci: delete '.hoa' directory (#8)

- Kowyo 在 [普通天文学](https://github.com/HITSZ-OpenAuto/SPST1004) 中提交了信息：ci: delete '.hoa' directory (#8)

- Kowyo 在 [工程训练（金工实习）](https://github.com/HITSZ-OpenAuto/ENGG1002) 中提交了信息：ci: delete '.hoa' directory (#8)

- Kowyo 在 [工程训练（电子工艺实习）](https://github.com/HITSZ-OpenAuto/ENGG1003) 中提交了信息：ci: delete '.hoa' directory (#10)

- Kowyo 在 [高等电路与电子分析](https://github.com/HITSZ-OpenAuto/EE2004) 中提交了信息：ci: delete '.hoa' directory (#10)

- Kowyo 在 [数值分析](https://github.com/HITSZ-OpenAuto/MATH4004) 中提交了信息：ci: delete '.hoa' directory (#8)

- Kowyo 在 [移动机器人导论](https://github.com/HITSZ-OpenAuto/AUTO3012) 中提交了信息：ci: delete '.hoa' directory (#9)

- Kowyo 在 [文理通识课程体系](https://github.com/HITSZ-OpenAuto/GeneralKnowledge) 中提交了信息：ci: delete '.hoa' directory (#13)

- Kowyo 在 [写作与沟通](https://github.com/HITSZ-OpenAuto/WRIT0001) 中提交了信息：ci: delete '.hoa' directory (#8)

- Kowyo 在 [机器学习概论](https://github.com/HITSZ-OpenAuto/AUTO3019) 中提交了信息：ci: delete '.hoa' directory (#9)

- Kowyo 在 [日语 I](https://github.com/HITSZ-OpenAuto/WOCD1008) 中提交了信息：ci: delete '.hoa' directory (#7)

- Kowyo 在 [运动控制系统](https://github.com/HITSZ-OpenAuto/AUTO3011) 中提交了信息：ci: delete '.hoa' directory (#10)

- Kowyo 在 [模式识别](https://github.com/HITSZ-OpenAuto/AUTO5024) 中提交了信息：ci: delete '.hoa' directory (#12)

- Kowyo 在 [嵌入式系统](https://github.com/HITSZ-OpenAuto/AUTO3024) 中提交了信息：ci: delete '.hoa' directory (#9)

- Kowyo 在 [非线性与自适应控制](https://github.com/HITSZ-OpenAuto/AUTO5005) 中提交了信息：ci: delete '.hoa' directory (#9)

- Kowyo 在 [系统辨识](https://github.com/HITSZ-OpenAuto/AUTO5002) 中提交了信息：ci: delete '.hoa' directory (#7)

- Kowyo 在 [线性系统理论](https://github.com/HITSZ-OpenAuto/AUTO5001) 中提交了信息：ci: delete '.hoa' directory (#10)

- Kowyo 在 [毕业设计](https://github.com/HITSZ-OpenAuto/AUTO3099) 中提交了信息：ci: delete '.hoa' directory (#14)

- Kowyo 在 [机器视觉](https://github.com/HITSZ-OpenAuto/AUTO3006) 中提交了信息：ci: delete '.hoa' directory (#15)

- Kowyo 在 [自动控制实践 B](https://github.com/HITSZ-OpenAuto/AUTO3002B) 中提交了信息：ci: delete '.hoa' directory (#19)

- Kowyo 在 [自动控制理论 B](https://github.com/HITSZ-OpenAuto/AUTO3001B) 中提交了信息：ci: delete '.hoa' directory (#20)

- Kowyo 在 [凸优化与最优控制](https://github.com/HITSZ-OpenAuto/AUTO5023) 中提交了信息：ci: delete '.hoa' directory (#12)

- Kowyo 在 [创新训练课 A](https://github.com/HITSZ-OpenAuto/AUTO2003A) 中提交了信息：ci: delete '.hoa' directory (#9)

- Kowyo 在 [电路与电子技术实验](https://github.com/HITSZ-OpenAuto/EE1014) 中提交了信息：ci: delete '.hoa' directory (#12)

- Kowyo 在 [体育](https://github.com/HITSZ-OpenAuto/PE100X) 中提交了信息：ci: delete '.hoa' directory (#21)

- Kowyo 在 [电路与电子学](https://github.com/HITSZ-OpenAuto/EE1013) 中提交了信息：ci: delete '.hoa' directory (#14)

- Kowyo 在 [微积分 A](https://github.com/HITSZ-OpenAuto/MATH1015A) 中提交了信息：ci: delete '.hoa' directory (#20)

- Kowyo 在 [电路 IA](https://github.com/HITSZ-OpenAuto/EE1011A) 中提交了信息：ci: delete '.hoa' directory (#15)

- Kowyo 在 [自动控制理论 A](https://github.com/HITSZ-OpenAuto/AUTO3001A) 中提交了信息：ci: delete '.hoa' directory (#25)

- Kowyo 在 [最优估计](https://github.com/HITSZ-OpenAuto/AUTO5013) 中提交了信息：ci: delete '.hoa' directory (#12)

- Kowyo 在 [自动化领域专家系列讲座](https://github.com/HITSZ-OpenAuto/AUTO3022) 中提交了信息：ci: delete '.hoa' directory (#10)

- Kowyo 在 [MOOC](https://github.com/HITSZ-OpenAuto/MOOC) 中提交了信息：ci: delete '.hoa' directory (#16)

- Kowyo 在 [机械设计基础](https://github.com/HITSZ-OpenAuto/MECH2010) 中提交了信息：ci: delete '.hoa' directory (#11)

- Kowyo 在 [微积分 B](https://github.com/HITSZ-OpenAuto/MATH1015B) 中提交了信息：ci: delete '.hoa' directory (#16)

- Kowyo 在 [电路实验 IA](https://github.com/HITSZ-OpenAuto/EE1012A) 中提交了信息：ci: delete '.hoa' directory (#11)

- Kowyo 在 [大学英语](https://github.com/HITSZ-OpenAuto/LANG100X) 中提交了信息：ci: delete '.hoa' directory (#13)

- Kowyo 在 [大学物理](https://github.com/HITSZ-OpenAuto/PHYS1001) 中提交了信息：ci: delete '.hoa' directory (#19)

- Kowyo 在 [创新训练课 B](https://github.com/HITSZ-OpenAuto/AUTO2003B) 中提交了信息：ci: delete '.hoa' directory (#16)

- Kowyo 在 [中国近现代史纲要](https://github.com/HITSZ-OpenAuto/GEIP1016) 中提交了信息：ci: delete '.hoa' directory (#16)

- Kowyo 在 [马克思主义基本原理](https://github.com/HITSZ-OpenAuto/GEIP1011) 中提交了信息：ci: delete '.hoa' directory (#27)

- Kowyo 在 [电路实验 IB](https://github.com/HITSZ-OpenAuto/EE1012B) 中提交了信息：ci: delete '.hoa' directory (#13)

- Kowyo 在 [自动化认知与实践](https://github.com/HITSZ-OpenAuto/AUTO1001) 中提交了信息：ci: delete '.hoa' directory (#25)

- Kowyo 在 [经济学原理](https://github.com/HITSZ-OpenAuto/ECON2005F) 中提交了信息：ci: delete '.hoa' directory (#9)

- Kowyo 在 [理论力学Ⅱ](https://github.com/HITSZ-OpenAuto/EMEC1002) 中提交了信息：ci: delete '.hoa' directory (#15)

- Kowyo 在 [毛泽东思想和中国特色社会主义理论体系概论](https://github.com/HITSZ-OpenAuto/GEIP1018) 中提交了信息：ci: delete '.hoa' directory (#13)

- Kowyo 在 [模拟电子技术实验](https://github.com/HITSZ-OpenAuto/EE1008) 中提交了信息：ci: delete '.hoa' directory (#11)

- Kowyo 在 [数字电子技术实验](https://github.com/HITSZ-OpenAuto/EE1010) 中提交了信息：ci: delete '.hoa' directory (#11)

- Kowyo 在 [数字电子技术基础](https://github.com/HITSZ-OpenAuto/EE1009) 中提交了信息：ci: delete '.hoa' directory (#21)

- Kowyo 在 [模拟电子技术基础](https://github.com/HITSZ-OpenAuto/EE1007) 中提交了信息：ci: delete '.hoa' directory (#19)

- Kowyo 在 [控制理论中的代数基础](https://github.com/HITSZ-OpenAuto/AUTO2006) 中提交了信息：ci: delete '.hoa' directory (#15)

- Kowyo 在 [DSP 的原理与应用](https://github.com/HITSZ-OpenAuto/EE3005) 中提交了信息：ci: delete '.hoa' directory (#9)

- Kowyo 在 [代数与几何](https://github.com/HITSZ-OpenAuto/MATH1002) 中提交了信息：ci: delete '.hoa' directory (#21)

- Kowyo 在 [自动控制实践 A 实验](https://github.com/HITSZ-OpenAuto/AUTO3016) 中提交了信息：ci: delete '.hoa' directory (#20)

- Kowyo 在 [机器人学导论](https://github.com/HITSZ-OpenAuto/AUTO3005) 中提交了信息：ci: delete '.hoa' directory (#18)

- Kowyo 在 [C++ 语言程序设计](https://github.com/HITSZ-OpenAuto/COMP2014) 中提交了信息：ci: delete '.hoa' directory (#12)

- Kowyo 在 [程序设计思维与实践](https://github.com/HITSZ-OpenAuto/COMP1011) 中提交了信息：ci: delete '.hoa' directory (#15)

- Kowyo 在 [数学规划与数值优化](https://github.com/HITSZ-OpenAuto/AUTO3028) 中提交了信息：ci: delete '.hoa' directory (#12)

- Kowyo 在 [数据结构与算法](https://github.com/HITSZ-OpenAuto/COMP2050) 中提交了信息：ci: delete '.hoa' directory (#11)

- Kowyo 在 [过程控制系统](https://github.com/HITSZ-OpenAuto/AUTO3007) 中提交了信息：ci: delete '.hoa' directory (#23)

- Kowyo 在 [电路 IB](https://github.com/HITSZ-OpenAuto/EE1011B) 中提交了信息：ci: delete '.hoa' directory (#19)

- Kowyo 在 [概率论与数理统计](https://github.com/HITSZ-OpenAuto/MATH1004) 中提交了信息：ci: delete '.hoa' directory (#23)

- Kowyo 在 [复变函数与积分变换](https://github.com/HITSZ-OpenAuto/MATH1005) 中提交了信息：ci: delete '.hoa' directory (#24)

- Kowyo 在 [系统建模与仿真](https://github.com/HITSZ-OpenAuto/AUTO3004) 中提交了信息：ci: delete '.hoa' directory (#18)

- Kowyo 在 [数字图像处理](https://github.com/HITSZ-OpenAuto/AUTO3003) 中提交了信息：ci: delete '.hoa' directory (#20)

- Kowyo 在 [信号分析与处理](https://github.com/HITSZ-OpenAuto/AUTO2005) 中提交了信息：ci: delete '.hoa' directory (#27)

- Kowyo 在 [大学化学 III](https://github.com/HITSZ-OpenAuto/CHEM1012) 中提交了信息：ci: delete '.hoa' directory (#10)

- Kowyo 在 [自动控制实践 A](https://github.com/HITSZ-OpenAuto/AUTO3002A) 中提交了信息：ci: delete '.hoa' directory (#36)

- Kowyo 在 [（示例）大学物理实验](https://github.com/HITSZ-OpenAuto/course-template) 中提交了信息：ci: delete '.hoa' directory (#17)

- Kowyo 在 [repos-management](https://github.com/HITSZ-OpenAuto/repos-management) 中提交了信息：refactor: remove unused personal access token sourcing and streamline PR marker definition (#9)

- Kowyo 在 [repos-management](https://github.com/HITSZ-OpenAuto/repos-management) 中提交了信息：refactor: remove unused personal access token sourcing and streamline PR marker definition

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
