from app.domains.entities.ideal import IdealData
from app.usecases.rule_base import toshi_rulebase_func

def ideal_Rule_base(dancer: IdealData):
    dancer.Rule_base_Concious_Part = toshi_rulebase_func(dancer.Similarly_vocal, dancer.Similarly_melody, dancer.Similarly_drum)
    return dancer

def ideal_tf_idf(dancer: IdealData):
    dancer.Tf_idf_Concious_Part = toshi_rulebase_func(dancer.Similarly_vocal, dancer.Similarly_melody, dancer.Similarly_drum)
    return dancer

def Ideal_plot(dancer: IdealData):
    dancer = ideal_Rule_base(dancer)
    dancer = ideal_tf_idf(dancer)



    to_figure(enl_int_toshi_rule_base,
              enl_int_toshi_tf_idf,
              enl_int_toshi_accuracy_data)