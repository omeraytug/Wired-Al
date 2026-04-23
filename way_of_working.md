# Way of working 

## Purpose

We collaborate to deliver Wired Al through shared ownership, small requests and frequent integration.


### Workflow
- Communication over Discord
- Create issues in git project when needed/relevant
- Daily check-ins

### Branching Strategy
- Main always deployable
- Feature branches only
- Pull Request required before merge
- No direct commits to main

**Example**:
```bash
feature/rag-ingestion
docs/readme
feature/streamlit-ui
```

### Commits
- Use conventional commit messages

**Example**:
```bash
"feat(api): new endpoint for chat"
"docs(readme): correct spelling of CHANGELOG"
```

### Pull Requests
- Small PRs preferred
- At least one reviewer


### Coding Conventions
- Limited comments in code
- Docstrings, typehints
- Comment when LLM-generated code used

### Decision Making
- Architectural changes discussed together
- If blocked >30min, ask team

### Meetings
- Start-of-session planning: 10 daily check in
- End-of-session status check: 10min

### Definition of Done
Task done when:
- code merged
- tested
- issue updated
- documented if relevant