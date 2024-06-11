import json

from concept_meta import ConceptName, ConceptDescription


class Concept:
    def __init__(self, display_name):
        self.concept_class = "None"
        self.datatype = "N/A"
        self.retired: False
        self.owner_type = "Organization"
        self.owner_url = "/orgs/MOH-KENYA/"
        self.display_name = display_name
        self.display_locale = "en"
        self.names = [ConceptName(self.display_name)]
        self.descriptions = [ConceptDescription(self.display_name)]
        self.type = "Concept"
        self.children = []
        #
        # ConceptName(name=brand_proprietary_name, type="Brand/proprietary")

    def add_child(self, child):
        self.children.append(child)

    def has_children(self):
        return len(self.children) > 0

    def get_child(self, name):
        return next(child for child in self.children if child.display_name == name)

    def print_tree(self, idx, delimiter):
        print(json.dumps(self, indent=2, default=vars))
