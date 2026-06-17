# Project Guidance

## Project Memory System

This project maintains institutional knowledge in `docs/project_notes/` for consistency across sessions.

### Memory Files

- **bugs.md** - Bug log with timestamps, solutions, and prevention notes
- **decisions.md** - Architectural decision index; concrete ADRs live in `docs/project_notes/decisions/`
- **key_facts.md** - Project configuration, ports, commands, important paths, and non-secret constants
- **issues.md** - Work log with timestamps, descriptions, and status
- **research.md** - Research log for questions explored, reasoning, and findings; grouped by session
- **OVERVIEW.md** - Generated project briefing for fast onboarding

### Timestamp Format

All new entries in every memory file use `YYYY-MM-DD HH:MM` format.
Research entries are additionally grouped under `## Session YYYY-MM-DD HH:MM — Topic` headers.

### Memory-Aware Protocols

Before proposing architectural changes:
- Check `docs/project_notes/decisions.md` and `docs/project_notes/decisions/` for existing decisions.
- Verify the proposed approach does not conflict with past choices.
- If it does conflict, acknowledge the existing decision and explain why a change is warranted.

When encountering errors or bugs:
- Search `docs/project_notes/bugs.md` for similar issues.
- Apply known solutions if found.
- Document new bugs and solutions when resolved.

When looking up project configuration:
- Check `docs/project_notes/key_facts.md` before assuming commands, ports, paths, or dependency choices.
- Do not store secrets, tokens, or real passwords in project memory.

When completing work:
- Log completed work in `docs/project_notes/issues.md`.
- Include timestamp, status, brief description, and related OpenSpec change when relevant.

Before re-investigating a question:
- Search `docs/project_notes/research.md` for the topic.
- Check timestamps to understand chronological context and avoid re-deciding settled questions.

When user requests memory updates:
- Update the appropriate memory file: bugs, decisions, key_facts, issues, or research.
- Use YAML front matter for new entries.
- Regenerate `docs/project_notes/OVERVIEW.md` after significant updates.
