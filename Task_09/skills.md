# Claude Code Custom Skills

## Folder overview

Task_09/screenshot/structure.PNG

## Agent Configuration

File: agent.json

{
  "name": "book_generation_agent",
  "description": "An agent designed to help with book creation by generating chapter outlines, building characters, and checking plot consistency.",
  "skills": [
    "chapter_outline_generator",
    "character_development_assistant",
    "plot_consistency_checker"
  ],
  "goals": [
    "Generate structured book content",
    "Assist with character development",
    "Maintain plot consistency and event clarity"
  ]
}

### Purpose

The agent configuration defines how the main agent behaves and what skills it can use.


## System Configuration

File: config.json

{
  "version": "1.0",
  "agent": "agent.json",
  "skills_directory": "skills",
  "settings": {
    "load_skills": true,
    "logging": true
  }
}

### Purpose 

This configuration ensures Claude Code can automatically detect and load all skill files.


## Custom Skills

## Chapter Outline Generator

File: chapter_outline_generator.ccskill

{
  "name": "chapter_outline_generator",
  "description": "Creates structured chapter outlines based on a topic, genre, or story direction.",
  "inputs": [
    {
      "name": "topic",
      "type": "string",
      "required": true
    },
    {
      "name": "genre",
      "type": "string",
      "required": false
    }
  ],
  "outputs": [
    {
      "name": "outline",
      "type": "object"
    }
  ]
}

### Purpose 

Generates chapter outlines from the given topic and genre, ensuring a clear story structure.


## Character Development Assistant

File: character_development_assistant.ccskill

{
  "name": "character_development_assistant",
  "description": "Helps build detailed and consistent characters, including personality, background, and goals.",
  "inputs": [
    {
      "name": "character_name",
      "type": "string",
      "required": true
    },
    {
      "name": "story_context",
      "type": "string",
      "required": false
    }
  ],
  "outputs": [
    {
      "name": "character_profile",
      "type": "object"
    }
  ]
}

### Purpose 

Generates character backgrounds, personality traits, and development arcs.


## Plot Consistency Checker

File: plot_consistency_checker.ccskill

{
  "name": "plot_consistency_checker",
  "description": "Analyzes story events, checks for inconsistencies, missing links, timeline errors, and logical gaps.",
  "inputs": [
    {
      "name": "story_text",
      "type": "string",
      "required": true
    }
  ],
  "outputs": [
    {
      "name": "issues",
      "type": "array"
    }
  ]
}


### Purpose 

Detects plot holes, missing details, and timeline problems inside a story.