# lord-skills · lord-技能库

持续维护的个人 Agent Skills 集合。每个 `lord-*` 技能提供独立能力，按客户端适配和验证，可以单独安装使用。

技能指令与所治理的知识面向 AI；本页面向安装者，说明能力、安装和支持状态。

## 技能目录

| Skill | 用途 | Codex | Claude Code |
| --- | --- | --- | --- |
| [lord-文档知识治理](skills/lord-doc-knowledge-governance/SKILL.md) | 渐进读取、确认决定落盘、知识维护与跨会话恢复 | 已有全局安装；仅手动调用 | 预留扩展，尚未适配或验证 |

## Codex 安装与调用

在仓库内容发布到 GitHub 后，可以让 Codex 的 Skill Installer 从具体目录安装：

```text
$skill-installer install https://github.com/ErPeiGuo/lord-skills/tree/main/skills/lord-doc-knowledge-governance
```

然后显式调用，后面用自然语言说明任务：

```text
$lord-doc-knowledge-governance 接下来讨论新功能，请及时记录已确认的重要决定。
```

每个技能的调用方式由其配置独立声明。当前文档知识治理技能在 `agents/openai.yaml` 中关闭隐式调用；同一任务启动后持续维护，无需每次记录重新调用。

仓库是维护源，全局技能目录是安装副本。修改仓库后再更新安装副本；避免同时安装同名 Skill 的直接版本和插件版本。

## 客户端与发布边界

- 核心指导及参考资料维护在 `skills/<name>/`；每个技能标明实际支持的客户端。
- [Codex 插件清单](.codex-plugin/plugin.json)指向同一份 `skills/`，目前仅完成结构准备，尚未做插件安装验证或发布市场索引。当前使用上述单技能安装方式。
- [Claude Code 扩展入口](.claude-plugin/README.md)记录后续适配要求。尚无可安装的 Claude Code 插件清单，不承诺 Claude Code 或 Claude 网页版兼容性。
- 发布时以 Git 标签标识版本；当前仓库初始化尚未形成版本发布。

## 仓库结构

```text
skills/                 独立技能的唯一维护源
.codex-plugin/          Codex 发布配置
.claude-plugin/         Claude Code 扩展规划
evals/<skill>/          行为场景、输入材料与判断标准
scripts/                仓库结构检查
.github/workflows/      自动执行结构检查
AGENTS.md               AI 维护本仓库的共同规则
CLAUDE.md               Claude Code 的共同规则入口
```

新增技能放入 `skills/lord-<name>/`。只创建实际需要的 `references/`、`scripts/` 或 `assets/`；未来需要分类时先在目录表中分组。

## 检查与演进

```sh
python3 -m pip install -r scripts/requirements.txt
python3 scripts/check_repository.py
```

结构检查验证元数据、引用和打包路径，不替代实际行为验证。行为变化使用 [evals](evals/README.md) 下对应场景，客户端结果分别记录。

技能方法的来源保留在各自参考资料中。本仓库原创内容采用 [MIT License](LICENSE)；外部链接内容遵循各自许可。
