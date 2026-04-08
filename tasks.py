TASKS = {
    "spam_detection": {
        "email": "Congratulations! You won $1000. Click here.",
        "label": "spam",
        "archive": True,
        "keywords": []
    },
    "meeting_schedule": {
        "email": "Can we meet tomorrow at 3 PM?",
        "label": "normal",
        "archive": False,
        "keywords": ["confirm", "3 pm"]
    },
    "complaint_handling": {
        "email": "My order hasn’t arrived in 10 days. Very disappointed.",
        "label": "urgent",
        "archive": False,
        "keywords": ["sorry", "refund", "track"]
    }
}
