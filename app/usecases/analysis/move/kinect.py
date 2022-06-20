names_list=["PELVIS","SPINE_NAVAL","SPINE_CHEST","NECK","CLAVICLE_LEFT","SHOULDER_LEFT","ELBOW_LEFT","WRIST_LEFT",
"HAND_LEFT","HANDTIP_LEFT","THUMB_LEFT","CLAVICLE_RIGHT","SHOULDER_RIGHT","ELBOW_RIGHT","WRIST_RIGHT","HAND_RIGHT",
"HANDTIP_RIGHT","THUMB_RIGHT","HIP_LEFT","KNEE_LEFT","ANKLE_LEFT","FOOT_LEFT","HIP_RIGHT","KNEE_RIGHT",
"ANKLE_RIGHT","FOOT_RIGHT","HEAD","NOSE","EYE_LEFT","EAR_LEFT","EYE_RIGHT","EAR_RIGHT"]

kinect_names = ["Time"]
for name in names_list:
    kinect_names.append(name + "_X")
    kinect_names.append(name + "_Y")
    kinect_names.append(name + "_Z")
kinect_names.append("")


def numpy_data(df: pd.DataFrame, body_part: str):
    numX=df[body_part + '_X'].to_numpy()
    numY=df[body_part + '_Y'].to_numpy()
    numZ=df[body_part + '_Z'].to_numpy()

    numX = np.ndarray.flatten(numX)
    numY = np.ndarray.flatten(numY)
    numZ = np.ndarray.flatten(numZ)

    num = np.stack([numX, numY, numZ], 1)
#     print(num)
#     num = np.ndarray.flatten(num)
#     print(num)
    return num


def find_cos(start, point, end):
    cos_list = []
    for i in range(len(start)):
        vec_a = start[i] - point[i]
        vec_c = end[i] - point[i]

        # コサインの計算
        length_vec_a = np.linalg.norm(vec_a)
        length_vec_c = np.linalg.norm(vec_c)
        inner_product = np.inner(vec_a, vec_c)
        cos = inner_product / (length_vec_a * length_vec_c)

        # 角度（ラジアン）の計算
        rad = np.arccos(cos)

        # 弧度法から度数法（rad ➔ 度）への変換
        degree = np.rad2deg(rad)
        
        cos_list.append(degree)
#     print(cos_list)
    return cos_list


def degree(file_name):
  # 点A,B,Cの座標（3次元座標上の場合）
  #a = np.array([0,1,2]) #この3行の座標はテスト用
  #b = np.array([10,20,30])
  #c = np.array([5,7,9])
    df = pd.read_csv(file_name, header=None, names = kinect_names)
    WRIST_RIGHT_data = numpy_data(df, "WRIST_RIGHT")
    SHOULDER_RIGHT_data = numpy_data(df, "SHOULDER_RIGHT")
    ELBOW_RIGHT_data = numpy_data(df, "ELBOW_RIGHT")
    ANKLE_RIGHT_data = numpy_data(df, "ANKLE_RIGHT")
    HIP_RIGHT_data = numpy_data(df, "HIP_RIGHT")
    KNEE_RIGHT_data = numpy_data(df, "KNEE_RIGHT")
    WRIST_LEFT_data = numpy_data(df, "WRIST_LEFT")
    SHOULDER_LEFT_data = numpy_data(df, "SHOULDER_LEFT")
    ELBOW_LEFT_data = numpy_data(df, "ELBOW_LEFT")
    ANKLE_LEFT_data = numpy_data(df, "ANKLE_LEFT")
    HIP_LEFT_data = numpy_data(df, "HIP_LEFT")
    KNEE_LEFT_data = numpy_data(df, "KNEE_LEFT")
    
#     print(WRIST_RIGHT_data,SHOULDER_RIGHT_data)
#     print(WRIST_RIGHT_data - SHOULDER_RIGHT_data)
 
    ELBOW_RIGHT_degree = find_cos(WRIST_RIGHT_data, ELBOW_RIGHT_data, SHOULDER_RIGHT_data)
    KNEE_RIGHT_degree = find_cos(ANKLE_RIGHT_data, KNEE_RIGHT_data, HIP_RIGHT_data)
    ELBOW_LEFT_degree = find_cos(WRIST_LEFT_data, ELBOW_LEFT_data, SHOULDER_LEFT_data)
    KNEE_LEFT_degree = find_cos(ANKLE_LEFT_data, KNEE_LEFT_data, HIP_LEFT_data)
  
    return ELBOW_RIGHT_degree, KNEE_RIGHT_degree, ELBOW_LEFT_degree, KNEE_LEFT_degree


def file_cut(df: pd.DataFrame) -> pd.DataFrame:
#     df = pd.read_csv(file_name,header = None)
#     df.columns = ["Degree"]
#     df["time"] *= 0.2
    count = 0
    for i in range(len(df)):
        if i > 400 and df[i] >= 30:
            start_timing = i
            break
#     print(i)
    df = df[start_timing+1:]
    return df

# def decide_threshold_level()

def kinect_timing_move(accel_data, threshold_level, small_or_large):
#     accel_data = file_cut(df)
#     accel_data["time"] *= 0.02
    accel_data = accel_data[kinect_start_timing:]   # 開始タイミング
#     print(accel_data)
    if small_or_large == "small":
        data_kind = 90 - accel_data
    elif small_or_large == "large":
        data_kind = accel_data
    peaks, _ = find_peaks(data_kind, height=threshold_level)
#     plt.plot(accel_data)
#     plt.plot(int(peaks), accel_data[peaks], "x")
#     plt.plot(np.zeros_like(accel_data), "--", color="gray")
#     plt.show()
#     print(float(peaks[0]/20))
#     feature_datalist = []
#     for i in range(len(accel_data)):
# #         print(i)
#         if peaks.size != 0:
#             if i == peaks[0]:
#                 count += 1
#                 feature_datalist.insert(i,1)
#                 peaks = peaks[1:len(peaks)]
#             else:
#                 feature_datalist.insert(i,0)
                
#     for j in range(len(accel_data)):
#         for i in range(len(count_list)):
#             if peaks.size != 0:
#     #             print(count_list[i])
#                 if j == peaks[0]:
#                     peak_time = float(j/20)
#                     print(peak_time)
#                     if count_list[i] <= peak_time < count_list[i+1]:
#         #                 print(peaks[0])
#                         feature_datalist.insert(i,1)
#                     else:
#                         feature_datalist.insert(i,0)
#         peaks = peaks[1:len(peaks)]
#     print(feature_datalist)
    count = 0
    half_timing = []
    quarter_timing = []
    for _ in range(music_half_count_length):
        half_timing.append(0)
    for _ in range(music_quarter_count_length):
        quarter_timing.append(0)

#     timing 
    peak_time = []
    for i in peaks:
        time = float(i/30)
        peak_time.append(time)   
    for i in peak_time:
        for j in range(1, len(half_count_list)-1):
            if half_count_list[j] <= i < half_count_list[j+1]:
#                 if timing[j] == 1:
#                     continue
#                 else:
                half_timing[j] = 1
#             else:
#                 timing.insert(j, 0)
#     print(timing)
    return half_timing