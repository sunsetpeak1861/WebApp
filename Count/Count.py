import ui

# 変数を宣言
number = 0

# プラスボタンをタップしたときに呼ばれるメソッド

def plus(sender):
	# グローバル変数numberを使う
	global number
	
	# Labelの設定
	# senderはこの後Buttonと紐付けます。
	# 'label'は、Count.pyuiでLabelの設定をした時に確認した名前です。
	# つまり、「Buttonの親Viewに置いてある、'label1'という名前の部品」という意味ですね。
	# XCodeでの開発におけるIBOutletの関連づけと同じような事をここで行っていると言えます。
	label = sender.superview['label1']
	
	# numberの値を1増やしてlabelのtextに反映させる
	number += 1
	label.text = str(number)
	
	# 10以上だったら赤にする
	if number >= 10:
		label.text_color = 'red'
	
# ボタンをタップしたときに呼ばれるメソッド
def clear(sender):
	global number
	label = sender.superview['label1']
	
	number = 0
	label. text = str(number)
	
v = ui.load_view()
v.present('sheet')
