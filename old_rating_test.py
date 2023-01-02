def calc_by_old_rating(new_defnum: int, old_rating: int ,plus_rating: int) -> float:
        if not new_defnum or new_defnum <= 0:
            # 谱面没定数或者定数小于等于0被视作Unrank
            return -1
        if not old_rating or old_rating <= 0:
            return -1
        old_defnum = new_defnum - plus_rating
        if old_rating == old_defnum+2:
            return calculate_rating(new_defnum,10000000)
        if old_defnum+1<=old_rating<old_defnum+2:
            return calculate_rating(new_defnum,9800000+200000*(old_rating - old_defnum - 1))
        else:
            return calculate_rating(new_defnum,9500000+300000*(old_rating - old_defnum))
        
def calculate_rating(defnum: int, score: int) -> float:
        '''计算rating，谱面定数小于等于0视为Unrank，这里的defnum = Chart const'''
        if not defnum or defnum <= 0:
            # 谱面没定数或者定数小于等于0被视作Unrank
            return -1

        if score >= 10000000:
            ptt = defnum + 2
        elif score < 9800000:
            ptt = defnum + (score-9500000) / 300000
            if ptt < 0:
                ptt = 0
        else:
            ptt = defnum + 1 + (score-9800000) / 200000

        return ptt
    
print(calc_by_old_rating(19.4,12.9999,8.4))