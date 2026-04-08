from env.models import Observation, StepResult
from env.tasks import TASKS
from env.grader import compute_reward

class EmailEnv:

    def __init__(self, task_name="spam_detection"):
        self.task_name = task_name
        self.task = TASKS[task_name]
        self.done = False
        self.step_count = 0

    async def reset(self):
        self.done = False
        self.step_count = 0

        return StepResult(
            observation=Observation(
                email_text=self.task["email"],
                sender="user@example.com",
                subject="Inbox",
                step=0
            ),
            reward=0.0,
            done=False,
            info={}
        )

    async def step(self, action):
        if self.done:
            return await self.reset()

        self.step_count += 1

        reward = compute_reward(self.task, action)
        self.done = True

        return StepResult(
            observation=Observation(
                email_text="",
                sender="",
                subject="",
                step=self.step_count
            ),
            reward=reward,
            done=True,
            info={}
        )

    async def state(self):
        return {
            "task": self.task_name,
            "step": self.step_count
        }

    async def close(self):
        pass
