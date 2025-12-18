"""
Skill Extraction Module

Defines a ResumeSkillExtractor class that loads skills and aliases from CSV files,
builds a spaCy NLP pipeline, and extracts normalized, duplicate-free skills
from resume or job description text.
"""

import spacy
import pandas as pd
import re


class ResumeSkillExtractor:

    def _clean_text(self, text):
        text = re.sub(r'([a-zA-Z])([.,;:])', r'\1 \2', text)
        text = re.sub(r'([.,;:])([a-zA-Z])', r'\1 \2', text)
        return text


    def __init__(self, skill_csv_path, alias_csv_path=None):
        self.skill_csv_path = skill_csv_path
        self.alias_map = {}

        self.nlp = spacy.blank("en")
        self.ruler = self.nlp.add_pipe("entity_ruler")

        self._load_patterns()

        if alias_csv_path:
            self._load_aliases(alias_csv_path)

    def _load_patterns(self):
        df = pd.read_csv(self.skill_csv_path)
        patterns = []

        for _, row in df.iterrows():
            skill = row["skill"].lower()
            label = row["type"]

            words = skill.split()
            if len(words) == 1:
                patterns.append({
                    "label": label,
                    "pattern": [{"LOWER": skill}]
                })
            else:
                patterns.append({
                    "label": label,
                    "pattern": [{"LOWER": w} for w in words]
                })

        self.ruler.add_patterns(patterns)


    def _load_aliases(self, alias_csv_path):
        df = pd.read_csv(alias_csv_path)
        self.alias_map = {
            row["alias"].lower(): {
                "canonical": row["canonical"].lower(),
                "type": row["type"]
            }
            for _, row in df.iterrows()
        }


    def extract(self, text):
        text = self._clean_text(text.lower())
        doc = self.nlp(text)

        results = {}

        # 1. Entity-based extraction
        for ent in doc.ents:
            normalized = ent.text
            label = ent.label_

            for alias, info in self.alias_map.items():
                if alias in ent.text:
                    normalized = info["canonical"]
                    label = info["type"]
                    break

            results.setdefault(label, set()).add(normalized)

        # 2. Fallback alias detection (category-aware)
        for alias, info in self.alias_map.items():
            if alias in text:
                results.setdefault(info["type"], set()).add(info["canonical"])

        return results
