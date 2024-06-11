import json

from concept_meta import ConceptName, ConceptDescription


def set_concept_names(brand_proprietary_name, inn):
    concept_names = []
    if brand_proprietary_name:
        concept_name = ConceptName(
            name=brand_proprietary_name, ctype="Brand/proprietary")
        concept_name.locale_preferred = True
        concept_names.append(concept_name)
    if inn:
        concept_name = ConceptName(name=inn, ctype="INN")
        concept_names.append(concept_name)

    return concept_names


def set_concept_descriptions(product_visual_descriptions, brand_proprietary_name):
    concept_descriptions = []
    if product_visual_descriptions:
        concept_description = ConceptDescription(product_visual_descriptions)
        concept_descriptions.append(concept_description)
    else:
        concept_description = ConceptDescription(brand_proprietary_name)
        concept_descriptions.append(concept_description)
    return concept_descriptions


class Concept:
    def __init__(self, brand_proprietary_name, inn, product_visual_descriptions):
        self.concept_class = "Drug"
        self.datatype = "N/A"
        self.retired: False
        self.owner_type = "Organization"
        self.owner_url = "/orgs/MOH-KENYA/"
        self.display_locale = "en"
        self.names = set_concept_names(brand_proprietary_name, inn)
        self.descriptions = set_concept_descriptions(
            product_visual_descriptions, brand_proprietary_name)
        self.type = "Concept"
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def has_children(self):
        return len(self.children) > 0

    def get_child(self, name):
        return next(child for child in self.children if child.display_name == name)

    def print_tree(self, idx, delimiter):
        print(json.dumps(self, indent=2, default=vars))
