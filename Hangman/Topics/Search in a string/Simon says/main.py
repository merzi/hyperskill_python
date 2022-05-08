def what_to_do(instructions):
    instruction_pattern = "Simon says"
    if instructions.startswith(instruction_pattern) or instructions.endswith(instruction_pattern):
        activity = instructions.replace(instruction_pattern, '').strip()
        return f"I {activity}"
    return "I won't do it!"
