def accel_composite(file_path):
    df = pd.read_csv(file_path, header = None, usecols=[3, 4, 5])
    df.columns = ["x", "y", "z"]
#     print(df)
    composite = []
    for i in range(len(df)):
        x_value = float(df["x"][i] ** 2)
        y_value = float(df["y"][i] ** 2)
        z_value = float(df["z"][i] ** 2)
        composite_value = math.sqrt(x_value + y_value + z_value)
        composite.append(composite_value)
    return composite[accel_start_timing:]  # 開始タイミング



def accel_timing_move(file_path, threshold_level, small_or_large):
    composite = accel_composite(file_path)
#     accel_data["time"] *= 0.02
    accel_data = np.array(composite)
    accel_data = np.ndarray.flatten(accel_data)
    if small_or_large == "small":
        data_kind = 90 - accel_data
    elif small_or_large == "large":
        data_kind = accel_data
    peaks, _ = find_peaks(data_kind, height=threshold_level)
#     plt.plot(accel_data)
#     plt.plot(peaks, accel_data[peaks], "x")
#     plt.plot(np.zeros_like(accel_data), "--", color="gray")
#     plt.show()
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
        time = float(i/50)
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