# -*- coding: utf-8 -*-
"""
speech recognitionの上限
再生時間が5分以内
変換後のテキスト（スペース含む）の文字数が1387（最大で確認できた）以内
"""

import pyaudio
import numpy as np
import wave

import ffmpeg
import speech_recognition as sr
import subprocess

NAME = '10min'

MOVIE_PATH = f'MovieFile/{NAME}.mp4'
WAV_PATH_STEREO = f'WaveFile/{NAME}_STEREO.wav'
WAV_PATH_MONO = f'WaveFile/{NAME}_MONO.wav'
WAV_PARTS_PATH = f'WavePartsFile/_{NAME}_0'
TEXT_PATH_1 = f'TextFile/{NAME}_3.txt'

DURATION = 5 #5分間

#mp4から音声を抽出してwavファイルへ変換．
#subprocess経由でffmpegを呼び出すと，wavへのコーデックに失敗するため，ffmpeg-pythonを使用
def MP4_to_WAV(movie_path, wav_path):
    stream = ffmpeg.input(movie_path)
    stream = ffmpeg.output(stream, wav_path, format='wav')
    ffmpeg.run(stream)

def Codec_to_Mono(wav_path_in, wav_path_out):
    command = f'ffmpeg -i {wav_path_in} -ac 1 {wav_path_out}'
    subprocess.call(command, shell=True)

#wavを分割
def Wav_Divide(wav_path_in, start_time, finish_time, wav_path_out):
    command = f'ffmpeg -i {wav_path_in} -ss {start_time} -to {finish_time} -acodec copy {wav_path_out}'
    subprocess.call(command, shell=True)

#文字起こし
def Speech_to_Text_sr(wav_path):
    r = sr.Recognizer()

    with sr.AudioFile(wav_path) as source:
        audio = r.record(source)
        text = r.recognize_google(audio, language='ja-JP')
    
    return text

#テキストファイルに書き込み
def Write_Text(text_path, text, mode):
    with open(text_path, mode) as f:
            f.write(text)
         
            
if __name__ == '__main__':
    result_text = []
    num_chara = []
    MP4_to_WAV(MOVIE_PATH, WAV_PATH_STEREO)
    #Codec_to_Mono(WAV_PATH_STEREO, WAV_PATH_MONO)
    for i in range(20):
        start_time = i*30
        wav_parts_path = f'{WAV_PARTS_PATH}{i}.wav'
        Wav_Divide(WAV_PATH_STEREO, start_time, start_time + 30, wav_parts_path)
        result = Speech_to_Text_sr(wav_parts_path)
        result_text.append(result)
        num_chara.append(len(result_text[i]))
        Write_Text(TEXT_PATH_1, result_text[i], "a")
        
    num_chara_sum = sum(num_chara)
    print(num_chara_sum)
    """
    MOVIE_PATH = f'MovieFile/{WHO}.mp4'
WAV_PATH_ORI = f'WaveFile/{WHO}.wav'
WAV_PATH = f'WaveFile/{WHO}_MONO.wav'
WAV_PARTS_PATH = f'WavePartsFile/{WHO}_0'
WAV_PARTS_PATH_1 = f'WavePartsFile/{WHO}_1.wav'
WAV_PARTS_PATH_2 = f'WavePartsFile/{WHO}_2.wav'
WAV_PARTS_PATH_3 = f'WavePartsFile/{WHO}_3.wav'
TEXT_PATH_1 = f'TextFile/{WHO}_1.txt'
TEXT_PATH_2 = f'TextFile/{WHO}_2.txt'
TEXT_PATH_3 = f'TextFile/{WHO}_3.txt'
#その1
    Wav_Divide(WAV_PATH, 0, 30, WAV_PARTS_PATH_1)
    result_text_1 = Speech_to_Text_sr(WAV_PARTS_PATH_1)
    num_chara_1 = len(result_text_1)
    Write_Text(TEXT_PATH_1, result_text_1, "w")
    #その2
    Wav_Divide(WAV_PATH, 30, 60, WAV_PARTS_PATH_2)
    result_text_2 = Speech_to_Text_sr(WAV_PARTS_PATH_2)
    num_chara_2 = len(result_text_2)
    Write_Text(TEXT_PATH_2, result_text_2, "w")
    #その3

    Wav_Divide(WAV_PATH, 40, 60, WAV_PARTS_PATH_3)
    result_text_3 = Speech_to_Text_sr(WAV_PARTS_PATH_3)
    num_chara_3 = len(result_text_3)
    Write_Text(TEXT_PATH_3, result_text_3, "w")
    print(num_chara_1 + num_chara_2 + num_chara_3)
    """
    
    #monoに変換したら0~30[s]は102字と30~60[s]は157字
    