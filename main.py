import openpyxl

from concept import Concept
from http_utils import post_concept

if __name__ == '__main__':
    wb = openpyxl.load_workbook("files/excel/hpt_non_pharm_group_22nd_may_5pm.xlsx")
    sheet = wb["Sheet 1 - md_register"]

    for row in range(2, sheet.max_row + 1):
        atc_code = sheet.cell(row=row, column=1).value
        generic_name = sheet.cell(row=row, column=2).value
        strength = sheet.cell(row=row, column=3).value
        product_form = sheet.cell(row=row, column=4).value
        product_name_and_brand = sheet.cell(row=row, column=5).value
        concept_class = sheet.cell(row=row, column=6).value
        data_type = sheet.cell(row=row, column=7).value
        route_of_administration = sheet.cell(row=row, column=8).value
        full_name = "{} {} {}".format(product_name_and_brand, strength, product_form)

        if full_name is not None:
            drug = Concept(full_name)
            drug.concept_class = concept_class
            drug.datatype = data_type
            drug.extras = {"level": "2", "atc_code": atc_code,
                           "generic_name": generic_name, "route_of_administration": route_of_administration}

            generic_name_tokens = generic_name.split('/')
            strength_tokens = strength.split('/')
            if len(generic_name_tokens) > 0 and len(generic_name_tokens) == len(strength_tokens):
                active_ingredients = []
                for idx, item in enumerate(generic_name_tokens):
                    active_ingredients.append({"name": generic_name_tokens[idx].strip(),
                                               "strength": strength_tokens[idx].strip()
                                               })
                drug.extras["active_ingredients"] = active_ingredients

            drug.print_tree(0, "")
            #post_concept(concept=drug, parent_id=72182, parent_concept_name="Pharmaceutical Products",
                        # parent_concept_url="/orgs/MOH-KENYA/sources/PPB/concepts/72182/")

    # for concept in generic_names_list:
    # post_concept(concept, "", "", "")
    #
