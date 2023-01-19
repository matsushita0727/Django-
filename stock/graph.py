import matplotlib.pyplot as plt
import base64
from io import BytesIO

#プロットしたグラフを画像データとして出力するための関数
def Output_Graph():
	buffer = BytesIO()                   #バイナリI/O(画像や音声データを取り扱う際に利用)
	plt.savefig(buffer, format="png")    #png形式の画像データを取り扱う
	buffer.seek(0)                       #ストリーム先頭のoffset byteに変更
	img   = buffer.getvalue()            #バッファの全内容を含むbytes
	graph = base64.b64encode(img)        #画像ファイルをbase64でエンコード
	graph = graph.decode("utf-8")        #デコードして文字列から画像に変換
	buffer.close()
	return graph

#グラフをプロットするための関数
def Plot_Graph(x,y):
	plt.switch_backend("AGG")        #スクリプトを出力させない
	plt.figure(figsize=(10,5))       #グラフサイズ
	plt.bar(x,y)                     #グラフ作成
	plt.xticks(rotation=45)          #X軸値を45度傾けて表示
	plt.title("inventory per created_at")    #グラフタイトル
	plt.xlabel("created_at")               #xラベル
	plt.ylabel("inventory")             #yラベル
	plt.tight_layout()               #レイアウト
	graph = Output_Graph()           #グラフプロット
	return graph