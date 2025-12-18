"""
Advanced Resume Analyzer

Extracts normalized skills from a resume and a job description,
then computes a weighted ATS-style match score with explanations.
"""

import os
from skill_e import ResumeSkillExtractor
from matcher import load_weights, weighted_match
from section_parser import split_into_sections



def get_multiline_input(prompt):
    print(prompt)
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    return "\n".join(lines)


def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    skills_path = os.path.join(base_dir, "data", "skills.csv")
    alias_path = os.path.join(base_dir, "data", "skill_aliases.csv")
    weight_path = os.path.join(base_dir, "data", "skill_weights.csv")

    extractor = ResumeSkillExtractor(skills_path, alias_path)
    weights = load_weights(weight_path)

    resume_text = get_multiline_input(
        "\nPaste RESUME text (press ENTER twice to finish):"
    )

    job_text = get_multiline_input(
        "\nPaste JOB DESCRIPTION text (press ENTER twice to finish):"
    )

    sections = split_into_sections(resume_text)

    resume_skills = {}
    skill_evidence = {}

    for section, section_text in sections.items():
        extracted = extractor.extract(section_text)

        for category, skills in extracted.items():
            for skill in skills:
                resume_skills.setdefault(category, set()).add(skill)
                skill_evidence.setdefault(skill, set()).add(section)

    job_skills = extractor.extract(job_text)

    matched, missing, score = weighted_match(resume_skills, job_skills, weights)

    print("\n📌 MATCHED SKILLS")
    for k, v in matched.items():
        if v:
            print(f"{k}: {', '.join(sorted(v))}")

    print("\n⚠️ MISSING SKILLS")
    for k, v in missing.items():
        if v:
            print(f"{k}: {', '.join(sorted(v))}")

    print(f"\n📊 WEIGHTED MATCH SCORE: {score}%")
    print("\n📍 SKILL EVIDENCE BY SECTION")
    for skill, sections in skill_evidence.items():
        print(f"{skill}: {', '.join(sorted(sections))}")



if __name__ == "__main__":
    main()
