s = {
"Host": "ticket.interpark.com",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",
"Referer": "https://ticket.interpark.com/PCampingBook/BookSeat.asp?GoodsCode=21004842&PlaceCode=21000348&TmgsOrNot=D2006&LocOfImage=&KindOfGoods=01015&BizCode=42955&PlayDate=20220403&PlaySeq=229&PlaySeqList=229&SessionId=A99DF09418FF460ABDA71DAEEC70638D&BizMemberCode=&GoodsBizCode=42838&BizMemberFlag=Non",
"Cookie": "_SHOP_PC_ID=20220225221120525950648; pcid=164579468115291458; tourGUID=523018ec-50a0-4981-a1ce-76947012518c; ab.storage.sessionId.9f6f8142-b257-4385-abe1-6596c3f44be3=%7B%22g%22%3A%22b32ca800-dd07-f2a9-c1a8-b23dea0e0ca9%22%2C%22e%22%3A1646669093278%2C%22c%22%3A1646667293278%2C%22l%22%3A1646667293278%7D; ab.storage.deviceId.9f6f8142-b257-4385-abe1-6596c3f44be3=%7B%22g%22%3A%22f1f767b4-f084-01d6-77db-34ed317dc76c%22%2C%22c%22%3A1646667293282%2C%22l%22%3A1646667293282%7D; _gac_UA-86011220-3=1.1646667293.Cj0KCQiA95aRBhCsARIsAC2xvfy0lonatroBT7UUs8R9JQM8h3PW_5rhWvGzi3c91HXk5mgpIW-sukUaAhLmEALw_wcB; _gac_UA-86011220-1=1.1646667293.Cj0KCQiA95aRBhCsARIsAC2xvfy0lonatroBT7UUs8R9JQM8h3PW_5rhWvGzi3c91HXk5mgpIW-sukUaAhLmEALw_wcB; _gac_UA-93889457-1=1.1646667293.Cj0KCQiA95aRBhCsARIsAC2xvfy0lonatroBT7UUs8R9JQM8h3PW_5rhWvGzi3c91HXk5mgpIW-sukUaAhLmEALw_wcB; _trs_id=eY4%3E624%3F5235%3F5%3F6; _BS_GUUID=ytujI7xWI6YJuc12WSs8x5UXGmrQkCbS6FcOMKKu; _TRK_AUIDA_13778=06dbaa030cf2406a69f00650e0c2f5ae:1; _ga=GA1.1.1015826225.1646667293; _ga_4SKTL7E8Q8=GS1.1.1646667293.1.0.1646667293.0; cto_bundle=AXr4919tUUZ2WUpGZG10dmpKNjFIUEhGdkhROVRudEtZdzQzJTJCQlpXaWlwMW1EdHp0bng1NVllQ3VLdTVwNU9heTBQJTJGM3NudTBjUWtNOTBEcmxoMzRpaG9QbWtRcmxsUjBLelR1enBQSVBTNE54JTJCVlZwMmRRdktHSCUyRmJIT1dnU2tuS0QwMDZjVVBzMWxucDNSQ0pPckl0SlMlMkJBJTNEJTNE; PMFlag=MWa3%2F5DoIr4w25ucoIt2DQ%3D%3D; PMBizCode=%2B%2F57hgW0n2KdG2s89B%2FTFg%3D%3D; PMCode=; PMID=; PMName=; PMGrade=; PMAgree=gd%2BzEjhN0HbDaf%2FwK7Uu8w%3D%3D; PMSecLogin=CHSkLoVxzDU2TjyeRybJuA%3D%3D; ASPSESSIONIDSGDCDSQA=EFCOIBGBCCFKICFHLAODOILO; TMem%5FNO=; ASPSESSIONIDSEDCDSTB=ANPPPFMBDIEHJJILFIJFFMOI; ASPSESSIONIDQUDSQRCQ=KAJHBHMBDIBMLMKJFGLJIIHI; ASPSESSIONIDSEAAAQTC=ONJFHPLBKBPDHDIHOFKAIKDH; ASPSESSIONIDQGAACRQD=HMGLJFKBLKMPLMELDLGBBFIC; TSession%5FID=A99DF09418FF460ABDA71DAEEC70638D; ASPSESSIONIDQWCRRSCQ=ECLHHFKBKBPPMAIDLLECFBHG; ASPSESSIONIDSGSBTCQA=IAKHCHMBLCOLPNGOLDBBHEIL"
}

import requests, time,json, xmltodict
url = "https://ticket.interpark.com/PCampingBook/Lib/BookInfoXml.asp?Flag=AllBlock&GoodsCode=21004842&PlaceCode=21000348&PlaySeqList=229&TmgsOrNot=D2006"
from datetime import datetime

while True:
	result = requests.get(url=url, headers=s, timeout=15)
	now = datetime.now()
	# print(json.dumps(result.json()),indent=4)
	data = xmltodict.parse(result.text) 
	isItem = data["NewDataSet"]["Table"]
	for Item in isItem:
		if int(Item["RemainCnt"]) > 0:
			print(f"{Item['SeatGradeName']}-{Item['RemainCnt']} 에약이 가능합니다!!!!")
			exit(-1)

	print(now.strftime("%Y-%m-%d %H:%M:%S") + json.dumps(xmltodict.parse(result.text), indent=4) + "\r\n")
	time.sleep(10)
