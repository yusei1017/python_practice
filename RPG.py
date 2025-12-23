import rpg_utility
import os
def clear():
    os.system("clear")


#---開始---
clear()
print("ようこそいでゆうせいRPGへ")
name=input("名前を入力してください：")
clear()
if name=="":
    name=input("名前をもう一度入力してください")
    clear()


#---playeデータ----
atk=rpg_utility.random_status(1,6)
defence=rpg_utility.random_status(1,3)
hp=rpg_utility.random_status(20,30)
player={"name":name,"atk":atk,"defence":defence,"hp":hp,"items":[{"name":"薬草","stock":0,"heal":10},{"name":"ポーション","stock":0,"heal":10}]}

#----キャラステータス表示----
print(f"{name}のステータスは以下の通りです")
print(f"[攻撃力:{player['atk']}/防御力:{player['defence']}/HP:{player['hp']}]")
print(f"[アイテム所持数 {player['items'][0]['name']}:{player['items'][0]['stock']}/{ player['items'][1]['name']}:{player['items'][1]['stock']}]")
print("それでは冒険に出発だ!")
clear()



#----enemy1データ----
ene1_atk=rpg_utility.random_status(1,2)
ene1_defence=rpg_utility.random_status(0,1)
ene1_hp=rpg_utility.random_status(10,20)
ene1_name="ゴブリン"
enemy1={"name":ene1_name,"atk":ene1_atk,"def":ene1_defence,"hp":ene1_hp}
#---enemy2データ----
ene2_atk=rpg_utility.random_status(1,4)
ene2_defence=rpg_utility.random_status(1,2)
ene2_hp=rpg_utility.random_status(10,30)
ene2_name="オーク"
enemy2={"name":ene2_name,"atk":ene2_atk,"def":ene2_defence,"hp":ene2_hp}
#----enemy3データ----
ene3_atk=rpg_utility.random_status(1,6)
ene3_defence=rpg_utility.random_status(1,3)
ene3_hp=rpg_utility.random_status(20,30)
ene3_name="盗賊"
enemy3={"name":ene3_name,"atk":ene3_atk,"def":ene3_defence,"hp":ene3_hp}


enemies=[enemy1,enemy2,enemy3]

for enemy in enemies:

    #----enemyの表示----
    print(f"{enemy['name']}が現れた!")
    print(f"[攻撃力:{enemy['atk']},HP:{enemy['hp']},防御力:{enemy['def']}]")
    #----攻撃表示-----
    is_guard=False
    while enemy["hp"]>0 and player["hp"]>0:
        
        print("-----プレイヤーのターン------")
        print(f"[{player['name']} 攻撃力:{player['atk']}/防御力:{player['defence']}/HP:{player['hp']}]")
        print("攻撃を選択")
        print("a:攻撃,s:防御,d:アイテム使用")
        command=input("コマンドを入力：")
        if command=="a":
            enemy["hp"]=enemy["hp"]-player["atk"]
            print(f"{enemy['name']}に{player['atk']}ダメージ与えた！")
        elif command=="s":
            print("防御する")
            is_guard=True
        elif command=="d":
            print("バックを開いた")
            if player['items'][0]["stock"]== 0:
                print("何も持っていない")
            else :
                player['items'][0]["stock"]= player['items'][0]["stock"]- 1
                player['hp']=player['hp']+ player['items'][0]["heal"]
                print(f"{hp}を10回復した 現在のHp:{player['hp']}")
        else :
            print("無効なコマンド")
    #---敵の反撃----
        if enemy["hp"]>0 :  
            print("----敵のターン-----")
            print(f"[{enemy['name']} 攻撃力:{enemy['atk']}/HP:{enemy['hp']}]")
            damage=enemy['atk']
            if is_guard :
                damage=enemy['atk']/2
                if damage< 1:
                    damage=0
            player['hp']=player['hp']-damage
            print(f"{damage}ダメージを受けた！") 

            input("Enterキーで次のターンへ")
            clear()
            
        #----勝利-----   
    if enemy['hp'] <= 0:
            print("-----勝利-------")
            print("アイテムを獲得した!")
            player["items"][0]["stock"]= player["items"][0]["stock"]+1
            print(f"[アイテム所持数 {player['items'][0]['name']}:{player['items'][0]['stock']}/{ player['items'][1]['name']}:{player['items'][1]['stock']}]")
            input("次の敵へ")
            clear()
            
        #-----敗北-------    
    if player["hp"] <=0:
            print("ゲームオーバー")
            break  
else :
    print("ゲームクリア!")