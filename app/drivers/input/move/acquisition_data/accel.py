from app.domains.entities.dancer import DancerAccel
from app.usecases.analysis.move.accel import accel_timing_move

def create_dancer_data(name: str, file_name):
    dancer_accel = DancerAccel()
    dancer_accel.name = name
    dancer_accel.right_hand = accel_timing_move("toshi_righthand02.csv", 2000, "large")
    dancer_accel.right_foot = accel_timing_move("toshi_rightfoot02.csv", 2000, "large")
    dancer_accel.left_hand = accel_timing_move("toshi_lefthand02.csv", 2000, "large")
    dancer_accel.left_foot = accel_timing_move("toshi_leftfoot02.csv", 2000, "large")
    return dancer_accel