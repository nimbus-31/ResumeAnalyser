"""
Resume Section Parser

Splits resume text into sections based on common resume headers
and returns a mapping of section name to text content.
"""

import re


SECTION_HEADERS = {
    "SKILLS": ["skills", "technical skills"],
    "EXPERIENCE": ["experience", "work experience", "professional experience"],
    "PROJECTS": ["projects", "academic projects"],
    "EDUCATION": ["education", "academic background"]
}
def normalize_headers(text):
    for section, keywords in SECTION_HEADERS.items():
        for keyword in keywords:
            text = text.replace(keyword, f"\n{keyword}\n")
    return text


def split_into_sections(text):
    text = normalize_headers(text.lower())
    lines = text.splitlines()

    sections = {}
    current_section = "OTHER"
    sections[current_section] = []

    for line in lines:
        stripped = line.strip()

        if not stripped:
            continue

        found_header = False
        for section, keywords in SECTION_HEADERS.items():
            if stripped in keywords:
                current_section = section
                sections.setdefault(current_section, [])
                found_header = True
                break

        if not found_header:
            sections[current_section].append(stripped)

    return {
        section: " ".join(content)
        for section, content in sections.items()
        if content
    }
