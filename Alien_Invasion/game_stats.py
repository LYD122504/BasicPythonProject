class GameStats():
    '''跟踪游戏的统计信息'''
    def __init__(self,setting,player_name):
        '''初始化统计信息'''
        self.setting=setting
        # 游戏刚启动时处于活动状态
        self.game_active=False
        self.reset_stats()
        # 存储最高分,任何情况下都不会重置最高得分
        self.high_score=0
        # 存储当前玩家用户名
        self.current_player_name=player_name
        self.load_high()
        if self.rank_list:
            self.high_score=self.rank_list[0][1]

    def reset_stats(self):
        '''初始化在游戏运行期间可能变化的统计信息'''
        self.ships_left=self.setting.ship_limit 
        self.score=0
        self.level=1
    
    def load_high(self):
        # 创建记录排行榜列表
        self.rank_list=[]
        with open('high_score.txt','r',encoding='utf-8') as f:
            for row in f:
                row=row.strip()
                row_list=row.split(',')
                if row_list[1]:
                    row_list[1]=int(row_list[1])
                    if not row_list[0]:
                        row_list[0]='NULL'
                    self.rank_list.append(row_list)
    
    def save_scores(self):
        self.rank_list.append([self.current_player_name,self.score])
        self.rank_list.sort(key=lambda x:x[1],reverse=True)
        self.rank_list=self.rank_list[:10]
        with open('high_score.txt', 'w', encoding='utf-8') as f:
            # 2. 遍历你整理好的排行榜列表
            for entry in self.rank_list:
                # 3. 构造一行字符串： "名字,分数\n"
                line = entry[0] + "," + str(entry[1]) + "\n"
                # 4. 写入文件
                f.write(line)