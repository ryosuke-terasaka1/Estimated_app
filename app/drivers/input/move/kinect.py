kinect_file_name = "toshi_kinect02.csv"
ELBOW_RIGHT_degree, KNEE_RIGHT_degree, ELBOW_LEFT_degree, KNEE_LEFT_degree = degree(kinect_file_name)

kinect_right_hand = kinect_timing_move(ELBOW_RIGHT_degree, 60, "large")
kinect_right_foot =  kinect_timing_move(KNEE_RIGHT_degree, 60, "large")
kinect_left_hand = kinect_timing_move(ELBOW_LEFT_degree, 60, "large")
kinect_left_foot =  kinect_timing_move(KNEE_LEFT_degree, 60, "large")