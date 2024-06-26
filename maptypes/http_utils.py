import sys
import os

import json
import requests

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from concept_meta import ConceptMapping
from common import settings


concept_api_url = settings.base_url + "/orgs/MOH-KENYA/sources/PPB_P/concepts/"
concept_mapping_api_url = settings.base_url + "/orgs/MOH-KENYA/sources/PPB_P/mappings/"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json',
           'Authorization': 'Bearer %s' % settings.token }


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
        # POST concept mapping to api
        concept_mapping = ConceptMapping(parent_id=parent_id, child_id=cid, from_concept_url=c_concept_url,
                                         to_concept_url=parent_concept_url, from_concept_name=concept_name,
                                         to_concept_name=parent_concept_name)
        mdata = json.dumps(concept_mapping, default=vars)
        mresponse = requests.post(concept_mapping_api_url, data=mdata, headers=headers)
        print("{} - {}".format(mresponse.status_code, mresponse.json()))

    return {"id": cid, "name": concept_name, "url": c_concept_url}