from policyengine_canada.model_api import *


class sk_count_children(Variable):
    value_type = int
    entity = Household
    label = "Children"
    unit = CAD
    documentation = "Number of dependant children under the age of 18"
    definition_period = YEAR