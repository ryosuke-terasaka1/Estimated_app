from app.usecases.rule_base import rule_base

rulebase_accel_leftfoot = rule_base(accel_leftfoot_melodys,accel_leftfoot_drums, accel_leftfoot_vocals)
rulebase_accel_rightfoot = rule_base(accel_rightfoot_melodys,accel_rightfoot_drums, accel_rightfoot_vocals)
rulebase_accel_lefthand = rule_base(accel_lefthand_melodys,accel_lefthand_drums, accel_lefthand_vocals)
rulebase_accel_righthand = rule_base(accel_righthand_melodys,accel_righthand_drums, accel_righthand_vocals)
rulebase_kinect_leftfoot = rule_base(kinect_leftfoot_melodys,kinect_leftfoot_drums, kinect_leftfoot_vocals)
rulebase_kinect_rightfoot = rule_base(kinect_rightfoot_melodys,kinect_rightfoot_drums, kinect_rightfoot_vocals)
rulebase_kinect_lefthand = rule_base(kinect_lefthand_melodys,kinect_lefthand_drums, kinect_lefthand_vocals)
rulebase_kinect_righthand = rule_base(kinect_righthand_melodys,kinect_righthand_drums, kinect_righthand_vocals)


body_part = body_concious_part(rulebase_accel_leftfoot,
                               rulebase_accel_rightfoot,
                               rulebase_accel_lefthand,
                               rulebase_accel_righthand,
                               rulebase_kinect_leftfoot,
                               rulebase_kinect_rightfoot,
                               rulebase_kinect_lefthand,
                               rulebase_kinect_righthand)


rule_base_concious_part = make_concious_part(7, "two")
# del_body_part = delete_break_list(body_part)
sum_body_part = sum_four_counts(del_body_part)
value_rulebase_body_part = part_to_value(sum_body_part,rule_base_concious_part)
# print(sum_body_part)
# print(value_rulebase_body_part)
# del_value_body_part = part_to_value(del_body_part,rule_base_concious_part)
# del_concious_part = delete_break_list(enl_concious_part)
enl_value_rulebase_body_part = enlarge_sentence(value_rulebase_body_part,100)
enl_value_rulebase_concious_part = enlarge_sentence(value_rulebase_body_part,100)



toshi_rule_base =  toshi_rulebase_func(ideal_vocals, ideal_melodys, ideal_drums)
int_toshi_rule_base = to_int(toshi_rule_base)