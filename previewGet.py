# from pychorus import find_and_output_chorus
import os
from pydub import AudioSegment

path_vaild = []
path_invaild = []
path_final_error = []

# Function comes from 30-seconds-of-python
def in_range(n, start, end = 0):
  return start <= n <= end if end >= start else end <= n <= start

def path_find(input_path='.'):
    for root, dirs, files in os.walk(input_path, topdown=False):
        for n in dirs:
            n = os.path.join(root,n)
            print(n)
            if not os.path.exists(os.path.join(n,'preview.ogg')) and os.path.exists(os.path.join(n,'base.ogg')):
                path_vaild.append(n)
                continue
            print('Skip ', n)
                
def pychorus_try(single=1):
    for s in path_vaild:
        try:
    
            print('\nPychorus dealing, ',s)
            # find_and_output_chorus(os.path.join(s,'base.ogg'),os.path.join(s,'preview.ogg'))
            
            ogg_preview = AudioSegment.from_ogg(os.path.join(s,'preview.ogg'))
            ogg_preview.fade_in(1500).fade_out(1500).export(os.path.join(s,'preview.ogg'))
            
        except:
            if single == 1:
                path_final_error.append(s)
            else:
                path_invaild.append(s)
                
def pydub_try(single=1):
    if single == 1:
        path_pydub = path_vaild
    else:
        path_pydub = path_invaild
    for r in path_pydub:
    
        print('\nPydub dealing, ',r)
        try:
            ogg_base = AudioSegment.from_ogg(os.path.join(r,'base.ogg'))
            cut_second_mili = 0
        except:
            print('Audio is not readable.')
            path_final_error.append(r)
            continue
        segment_total_sec = int(int(ogg_base.duration_seconds))
        segment_volume = []
        for_times = 0
        high_ready_flag = False
        for s in range(0,segment_total_sec,5):
            for_times = int(s/5)
            song_part = ogg_base[s*1000:(s+5)*1000]
            segment_volume.append(song_part.dBFS)
            try:
                if not high_ready_flag and segment_volume[for_times - 1] < song_part.dBFS:
                    high_ready_flag = True
                    continue
                if in_range(song_part.dBFS,segment_volume[for_times - 2] -1, segment_volume[for_times - 2] +1):
                    cut_second_mili = (for_times -2) * 3 *1000
            except:
                continue
        part_cut = ogg_base[cut_second_mili:cut_second_mili + 15 * 1000]
        part_cut.fade_in(1500).fade_out(1500).export(os.path.join(r,'preview.ogg'))
        print(r,' has been exported.')


def __main__():
    method = 2
    input_path = input('输入songs目录路径，确保音频文件名为base.ogg，按照正确格式放置')
    
    path_find(input_path)
    
    if str(method) == '1':
        pychorus_try()
    elif str(method) == '2':
        pydub_try()
    else:
        pychorus_try(0)
        pydub_try(0)
        
    print('\nCannot be export correctly:')
    for p in path_final_error:
        print(p)
        
    print('Done.')
    
__main__()