import csv

import openpyxl

from concept import Concept
from http_utils import post_concept


def process_pharmaceutical_dosage_forms():
    #has-dose_form
    dosage_form = Concept("Dosage Forms")
    dosage_form.concept_class = "ConvSet"
    dosage_form.datatype = "N/A"
    df_dict = post_concept(concept=dosage_form, parent_id=None, parent_concept_name=None, parent_concept_url=None)
    #print(df_dict)
    dosage_forms = []
    with open('..files/csv/param_pharmaceutical_dosage_form.csv', mode='r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        row_count = 0
        for line in csv_reader:
            if row_count != 0:
                dosage_form_line = line[1]
                if dosage_form_line not in dosage_forms:
                    dosage_forms.append(dosage_form_line)
            row_count += 1

    for dosage_form_df in dosage_forms:
        dosage_form_concept = Concept(dosage_form_df)
        dosage_form_concept.concept_class = "Misc"
        dosage_form_concept.datatype = "N/A"
        post_concept(concept=dosage_form_concept, parent_id=df_dict['id'], parent_concept_name=df_dict['name'],
                             parent_concept_url=df_dict['url'])


def process_routes_of_administration():
    route_of_administration = Concept("Routes Of Administration")
    route_of_administration.concept_class = "ConvSet"
    route_of_administration.datatype = "N/A"
    roa_dict = post_concept(concept=route_of_administration, parent_id=None, parent_concept_name=None, parent_concept_url=None)

    routes_of_administration = []
    with open('../files/csv/param_routes_of_admin.csv', mode='r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for line in csv_reader:
            route_of_administration_line = line[1].title()
            if route_of_administration_line not in routes_of_administration:
                routes_of_administration.append(route_of_administration_line)

    for route_of_administration_roa in routes_of_administration:
        route_of_administration_concept = Concept(route_of_administration_roa)
        route_of_administration_concept.concept_class = "Misc"
        route_of_administration_concept.datatype = "N/A"
        post_concept(concept=route_of_administration_concept, parent_id=roa_dict['id'], parent_concept_name=roa_dict['name'],
                     parent_concept_url=roa_dict['url'])


def create_shelf_life_map_type():
    has_shelf_life_map_type = Concept("Has shelf life")
    has_shelf_life_map_type.id = "Has-shelf-life"
    has_shelf_life_map_type.external_id = "3cfa89ca-49a1-42b6-89ed-08afb7c959f9"
    has_shelf_life_map_type.concept_class = "MapType"
    has_shelf_life_map_type.datatype = "N/A"
    post_concept(concept=has_shelf_life_map_type, parent_id=None, parent_concept_name=None, parent_concept_url=None)


def process_shelf_lives():
    create_shelf_life_map_type()
    shelf_life = Concept("Shelf Lives")
    shelf_life.concept_class = "ConvSet"
    shelf_life.datatype = "N/A"
    sl_dict = post_concept(concept=shelf_life, parent_id=None, parent_concept_name=None,
                            parent_concept_url=None)

    shelf_lives = []
    with open('../files/csv/param_shelf_life.csv', mode='r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for line in csv_reader:
            shelf_life_line = line[1]
            if shelf_life_line not in shelf_lives:
                shelf_lives.append(shelf_life_line)

    for shelf_life_sl in shelf_lives:
        shelf_life_concept = Concept(shelf_life_sl)
        shelf_life_concept.concept_class = "Misc"
        shelf_life_concept.datatype = "N/A"
        post_concept(concept=shelf_life_concept, parent_id=sl_dict['id'],
                     parent_concept_name=sl_dict['name'],
                     parent_concept_url=sl_dict['url'])


def create_storage_condition_map_type():
    storage_condition_map_type = Concept("Storage Condition")
    storage_condition_map_type.id = "Storage-condition"
    storage_condition_map_type.external_id = "f0d1f2a0-568a-43de-9a60-feac8479f35b"
    storage_condition_map_type.concept_class = "MapType"
    storage_condition_map_type.datatype = "N/A"
    post_concept(concept=storage_condition_map_type, parent_id=None, parent_concept_name=None, parent_concept_url=None)


def process_storage_conditions():
    create_storage_condition_map_type()
    storage_condition = Concept("Storage Conditions")
    storage_condition.concept_class = "ConvSet"
    storage_condition.datatype = "N/A"
    sc_dict = post_concept(concept=storage_condition, parent_id=None, parent_concept_name=None,
                           parent_concept_url=None)

    storage_conditions = []
    with open('../files/csv/param_storage_conditions.csv', mode='r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for line in csv_reader:
            print(line)
            storage_condition_line = line[1]
            if storage_condition_line not in storage_conditions:
                storage_conditions.append(storage_condition_line)

    for storage_condition_sc in storage_conditions:
        storage_condition_concept = Concept(storage_condition_sc)
        storage_condition_concept.concept_class = "Misc"
        storage_condition_concept.datatype = "N/A"
        post_concept(concept=storage_condition_concept, parent_id=sc_dict['id'],
                     parent_concept_name=sc_dict['name'],
                     parent_concept_url=sc_dict['url'])


if __name__ == '__main__':
    process_pharmaceutical_dosage_forms()
    process_routes_of_administration()
    process_shelf_lives()
    process_storage_conditions()
