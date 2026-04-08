def compute_reward(task, action):
    reward = 0.0

    
    if action.classification.lower() == task["label"]:
        reward += 0.4

    
    if action.archive == task["archive"]:
        reward += 0.2

    
    reply = action.reply.lower()
    keywords = task["keywords"]

    if len(keywords) == 0:
        if reply.strip() == "":
            reward += 0.4
    else:
        matches = sum(1 for k in keywords if k in reply)
        reward += 0.4 * (matches / len(keywords))

    return min(reward, 1.0)
