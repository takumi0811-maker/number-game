# 数当てゲーム
# コンピューターが選んだ 1〜100 の数字を当てるゲームです。

import random  # ランダムな数字を作るためのモジュール

# 数字の範囲（ここを変えると難易度を変えられます）
MIN_NUMBER = 1
MAX_NUMBER = 100


def get_guess():
    """ユーザーから正しい予想（1〜100の整数）を受け取るまで繰り返す関数"""
    while True:
        text = input(f"{MIN_NUMBER}〜{MAX_NUMBER}の数字を入力してください: ")

        # 数字に変換できるかチェック（できなければエラーメッセージ）
        try:
            guess = int(text)
        except ValueError:
            print("エラー：数字を入力してください。")
            continue  # もう一度入力してもらう

        # 範囲内かチェック
        if guess < MIN_NUMBER or guess > MAX_NUMBER:
            print(f"{MIN_NUMBER}〜{MAX_NUMBER}の範囲で入力してください。")
            continue

        # 正しい入力なので返す
        return guess


def play_game():
    """1回分のゲームを行う関数"""
    # 正解の数字をランダムに決める（ユーザーには表示しない）
    answer = random.randint(MIN_NUMBER, MAX_NUMBER)
    count = 0  # 試行回数

    print("\n数字を選びました。当ててみてください！")

    while True:
        guess = get_guess()
        count += 1  # 有効な入力のときだけ回数を増やす

        if guess < answer:
            print("もっと大きい数字です！")
        elif guess > answer:
            print("もっと小さい数字です！")
        else:
            print(f"正解です！{count}回で当たりました！")
            break  # 正解したのでループを抜ける


def ask_play_again():
    """もう一度遊ぶかどうかを聞く関数（y なら True、n なら False）"""
    while True:
        answer = input("もう一度遊びますか？（y/n）: ").strip().lower()
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print("y か n で答えてください。")


def main():
    """ゲーム全体の流れ"""
    print("=== 数当てゲームへようこそ！ ===")

    while True:
        play_game()
        if not ask_play_again():
            break

    print("遊んでくれてありがとう！またね！")


# このファイルを直接実行したときだけゲームを始める
if __name__ == "__main__":
    main()
