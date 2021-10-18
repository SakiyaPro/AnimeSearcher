import json


FILE_PATH = "./json/anime-title.json"


def load_json(FILE_PATH):
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def update_json(FILE_PATH, json_data):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)


def main():
    json_data = load_json(FILE_PATH)
    json_data["一週間フレンズ。"] = {
        "画像": "img/anime-image/一週間フレンズ。.jpg",
        "評価": 4.5,
        "あらすじ": """高校生・長谷祐樹は、いつも一人きりでいるクラスメイトの藤宮香織と仲良くなりたいと思い、彼女に近づこうとする。しかし、彼女はそれを頑なに拒む。その理由は、「1週間で友達との記憶を無くしてしまう」からだった…。

だが、それでも祐樹はひたむきに、香織との仲を紡いでいこうとする。祐樹の親友でクールな桐生将吾や、天然系の忘れっぽい性格の山岸沙希との交流を通して、香織は少しずつだが友達のことを記憶できるようになっていく。

そんな中、香織の小学校の頃のクラスメイトの九条一が転校してきた事から、香織は再び記憶を失ってしまう。小学生時代、仲の良かった二人は、それが元で親友だった女子たちから非難され、そのショックから香織は記憶を失ってしまったのだ。記憶喪失の原因を思い出し乗り越えたことで、香織の症状は改善の兆候を見せ、祐樹との関係も変化していく……。"""
    }
    update_json(FILE_PATH, json_data)


if __name__ == "__main__":
    main()
