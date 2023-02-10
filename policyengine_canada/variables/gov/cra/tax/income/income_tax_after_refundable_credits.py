from policyengine_canada.model_api import *


class income_tax(Variable):
    value_type = float
    entity = Household
    label = "Income tax after non-refundable tax credits"
    unit = CAD
    documentation = "Example income tax regime"
    definition_period = YEAR

    adds = ["income_tax_before_refundable_credits"]
    subtracts = ["refundable_tax_credits"]
