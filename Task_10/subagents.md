# Claude Code Sub-Agents

## Folder Overview

![!\[structure\](structures.PNG)](screenshot/structures.PNG)

## Main Orchestrator Agent

File: agent.json

{
  "name": "book_orchestrator",
  "description": "Controls the full workflow of book creation using research, writing, editing, and formatting sub-agents.",
  "subagents": [
    "research_agent",
    "writing_agent",
    "editing_agent",
    "formatting_agent"
  ],
  "goal": "Produce a complete, well-structured book chapter."
}

### Purpose

This is the main controller that runs all sub-agents in sequence and ensures the complete book-writing workflow is executed properly.


## System Configuration File

File: config.json

{
  "version": "1.0",
  "agent": "agent.json",
  "subagents_directory": "subagents",
  "settings": {
    "load_subagents": true
  }
}


### Purpose

This file tells Claude Code:

where the main agent is

where the sub-agents are stored

and whether they should auto-load


## Sub-Agents

Each sub-agent focuses on one part of the book writing workflow.

## Research Agent

File: research.json

{
  "name": "research_agent",
  "description": "Collects topic research, key facts, and background information.",
  "goals": [
    "Find relevant research",
    "Summarize important facts",
    "Provide references for writing"
  ]
}

### Purpose

This agent gathers the topic information, extracts facts, and prepares research summaries for the writing process.


## Writing Agent

File: writing.json

{
  "name": "writing_agent",
  "description": "Writes the first draft of the chapter using the research notes.",
  "goals": [
    "Generate structured chapter content",
    "Follow the outline and flow",
    "Maintain clarity and coherence"
  ]
}


### Purpose

This agent uses the research to generate the chapter’s first draft.


## Editing Agent

File: editing.json

{
  "name": "editing_agent",
  "description": "Improves the chapter by fixing errors, enhancing clarity, and strengthening narrative flow.",
  "goals": [
    "Correct grammar",
    "Fix weak sentences",
    "Improve readability"
  ]
}

### Purpose

This agent fixes grammar, structure, and clarity issues.


## Formatting Agent

File: formatting.json

{
  "name": "formatting_agent",
  "description": "Formats the final output into a clean, organized chapter.",
  "goals": [
    "Apply formatting rules",
    "Organize headings, spacing, and layout",
    "Prepare chapter for publication"
  ]
}

### Purpose

This agent formats the final output into a polished chapter ready for reading.
