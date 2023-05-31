from policyengine_canada.model_api import *


class sk_seniors_income_plan_at_home(Variable):
    value_type = float
    entity = Household
    label = "Saskatchewan seniors income plan client category - living at home"
    definition_period = YEAR
    defined_for = ProvinceCode.SK

    def formula(household, period, parameters):
        p = parameters(period).gov.provinces.sk.benefits.sip
        cpp = household("canada_pension_plan_payout", period)
        person = household.members
        age = person("age", period)
        eligible = ~(person("special_care_home", period))
        pensioner = person("is_pensioner", period)
        married = household("is_married", period)
        count_pensioners = household.sum(pensioner)
        spouse_ineligible = person("is_spouse", period) & (age < p.age.spouse_threshold)
        received_allowance = person("receive_allowance")
        return eligible * (select(
            # Conditions.
            [(~married) & (pensioner == true), (married) & (count_pensioners == 2), (married) & spouse_ineligible, (married) & (received_allowance > 0)],
            # Results.
            [
                p.living_at_home.max_amount.single, #need to add reduction & CPP eligibility,
                p.living_at_home.max_amount.married_both_pensioners,
                p.living_at_home.max_amount.married_spouse_below_age_threshold,
                p.living_at_home.max_amount.married_spouse_receiving_allowance,
            ],
            default=0,
        ))


#TODO: add cpp payout elgibility in a separate select
# make test for variable
# do same for the special care home
# find out what the reduction is and add to formula