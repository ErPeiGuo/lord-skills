# Knowledge governance scenarios

These synthetic scenarios capture initialization, changed decisions and fresh-context recovery. They preserve the task shapes used during the skill's initial development; no client execution is performed merely by adding these files. The initial repository setup leaves Claude Code evaluation unrun.

## Initialize a knowledge root

Input: an empty temporary directory. Invoke the skill explicitly and give it this prompt:

> 在此目录建立工单导出功能的知识目录 docs/export。我们会继续讨论，现在先记录：已确认只导出 CSV、同步处理、最多 2 万行，超限直接拒绝；这样做是为了限制单请求内存。已否决异步队列，因为当前需求不需要后台任务。时区还没决定，不能默认 UTC。有人提过 XLSX，但我还没采纳。当前没有实现。先不写代码。

Evaluator checks: persist confirmed scope and rationale; retain the effective queue rejection; distinguish unresolved timezone and unapproved XLSX; claim no implementation. A small entry routes to current owners without duplicated contracts or irrelevant scaffolding. No source code is created.

## Update a confirmed decision

Input: copy the [fixture](fixtures/export-project/AGENTS.md) and its sibling files into a temporary workspace. Invoke the skill explicitly and give it this prompt:

> 继续 notes/index.md 下的导出知识。现在确认最大行数改为 5 万，因为客户正常工单量约 3 万，仍同步导出，CSV 范围不变。请马上更新相关知识，保留决策依据和可恢复的下一步；代码实施留到下一次。

Evaluator checks: approved target becomes 50,000 with its reason, while synchronous CSV and unresolved timezone remain intact. Source still enforces 20,000 and is not edited. Evidence keeps implementation distinct from the new target. Resume routing identifies the next implementation work without copying the whole contract. No default chronology is added to the live contract. Billing and unrelated paths remain unchanged.

## Recover with no conversation history

Input: the resulting workspace from the update scenario. Give a fresh read-only reader the workspace instructions and this prompt only; withhold this scenario file and prior chat:

> 从 notes/index.md 开始回答：当前批准的上限和原因是什么？代码实际上限是多少？能否声称 5 万行已经验证？下一步做什么？请给实际读取路径，别扫描 billing。

Evaluator checks: retrieves 50,000 as target and about 30,000 normal customer rows as rationale; retrieves 20,000 as implementation; does not claim 50,000 runtime verification. Identifies implementation and relevant boundary verification as next work. Reads the routed owners and necessary source only, without reading billing or changing files.
