from app.usecases.modify_part import similarly_score
from app.drivers.input.move.acquisition_data.accel import accel_right_foot, accel_right_hand, accel_left_foot, accel_left_hand
from app.drivers.input.move.acquisition_data.kinect import kinect_left_foot, kinect_left_hand, kinect_right_foot, kinect_right_hand
from app.drivers.input.music.onset import vocals_onset, drums_onset, melodys_onset

kinect_leftfoot_vocals = similarly_score(kinect_left_foot, vocals_onset)
kinect_leftfoot_drums = similarly_score(kinect_left_foot, drums_onset)
kinect_leftfoot_melodys = similarly_score(kinect_left_foot, melodys_onset)
accel_lefthand_vocals = similarly_score(accel_left_hand, vocals_onset)
accel_lefthand_drums = similarly_score(accel_left_hand, drums_onset)
accel_lefthand_melodys = similarly_score(accel_left_hand, melodys_onset)
kinect_lefthand_vocals = similarly_score(kinect_left_hand, vocals_onset)
kinect_lefthand_drums = similarly_score(kinect_left_hand, drums_onset)
kinect_lefthand_melodys = similarly_score(kinect_left_hand, melodys_onset)
accel_rightfoot_vocals = similarly_score(accel_right_foot, vocals_onset)
accel_rightfoot_drums = similarly_score(accel_right_foot, drums_onset)
accel_rightfoot_melodys = similarly_score(accel_right_foot, melodys_onset)
kinect_rightfoot_vocals = similarly_score(kinect_right_foot, vocals_onset)
kinect_rightfoot_drums = similarly_score(kinect_right_foot, drums_onset)
kinect_rightfoot_melodys = similarly_score(kinect_right_foot, melodys_onset)
accel_righthand_vocals = similarly_score(accel_right_hand, vocals_onset)
accel_righthand_drums = similarly_score(accel_right_hand, drums_onset)
accel_righthand_melodys = similarly_score(accel_right_hand, melodys_onset)
kinect_righthand_vocals = similarly_score(kinect_right_hand, vocals_onset)
kinect_righthand_drums = similarly_score(kinect_right_hand, drums_onset)
kinect_righthand_melodys = similarly_score(kinect_right_hand, melodys_onset)
accel_leftfoot_vocals = similarly_score(accel_left_foot, vocals_onset)
accel_leftfoot_drums = similarly_score(accel_left_foot, drums_onset)
accel_leftfoot_melodys = similarly_score(accel_left_foot, melodys_onset)