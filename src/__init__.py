def __init__(self, skill_csv_path, alias_csv_path=None):
    self.skill_csv_path = skill_csv_path
    self.alias_map = {}
    self.nlp = spacy.blank("en")
    self.ruler = self.nlp.add_pipe("entity_ruler")
    self._load_patterns()

    if alias_csv_path:
        self._load_aliases(alias_csv_path)
