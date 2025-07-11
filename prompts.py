def get_tech_questions_prompt(tech_stack):
    return f"""
    You are an AI technical interviewer.
    Generate 3 to 5 technical interview questions for a candidate skilled in: {tech_stack}.
    The questions should test practical and core knowledge, and be suitable for someone with 1-3 years of experience.
    Format the output cleanly using bullet points.
    """
