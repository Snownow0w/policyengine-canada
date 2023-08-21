from policyengine_canada.model_api import *


class sk_spouse_or_common_law_partner_credit(Variable):
    value_type = float
    entity = Household
    label = "Saskatchewan spouse or common law partner credit"
    definition_period = YEAR
    defined_for = "sk_spouse_or_common_law_partner_credit_eligible"

    def formula(household, period, parameters):
        p = parameters(
            period
        ).gov.provinces.sk.tax.income.credits.spouse_or_common_law_partner_amount
        person = household.members
        spouse_income = household.sum(person("spouse_income", period))
        reduction_threshold = spouse_income <= p.reduction.income_threshold
        reduced_amount = max_(p.reduction.base_amount - spouse_income, 0)
        amount = where(
            reduction_threshold,
            reduced_amount,
            p.max_amount,
        )

        return amount
