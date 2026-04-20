---
name: game-replica-dispatch
description: Generate dispatch-ready game remake plans from a game title, including (1) an overall milestone roadmap and (2) milestone-specific task lists split into Art, Code, and QA documents. Use when users ask to decompose a game into remake milestones, assign role-based tasks, define dependencies/handoffs/acceptance criteria, or save plans as standalone files for direct team dispatch.
---

# Game Replica Dispatch Skill

## Operating Rules

1. Assume scope is `core experience version` unless the user explicitly asks for higher fidelity, multiplayer, full content, or platform-specific variants.
2. Organize output by milestones, not by disconnected systems.
3. Split detailed assignments into exactly three roles:
- Art
- Code
- QA
4. Keep language short, direct, and executable. Avoid long conceptual explanations.
5. Prioritize parallel kickoff. Mark what can start now vs what must wait.
6. Write outputs for direct dispatch, not for teaching.
7. If the user prefers `document-first`, save files and return paths only.
8. Output documents must be fully in Chinese.
9. Use Chinese for all titles, section names, table headers, and field values unless proper nouns must stay in original language.

## Trigger Cues

Trigger when user intent matches any of:
1. Provide a game title and ask for remake decomposition.
2. Ask for an overall milestone plan.
3. Ask for role-specific assignments for a milestone.
4. Ask to save planning outputs into standalone files.
5. Explicitly say detailed content should be in files instead of chat.

## Workflow

### Step 1: Parse Request
Extract:
1. `game_name`
2. Ask type: overall plan, milestone task list, or both
3. Target milestone (for example `M1`)
4. Whether to save docs
5. Whether user asked for no inline detail

### Step 2: Build Overall Milestone Plan
Use this default phase structure:
1. `M1` Skeleton runnable
2. `M2` Core loop stable
3. `M3` Content reinforcement
4. `M4` Polish and optimization

For each milestone, include:
1. Stage goals
2. What must be completed
3. Acceptance criteria
4. Role-level progression order
5. Cross-role collaboration and handoff rules

### Step 3: Build Milestone Task Docs
Generate three separate docs for the requested milestone:
1. Art task list
2. Code task list
3. QA task list

Each doc must contain:
1. Stage goal
2. Must-complete items
3. Detailed task table
4. Execution order
5. Deliverable format
6. Naming convention
7. Receiver (who gets the output)
8. Done criteria
9. Blockers and dependencies
10. Start-now vs wait states

Execution-level requirements by role:
1. Art: specify required model/texture/UI/VFX items, counts, naming, formats, and handoff target.
2. Code: specify systems to implement, concrete feature scope, specs to provide Art first, package handoff to QA, and done criteria.
3. QA: specify smoke checklist, first regression scope, issue ticket format, what waits for code package, and what requires retest after art integration.

### Step 4: Save Documents
Default folder:
`D:\GJ\docs\dispatch\`

Default filenames:
1. `{game_name}_整体里程碑规划.md`
2. `{game_name}_{milestone}_美术任务清单.md`
3. `{game_name}_{milestone}_代码任务清单.md`
4. `{game_name}_{milestone}_测试任务清单.md`

Create folder if missing. Overwrite only when user intent implies regenerate/update.

### Step 5: Reply Format
If user asked not to show details inline:
1. Confirm saved
2. List file paths
3. Offer next document generation step

Otherwise:
1. Give short summary in chat
2. Still save files by default
3. Include paths

## Output Contracts

### Overall Plan Contract
Always include:
1. Project objective
2. Core gameplay loop
3. Milestone breakdown (`M1` to `M4`)
4. Stage-level acceptance criteria
5. Three-role coordination order
6. Dependency and handoff map
7. Chinese-only wording for headings and body content

### Role Task Contract
Every role document must explicitly answer:
1. What to do
2. How much to do
3. Naming rules
4. Output format
5. Deliver to whom
6. How to verify completion
7. Depends on whom
8. Can start now or must wait
9. Chinese-only wording for headings and body content

## Default Assumptions

1. Base on the game's core loop and minimum playable content slice.
2. Avoid auto-expanding to multiplayer/full campaign/high-fidelity unless asked.
3. Keep handoff chain explicit so team members know who blocks whom.

## Fast Behavior Rules

1. If user gives only game name, start with overall milestone plan.
2. If user asks for milestone task list, generate three role files for that milestone.
3. If user confirms doc-first preference, keep future replies short and path-centric.
4. Always generate concise Chinese in dispatch docs, regardless of chat language, unless user explicitly requests another language.

## Resources
Use `references/dispatch_doc_template.md` as the baseline layout for generated dispatch files.
