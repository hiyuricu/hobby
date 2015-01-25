#!/usr/bin/python
# -*- coding: utf-8 -*-

import random, copy

player_dic = {}
card_dic = {}
temp_dic = {}

j = -1
card_value_list = range(1, 14) * 4
card_number_list = range(1, 53)
random.shuffle(card_number_list)

for i in card_number_list:
	j += 1
	card_dic[i] = card_value_list[j]

def choose_card(player):
	return_dic = card_dic
	print "以下の数値からカードを選んで下さい。"
	while True:
		again_flag = True
		print return_dic.keys()
		print "カードの場所:",
		input_line = raw_input()
		try:
			print "カードの値:", return_dic[int(input_line)]
			choose_card1_value = return_dic[int(input_line)]
			temp_dic = copy.deepcopy(return_dic)
			del temp_dic[int(input_line)]

			print "以下の数値からカードを選んで下さい。"
			while True:
				print temp_dic.keys()
				print "カードの場所:",
				input_line = raw_input()
				try:
					print "カードの値:", temp_dic[int(input_line)]
					if choose_card1_value == temp_dic[int(input_line)]:
						print "当たりました！"
						del temp_dic[int(input_line)]
						return_dic = temp_dic
						player_dic[player] += 1
						if len(return_dic) != 0:
							again_flag = False
					break
				except:
					print "その数値のカードはありません。もう一度以下の数値からカードを選んで下さい。"

			if again_flag:
				break
			else:
				print "もう一度以下の数値からカードを選んで下さい。"
		except:
			print "その数値のカードはありません。もう一度以下の数値からカードを選んで下さい。"

	return return_dic


print "ルール説明とか"
print "プレイヤー人数を数値で入力して下さい(二人なら'2'、三人なら'3'のように)"
input_line1 = raw_input()

print "プレイヤーの名前を入力してください"
for i in range(1, int(input_line1) + 1):
	print "%s人目の名前" % i
	input_line2 = raw_input()
	player_dic[input_line2] = 0


while len(card_dic) != 0:
	for player in player_dic.keys():
		print "------------%sさんの番です--------------" % player
		card_dic = choose_card(player)
		print "%sさんが現在獲得したペア数は%iです。" % (player, player_dic[player])
		if len(card_dic) == 0:
			break

print "ゲーム終了です。\n-----------ゲーム結果------------"
for k,v in sorted(player_dic.items(), key=lambda x:x[1], reverse=True):
	print "%sさんの獲得ペア数:%iペア" % (k,v)



