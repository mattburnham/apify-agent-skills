#!/bin/bash
# Claude Code PreToolUse hook - runs version bump before git commit
# This script receives tool input JSON on stdin

# Read tool input
INPUT=$(cat)

# Extract the bash command
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // ""')

# Quick exit if not a git commit command
if ! echo "$COMMAND" | grep -qE 'git\s+commit'; then
    exit 0
fi

# Extract commit message from -m "message" or -m 'message'
COMMIT_MSG=$(echo "$COMMAND" | grep -oE '\-m\s+["'"'"'][^"'"'"']+["'"'"']' | sed -E 's/-m\s+["'"'"'](.*)["'"'"']/\1/' | head -1)

# If no message found, skip bump (might be interactive commit)
if [ -z "$COMMIT_MSG" ]; then
    exit 0
fi

# Run version bump
cd "$CLAUDE_PROJECT_DIR" 2>/dev/null || cd "$(dirname "$0")/../.."
uv run scripts/generate_agents.py --bump "$COMMIT_MSG"

# Stage any modified version files
git add -u .claude-plugin/marketplace.json .claude-plugin/plugin.json 2>/dev/null
git add -u skills/*/reference/scripts/run_actor.py 2>/dev/null

exit 0
