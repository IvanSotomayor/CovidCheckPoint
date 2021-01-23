import requests

class Credential:
    def __init__(self, name, status, area, clearance):
        self.name = name
        self.status = status
        self.area = area
        self.clearance = clearance

class COVID:
    def __init__(self, date, days, validity):
        self.date = date
        self.days = days
        self.validity = validity

class Mask: 
    def __init__(self, wearsMask):
        self.wearsMask = wearsMask

class Dice: 
    def __init__(self, probability):
        self.probability = probability

while True:
    print('''
                                                                                                                                                                                ,----, 
               ,----..                                                               ,--,                            ,--.,-.----.       ,----..                    ,--.      ,/   .`| 
  ,----..     /   /   \                 ,---,    ,---,              ,----..        ,--.'|    ,---,.  ,----..     ,--/  /|\    /  \     /   /   \     ,---,       ,--.'|    ,`   .'  : 
 /   /   \   /   .     :        ,---.,`--.' |  .'  .' `\           /   /   \    ,--,  | :  ,'  .' | /   /   \ ,---,': / '|   :    \   /   .     : ,`--.' |   ,--,:  : |  ;    ;     / 
|   :     : .   /   ;.  \      /__./||   :  :,---.'     \         |   :     :,---.'|  : ',---.'   ||   :     ::   : '/ / |   |  .\ : .   /   ;.  \|   :  :,`--.'`|  ' :.'___,/    ,'  
.   |  ;. /.   ;   /  ` ; ,---.;  ; |:   |  '|   |  .`\  |        .   |  ;. /|   | : _' ||   |   .'.   |  ;. /|   '   ,  .   :  |: |.   ;   /  ` ;:   |  '|   :  :  | ||    :     |   
.   ; /--` ;   |  ; \ ; |/___/ \  | ||   :  |:   : |  '  |        .   ; /--` :   : |.'  |:   :  |-,.   ; /--` '   |  /   |   |   \ :;   |  ; \ ; ||   :  |:   |   \ | :;    |.';  ;   
;   | ;    |   :  | ; | '\   ;  \ ' |'   '  ;|   ' '  ;  :        ;   | ;    |   ' '  ; ::   |  ;/|;   | ;    |   ;  ;   |   : .   /|   :  | ; | ''   '  ;|   : '  '; |`----'  |  |   
|   : |    .   |  ' ' ' : \   \  \: ||   |  |'   | ;  .  |        |   : |    '   |  .'. ||   :   .'|   : |    :   '   \  ;   | |`-' .   |  ' ' ' :|   |  |'   ' ;.    ;    '   :  ;   
.   | '___ '   ;  \; /  |  ;   \  ' .'   :  ;|   | :  |  '        .   | '___ |   | :  | '|   |  |-,.   | '___ |   |    ' |   | ;    '   ;  \; /  |'   :  ;|   | | \   |    |   |  '   
'   ; : .'| \   \  ',  /    \   \   '|   |  ''   : | /  ;         '   ; : .'|'   : |  : ;'   :  ;/|'   ; : .'|'   : |.  \:   ' |     \   \  ',  / |   |  ''   : |  ; .'    '   :  |   
'   | '/  :  ;   :    /      \   `  ;'   :  ||   | '` ,/          '   | '/  :|   | '  ,/ |   |    \'   | '/  :|   | '_\.':   : :      ;   :    /  '   :  ||   | '`--'      ;   |.'    
|   :    /    \   \ .'        :   \ |;   |.' ;   :  .'            |   :    / ;   : ;--'  |   :   .'|   :    / '   : |    |   | :       \   \ .'   ;   |.' '   : |          '---'      
 \   \ .'      `---`           '---" '---'   |   ,.'               \   \ .'  |   ,/      |   | ,'   \   \ .'  ;   |,'    `---'.|        `---`     '---'   ;   |.'                     
  `---`                                      '---'                  `---`    '---'       `----'      `---`    '---'        `---`                          '---' 
  ''')
    print('''
    __     _____       _      _            
 /_ |   |_   _|     (_)    (_)           
  | |     | |  _ __  _  ___ _  __ _ _ __ 
  | |     | | | '_ \| |/ __| |/ _` | '__|                               
  | |_   _| |_| | | | | (__| | (_| | |                 
  |_(_) |_____|_| |_|_|\___|_|\__,_|_|   


  
  ___       _____       _ _      
 |__ \     / ____|     | (_)     
    ) |   | (___   __ _| |_ _ __ 
   / /     \___ \ / _` | | | '__|
  / /_ _   ____) | (_| | | | |   
 |____(_) |_____/ \__,_|_|_|_|   
                                 
                        
    ''')
    user_input = input()
    if user_input == 1:
        pass
    else:
        break



