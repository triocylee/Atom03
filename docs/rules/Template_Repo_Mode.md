# 模板仓库模式

## 目标

保证主仓库始终是“干净框架模板”，不夹带具体游戏实例数据。

## 规则

1. `projects/` 仅保留 `_template`。
2. 每次游戏实例必须创建在 `local_projects/<GameName>/`。
3. `local_projects/` 永不提交到仓库。
4. 帮手协作时默认基于模板文件工作，或基于本地实例快照工作。

## 初始化命令

```powershell
powershell -ExecutionPolicy Bypass -File scripts/init_local_project.ps1 -GameName "<GameName>"
```

## 验收

1. `git status` 不应出现 `local_projects/` 变更。
2. 主干提交只包含模板、规则、脚本改动。
