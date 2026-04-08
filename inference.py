import asyncio
import os
from openai import OpenAI

from env.environment import EmailEnv
from env.models import Action

API_KEY = os.getenv("HF_TOKEN")
API_BASE_URL = os.getenv("API_BASE_URL", "https://router.huggingface.co/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "Qwen/Qwen2.5-72B-Instruct")

TASKS = ["spam_detection", "meeting_schedule", "complaint_handling"]

def log_start(task):
    print(f"[START] task={task} env=email_env model={MODEL_NAME}", flush=True)

def log_step(step, action, reward, done):
    print(f"[STEP] step={step} action={action} reward={reward:.2f} done={str(done).lower()} error=null", flush=True)

def log_end(success, steps, score, rewards):
    rewards_str = ",".join(f"{r:.2f}" for r in rewards)
    print(f"[END] success={str(success).lower()} steps={steps} score={score:.2f} rewards={rewards_str}", flush=True)

def get_action(client, email):
    prompt = f"""
    Read the email and respond in this format:
    classification|reply|archive(true/false)

    Email:
    {email}
    """

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
        )

        text = response.choices[0].message.content.strip()
        c, r, a = text.split("|")

        return Action(
            classification=c.strip(),
            reply=r.strip(),
            archive=a.strip().lower() == "true"
        )
    except:
        return Action(classification="normal", reply="ok", archive=False)

async def run_task(task_name):
    client = OpenAI(base_url=API_BASE_URL, api_key=API_KEY)
    env = EmailEnv(task_name)

    log_start(task_name)

    rewards = []
    result = await env.reset()

    action = get_action(client, result.observation.email_text)
    result = await env.step(action)

    rewards.append(result.reward)
    log_step(1, str(action), result.reward, result.done)

    score = rewards[0]
    success = score > 0.5

    log_end(success, 1, score, rewards)

    await env.close()

async def main():
    for task in TASKS:
        await run_task(task)

if __name__ == "__main__":
    asyncio.run(main())
