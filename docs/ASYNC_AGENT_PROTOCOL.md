# ASYNC AGENT PROTOCOL

## Purpose
Enable multiple coding agents to work asynchronously without product drift, duplicated work, or conflicting changes.

## Mandatory reading order
Every agent must read, in order:
1. `AGENTS.md`
2. `docs/MASTER_TASK.md`
3. `docs/PROGRESS.md`
4. `docs/CONSTRAINTS.md`
5. this file
6. its assigned GitHub issue/task packet

## Work allocation model
Each agent receives one isolated task packet with:
- objective;
- owned files/directories;
- forbidden files/directories;
- acceptance criteria;
- exact deliverable;
- required tests/evidence;
- handoff format.

Agents must not self-expand scope.

## File ownership
Prefer non-overlapping ownership.

If two agents need the same file, one is designated owner; the other must propose a patch or note rather than editing it independently.

Current Phase 1.1 ownership recommendation:
- Agent A: integration/acceptance harness and fixture tooling.
- Agent B: Director JSON validation/schema compatibility tests.
- Agent C: CLI robustness and explicit failure-mode tests.
- Lead agent: merge decisions, PROGRESS/MASTER_TASK changes, acceptance gate.

## Branch/PR convention
Recommended branch names:
- `agent/a-acceptance-harness`
- `agent/b-schema-validation`
- `agent/c-cli-hardening`

Recommended PR title prefix:
- `[Agent A]`
- `[Agent B]`
- `[Agent C]`

## Forbidden async behavior
Agents may not:
- start Phase 2 renderer work before Phase 1.1 acceptance;
- rewrite PRD/vision to justify new features;
- change Director JSON schema incompatibly without approval;
- delete another agent's work to solve merge conflicts;
- claim runtime success without evidence;
- add cloud dependencies to solve local-first MVP problems without approval.

## Completion handoff format
Every agent must leave this exact information in its issue/PR:

### Handoff
- Task ID:
- Objective:
- Files changed:
- Commands run:
- Tests run and results:
- Acceptance criteria status:
- Known limitations:
- Merge/conflict notes:
- Recommended next action:

## Lead-agent merge gate
The lead agent accepts a worker result only when:
- scope stayed within contract;
- tests/evidence exist;
- no forbidden dependency or future-scope code was introduced;
- handoff is complete;
- repository truth docs are updated if the state materially changed.

## Progress truth
`docs/PROGRESS.md` is not a marketing status page. It must reflect the real state of the repository, including incomplete work and blockers.
