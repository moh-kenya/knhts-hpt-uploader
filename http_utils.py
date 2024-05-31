import json

import requests

from concept_meta import ConceptMapping

concept_api_url = "https://knhts-staging.health.go.ke/knhts-api/orgs/MOH-KENYA/sources/PPB_P/concepts/"
concept_mapping_api_url = "https://knhts-staging.health.go.ke/knhts-api/orgs/MOH-KENYA/sources/PPB_P/mappings/"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json',
           'Authorization': 'Bearer 891b4b17feab99f3ff7e5b5d04ccc5da7aa96da6'}


def process_concept_mapping(parent_id, child_id, from_concept_url, to_concept_url, from_concept_name, to_concept_name,
                            from_source_url, to_source_url, map_type):
    # POST concept mapping to api
    concept_mapping = ConceptMapping(parent_id=parent_id, child_id=child_id, from_concept_url=from_concept_url,
                                     to_concept_url=to_concept_url, from_concept_name=from_concept_name,
                                     to_concept_name=to_concept_name, from_source_url=from_source_url,
                                     to_source_url=to_source_url, map_type=map_type)
    mdata = json.dumps(concept_mapping, default=vars)
    mresponse = requests.post(concept_mapping_api_url, data=mdata, headers=headers)
    print(" Mapping response -->> {} - {}".format(mresponse.status_code, mresponse.json()))


def process_concept_mapping_metadata(concepts, meta_value, child_id, from_concept_url, from_concept_name, map_type):
    for concept in concepts:
        if "id" in concept and "display_name" in concept and concept['display_name'] == meta_value:
            process_concept_mapping(parent_id=concept['id'], child_id=child_id, from_concept_url=from_concept_url,
                                    to_concept_url=concept['url'], from_concept_name=from_concept_name,
                                    to_concept_name=concept['display_name'],
                                    from_source_url="/orgs/MOH-KENYA/sources/PPB_P/",
                                    to_source_url="/orgs/MOH-KENYA/sources/PPB_P/", map_type=map_type)


def post_concept(concept, parent_id, parent_concept_name, parent_concept_url):
    # POST concept to api
    data = json.dumps(concept, default=vars)
    response = requests.post(concept_api_url, data=data, headers=headers)
    json_response = response.json()
    print("{} - {}".format(response.status_code, json_response))
    cid = json_response['id']
    concept_name = json_response['display_name']
    c_concept_url = json_response['url']

    if parent_id:
        process_concept_mapping(parent_id=parent_id, child_id=cid, from_concept_url=c_concept_url,
                                to_concept_url=parent_concept_url, from_concept_name=concept_name,
                                to_concept_name=parent_concept_name,
                                from_source_url="/orgs/MOH-KENYA/sources/PPB_P/",
                                to_source_url="/orgs/MOH-KENYA/sources/PPB_P/", map_type="CONCEPT-SET")

    if hasattr(concept, 'storage_conditions') and concept.storage_conditions:
        concepts_sc = get_concept(concept.storage_conditions)
        process_concept_mapping_metadata(concepts_sc, concept.storage_conditions, cid, c_concept_url, concept_name,
                                         "storage-condition")

    if hasattr(concept, 'dosage_form') and concept.dosage_form:
        concepts_df = get_concept(concept.dosage_form)
        process_concept_mapping_metadata(concepts_df, concept.dosage_form, cid, c_concept_url, concept_name,
                                         "Has-dose-form")

    if hasattr(concept, 'route_of_administration') and concept.route_of_administration:
        concepts_roa = get_concept(concept.route_of_administration)
        process_concept_mapping_metadata(concepts_roa, concept.route_of_administration, cid, c_concept_url,
                                         concept_name, "Route-of-administration")

    if hasattr(concept, 'shelf_life') and concept.shelf_life:
        concepts_sl = get_concept(concept.shelf_life)
        process_concept_mapping_metadata(concepts_sl, concept.shelf_life, cid, c_concept_url, concept_name,
                                         "has-shelf-life")

    return {"id": cid, "name": concept_name, "url": c_concept_url}


def get_concept(concept_name):
    params = {'q': concept_name}
    response = requests.get(concept_api_url, headers=headers, params=params)
    json_response = response.json()
    return json_response
