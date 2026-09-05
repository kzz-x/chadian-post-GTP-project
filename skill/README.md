# 差点后期 Skill

这是 `kzz-x/chadian-post-GTP-project` 的 Skill 入口说明。

## 结构

- `SKILL.md`：唯一运行入口，负责阶段机、短指令语义、路由和按需读取规则。
- `project/01_项目指令.md`：项目级总规则。
- `project/来源/`：10 个专业 reference，按任务需要读取，不一次全量加载。
- `skill/REGRESSION.md`：行为回归测试清单，仅用于测试与验收。
- `archives/`：历史归档，仅版本恢复时读取。

## 使用原则

真正使用这个 Skill 时，应把整个仓库/Skill 文件夹作为一个能力包提供给支持 Skills 的环境，让模型从 `SKILL.md` 开始执行。

收到完整文案时默认停在 A 全文分析；“展开03”进入 B 设计；“制作03”才进入 C；“不好看/只改XX”进入 D。

不要把 `project/` 下 10 个来源重新复制进 `SKILL.md`。主 Skill 只做调度，专业细节始终以原 reference 为单一真源，避免两套规则漂移。