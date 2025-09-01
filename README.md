# AI Deep Research Agent

Multi-agent AI research system that automates comprehensive topic research through intelligent planning, web searching, report synthesis, and email distribution using OpenAI's Agent SDK.

## Project Overview

This project demonstrates a sophisticated multi-agent system that automates the entire research workflow - from initial query planning to final report delivery. The system uses 5 specialized AI agents working in coordination to produce publication-quality research reports.

## Architecture

### Core Agents

- **Research Manager** - Orchestrates the entire workflow and coordinates agent interactions
- **Planner Agent** - Creates strategic search plans with 5 targeted web queries
- **Search Agent** - Performs concurrent web searches and generates concise summaries
- **Writer Agent** - Synthesizes research into comprehensive 1000+ word markdown reports
- **Email Agent** - Formats reports as HTML and handles email distribution

### Workflow Pipeline

```
Query Input → Planning → Parallel Searching → Report Writing → Email Delivery
```

## Features

- **Intelligent Search Planning** - AI-generated search strategies with reasoning
- **Concurrent Web Searching** - Parallel execution for faster results
- **Structured Outputs** - Pydantic models for reliable data handling
- **Comprehensive Reports** - Detailed markdown reports with follow-up questions
- **Web Interface** - Gradio UI for easy interaction
- **Email Integration** - Automated HTML email delivery via SendGrid
- **OpenAI Tracing** - Built-in monitoring and debugging capabilities

## Cost Considerations

- OpenAI WebSearchTool: ~$0.025 per search call
- Typical research session: $2-3 for comprehensive reports
- Alternative free search tools available for cost-sensitive usage

## Learning Outcomes

This project demonstrates:

- **Multi-Agent Orchestration** - Coordinated AI agent workflows
- **Structured Outputs** - Pydantic models for reliable data handling
- **Async Processing** - Concurrent operations for performance
- **Tool Integration** - External service integration patterns
- **Workflow Design** - End-to-end automation architecture

## Technical Stack

- **OpenAI Agent SDK** - Core agent framework
- **GPT-4o-mini** - Language model for all agents
- **Gradio** - Web interface framework
- **SMTP (Gmail)** - Email delivery service
- **Pydantic** - Data validation and structured outputs
- **asyncio** - Asynchronous processing
