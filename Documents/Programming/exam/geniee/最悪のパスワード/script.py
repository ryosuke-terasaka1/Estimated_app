import sys

symbol_set = {'@', '%', '$'}


def search_min_pass_length(string: str) -> int:
    
    # 最小値を見つけるので初期値を大きく設定する
    pass_length = 1000000
    
    # 初めの文字をstring[i], 終わりの文字をstring[j]として条件を満たす文字列を探索
    for i in range(len(string)):
        is_more_5_kind_str = False
        is_only_str = True
        is_symbol = False
        string_set = set()

        # 最低文字数のパスワードが決まった場合、探索を終了する
        if pass_length == 6:
            break

        for j in range(i, len(string)):
            
            # これまでに出力したパスワード以上の長さになった時点で探索を終了する
            if pass_length <= j - i + 1:
                break

            if string[j] not in string_set and string[j] not in symbol_set:
                string_set.add(string[j])
            
            # 条件を満たすかどうかの判定
            if len(string_set) >= 5:
                is_more_5_kind_str = True
            if string[j] in symbol_set:
                is_symbol = True
            if not (string[j].islower() or string[j] in symbol_set):
                is_only_str = False 

            # 条件を全て満たした場合にパスワードの長さを更新し、開始地点(string[i])を変える
            if (is_symbol and is_only_str and is_more_5_kind_str):
                pass_length = min(pass_length, (j - i + 1)) 
                break

    return pass_length


def main(lines: str) -> None:
    string = lines[0]

    pass_length = search_min_pass_length(string)

    # もし条件を満たす文字列がなかった場合、エラーを表示する
    if pass_length == 10000000:
        sys.stderr.write('作成できるパスワードはありません。')
        sys.exit(1)

    else: print(pass_length)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)

