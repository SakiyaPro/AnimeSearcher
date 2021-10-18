# coding: UTF-8
import sqlite3


# anime_dbにデータを追加する関数
def insert_sqlite(title, star, story, img_path):
    # dbの作成
    # 既に存在している場合はアクセスされる
    sqlite_path = "db.sqlite3"
    connection = sqlite3.connect(sqlite_path)

    # cursorの作成
    cursor = connection.cursor()

    # 値の追加
    cursor.execute('INSERT INTO anime_db (title, star, story, img_path) VALUES (?, ?, ?, ?))',
                    (title, star, story, img_path))
    connection.commit()
    connection.close()
    print("finish insert!")


# anime_dbのデータを更新する関数
def update_sqlite(title=None, star=None, story=None, img_path=None, *, id):
    '''
    idは必ず指定する。(どのレコードを編集するか判別するため)
    '''
    # dbの作成
    # 既に存在している場合はアクセスされる
    sqlite_path = "db.sqlite3"
    connection = sqlite3.connect(sqlite_path)

    # cursorの作成
    cursor = connection.cursor()

    # 値の更新
    if title:
        cursor.execute('UPDATE anime_db SET title=? WHERE id=?', (title, id))
    if star:
        cursor.execute('UPDATE anime_db SET star=? WHERE id=?', (star, id))
    if story:
        cursor.execute('UPDATE anime_db SET story=? WHERE id=?', (story, id))
    if img_path:
        cursor.execute(
            f'UPDATE anime_db SET img_path=? WHERE id=?', (img_path, id))
    connection.commit()
    connection.close()
    print("finish update!")


def main():
    # dbテーブルの作成。一回しか使わないのでコメントアウト。
    # 既に存在している場合は「"table anime_db already exists!"」を出力
    """ try:
        cursor.execute(
            'CREATE TABLE anime_db(id INTEGER PRIMARY KEY AUTOINCREMENT, title STRING, star REAL, story STRING, img_path STRING)'
        )
    except sqlite3.OperationalError:
        print("table anime_db already exists!") """

    update_sqlite(
        id=4, title="一週間フレンズ")


if __name__ == "__main__":
    main()
