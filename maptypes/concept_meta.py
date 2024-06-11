class ConceptName(object):
    def __init__(self, name):
        self.name = name
        self.locale = "en"
        self.locale_preferred = True
        self.name_type = "Fully Specified"


class ConceptDescription:
    def __init__(self, description):
        self.description = description
        self.locale = "en"
        self.locale_preferred = True


class ConceptMapping:
    def __init__(self, parent_id, child_id, from_concept_url, to_concept_url, from_concept_name, to_concept_name):
        self.from_concept_code = child_id
        self.to_concept_code = parent_id

        self.from_concept_url = from_concept_url
        self.to_concept_url = to_concept_url

        self.from_concept_name = from_concept_name
        self.to_concept_name = to_concept_name

        self.from_source_url = "/orgs/MOH-KENYA/sources/PPB_P/"
        self.to_source_url = "/orgs/MOH-KENYA/sources/PPB_P/"
        self.map_type = "CONCEPT-SET"
        self.retired = False
