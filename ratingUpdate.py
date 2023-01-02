import sqlite3

conn = sqlite3.connect('ad_2100.db')
c = conn.cursor()
c1 = conn.cursor()

def update_chart(rating_plus:int):
    # First update rating_ftr
    c.execute('''update chart set rating_ftr = rating_ftr + ? where rating_ftr>0;''',(rating_plus*10,))
    c.execute('''update chart set rating_byn = rating_byn + ? where rating_byn>0;''',(rating_plus*10,))
    conn.commit()
    
def update_best_scores():
    c.execute('''select song_id,difficulty,score from best_score where rating>0;''')
    for row in c:
        if row[1] == 2:
            c1.execute('''select rating_ftr from chart where song_id=?;''',(row[0],))
            for row1 in c1:
                sql = 'update best_score set rating = '+ str(calculate_rating(row1[0]/10,row[2])) +' where song_id=\''+ str(row[0])+ '\' and difficulty='+str(row[1])+';'
                if calculate_rating(row1[0]/10,row[2])<=0:
                    continue
                c1.execute(sql)

        if row[1] == 3:
            c1.execute('''select rating_byn from chart where song_id=?;''',(row[0],))
            for row1 in c1:
                sql = 'update best_score set rating = '+ str(calculate_rating(row1[0]/10,row[2])) +' where song_id=\''+ str(row[0])+ '\' and difficulty='+str(row[1])+';'
                if calculate_rating(row1[0]/10,row[2])<=0:
                    continue
                c1.execute(sql)
        else:
            continue
    conn.commit()
        
def update_recent30(rating_plus: int):
    c.execute('''select * from recent30 where r0>=0;''')
    for row in c:
        for i in range(0,30):
            if row[2*i+1+1][-1:] == '2':
                c1.execute('''select rating_ftr from chart where song_id=?;''',(row[2*i+1+1][:len(row[2*i+1+1])-1],))
                for row1 in c1:
                    sql = 'update recent30 set ' + 'r'+str(i) + '=' + str(calc_by_old_rating(row1[0]/10,row[2*i+1],rating_plus)) + ' where user_id=' + str(row[0]) + ';'
                    c1.execute(sql)

            if row[2*i+1+1][-1:] == '3':
                c1.execute('''select rating_byn from chart where song_id=?;''',(row[2*i+1+1][:len(row[2*i+1+1])-1],))
                for row1 in c1:
                    sql = 'update recent30 set ' + 'r'+str(i) + '=' + str(calc_by_old_rating(row1[0]/10,row[2*i+1],rating_plus)) + ' where user_id=' + str(row[0]) + ';'
    conn.commit()
    
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

def calc_by_old_rating(new_defnum: int, old_rating: int ,plus_rating: int) -> float:
        if not new_defnum or new_defnum <= 0:
            # 谱面没定数或者定数小于等于0被视作Unrank
            return 0
        if not old_rating or old_rating <= 0:
            return 0
        old_defnum = new_defnum - plus_rating
        if old_rating == old_defnum+2:
            return calculate_rating(new_defnum,10000000)
        if old_defnum+1<=old_rating<old_defnum+2:
            return calculate_rating(new_defnum,9800000+200000*(old_rating - old_defnum - 1))
        else:
            return calculate_rating(new_defnum,9500000+300000*(old_rating - old_defnum))
            
# update_best_scores()
uprating = 8.4
# update_chart(uprating)
update_best_scores()
# update_recent30(uprating)
c.close()
conn.close()