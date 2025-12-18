"""
Skill Matching Module

Compares resume skills with job description skills and computes
a weighted match score with explainable results.
"""

import pandas as pd


def load_weights(weight_csv_path):
    df = pd.read_csv(weight_csv_path)
    return {
        row["skill"].lower(): row["weight"]
        for _, row in df.iterrows()
    }


def weighted_match(resume_skills, job_skills, weights):
    matched = {}
    missing = {}

    matched_score = 0
    total_score = 0

    for category, required_skills in job_skills.items():
        resume_set = resume_skills.get(category, set())

        matched[category] = resume_set & required_skills
        missing[category] = required_skills - resume_set

        for skill in required_skills:
            weight = weights.get(skill, 1)
            total_score += weight
            if skill in resume_set:
                matched_score += weight

    score = round((matched_score / total_score) * 100, 2) if total_score else 0.0
    return matched, missing, score
