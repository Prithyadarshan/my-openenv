Email Triage OpenEnv

Simulates real-world email handling tasks (spam detection, meeting scheduling, complaint handling) using Python and OpenEnv.

Functional Requirements
Classify emails: spam / normal / urgent
Generate appropriate reply
Decide whether to archive email
Track steps & compute reward
Reset & reuse environment
Project Structure
openenv-email-agent/
├── env/
│   ├── environment.py
│   ├── models.py
│   ├── tasks.py
│   └── grader.py
├── inference.py
├── openenv.yaml
├── Dockerfile
├── requirements.txt
├── README.md
└── scripts/
    └── validate-submission.sh
Classes & Files
EmailEnv – reset, step, state, close
Models – Observation, Action, StepResult
Grader – computes rewards
Tasks – predefined email tasks
Inference – runs tasks using HF/OpenAI model
Run

Locally:

pip install -r requirements.txt
python inference.py

Docker:

docker build -t email-env .
docker run email-env

Validation:

chmod +x scripts/validate-submission.sh
./scripts/validate-submission.sh https://your-space-name.hf.space
