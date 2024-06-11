class ConceptName(object):
    def __init__(self, name, ctype):
        self.name = name
        self.type = ctype
        self.locale = "en"


class ConceptDescription:
    def __init__(self, description):
        self.description = description
        self.locale = "en"


class ConceptMapping:
    def __init__(self, parent_id, child_id, from_concept_url, to_concept_url,
                 from_concept_name, to_concept_name,
                 from_source_url, to_source_url, map_type):
        self.from_concept_code = child_id
        self.to_concept_code = parent_id

        self.from_concept_url = from_concept_url
        self.to_concept_url = to_concept_url

        self.from_concept_name = from_concept_name
        self.to_concept_name = to_concept_name

        self.from_source_url = from_source_url
        self.to_source_url = to_source_url
        self.map_type = map_type
        self.retired = False
