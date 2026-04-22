# Unity Base Template

This folder defines the Unity baseline used for each local game instance.

## Target

1. Unity `2022.3 LTS`
2. Windows PC first
3. Single-player core loop first

## Included Baseline

1. Folder layout for `Assets`, `Packages`, `ProjectSettings`
2. Default package manifest with `Input System`
3. Starter scenes and script folders

## How to Use

1. Create local instance:
`powershell -ExecutionPolicy Bypass -File scripts/init_local_project.ps1 -GameName "<GameName>"`
2. Bootstrap Unity layout:
`powershell -ExecutionPolicy Bypass -File scripts/bootstrap_unity_project.ps1 -GameName "<GameName>"`

## Notes

1. This repo stores template only.
2. Real Unity project files are created under:
`local_projects/<GameName>/UnityProject`
