Project Overview

This project simulates real-world email handling tasks using Python and OpenEnv. It classifies incoming emails, generates appropriate replies, decides whether to archive them, and computes task-based rewards for AI agents. The environment is designed for testing and deploying AI email triage solutions.

Objectives
* Classify emails as spam, normal, or urgent.
* Generate automated replies based on email content.
* Determine whether emails should be archived.
* Evaluate actions using reward metrics for AI agent training.
* Provide a reusable environment for AI experimentation and Hugging Face deployment.

Key Features
* Predefined email tasks: spam detection, meeting scheduling, complaint handling.
* Step-based environment with reset and reward computation.
* Modular design with separate files for environment, tasks, models, and grading.
* Supports AI model inference using Hugging Face/OpenAI APIs.
* Validation script to ensure compliance with OpenEnv standards.

Technology Stack
* Python (asyncio, Pydantic)
* OpenEnv framework
* Hugging Face API / OpenAI API
* Docker for containerized deployment
* CSV (optional for storing task results)

Dataset Description
* Tasks are predefined within tasks.py for simulation purposes.
* Includes email text, sender info, subject, and expected actions.
* Actions evaluated against labels (classification, reply, archive) for reward computation.
* No external datasets required; fully self-contained environment.

Expected Outcomes
* Accurate classification of emails based on content.
* Automated and contextually appropriate replies.
* Computation of reward metrics for AI evaluation.
* Reusable, modular environment suitable for AI training and benchmarking.
* Deployment-ready solution for Hugging Face Spaces.

Future Enhancements
* Integration with live email services for real-time testing.
* Expand tasks to include multi-step workflows or multi-agent simulations.
* Advanced reply generation using larger language models.
* Dashboard for monitoring performance and rewards.
* Support for multi-user email inbox simulations.
