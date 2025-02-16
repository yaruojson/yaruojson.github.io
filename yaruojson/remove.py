import os

# 削除したい文字列（この文字列が含まれる行を削除します）
target_string = """<a href="http://blog-imgs-88.fc2.com/o/y/o/oyoguyaruo"""

# 対象のフォルダパス（適宜変更してください）


def process_folder(target_folder):
    for root, dirs, files in os.walk(target_folder):
        for file in files:
            # 拡張子が .txt のファイルのみ対象
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                # 読み込み（エンコーディングはファイルに合わせて変更してください）
                with open(file_path, "r", encoding="utf-8") as f:
                    lines = f.readlines()

                # 行ごとに対象文字列が含まれていなければ出力
                with open(file_path, "w", encoding="utf-8") as f:
                    for line in lines:
                        if target_string not in line:
                            f.write(line)


if __name__ == "__main__":
    # 処理対象のフォルダパスをユーザから入力
    folder_path = input("処理するフォルダのパスを入力してください: ")
    process_folder(folder_path)
