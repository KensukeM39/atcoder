from collections import deque, defaultdict

def solve_shortest_shiritori(start_word, goal_word, word_list):
    """
    start_wordからgoal_wordまでの最短しりとり経路を探索する関数
    """
    
    # 1. グラフの構築 (前処理)
    # 検索を高速化するため、
    # 「ある文字(key)で始まる単語のリスト(value)」という辞書を作ります。
    # 例: {'e': ['element', 'elephant'], 't': ['tiger']}
    words_by_first_char = defaultdict(list)
    for word in word_list:
        if not word: continue # 空文字対策
        first_char = word[0]
        words_by_first_char[first_char].append(word)

    # 2. BFS (幅優先探索) の準備
    # queueには (現在の単語, ここまでの経路リスト) を格納します
    queue = deque()
    queue.append((start_word, [start_word]))
    
    # 無限ループを防ぐために、一度使った単語は記録しておきます
    visited = set()
    visited.add(start_word)
    
    print(f"開始: {start_word} -> 目標: {goal_word}")
    print("-" * 30)

    # 3. 探索ループ
    while queue:
        current_word, path = queue.popleft()
        
        # ゴールに到達したかチェック
        if current_word == goal_word:
            return path
        
        # 次のステップを探す
        # 現在の単語の「最後の文字」を取得
        last_char = current_word[-1]
        
        # その文字で始まる単語候補を取得
        next_candidates = words_by_first_char[last_char]
        
        for next_word in next_candidates:
            if next_word not in visited:
                visited.add(next_word)
                # 新しい経路を作ってキューに追加
                new_path = path + [next_word]
                queue.append((next_word, new_path))
    
    # 4. ループを抜けてもゴールに着かなかった場合
    return None

# --- テスト実行 ---

def run_test():
    # 使用する単語リスト
    words = [
        "apple", "element", "train", "net", 
        "tiger", "robot", "tensor", "road", "dog"
    ]
    
    # ケース1: つながる場合
    start = "apple"
    goal = "robot"
    # 予想: apple -> element -> tiger -> robot
    
    result = solve_shortest_shiritori(start, goal, words)
    
    if result:
        print(f"最短経路が見つかりました (長さ: {len(result)})")
        print(" -> ".join(result))
    else:
        print("経路が見つかりませんでした。")

    print("\n" + "="*30 + "\n")

    # ケース2: つながらない場合
    start2 = "dog"
    goal2 = "apple"
    result2 = solve_shortest_shiritori(start2, goal2, words)
    
    if result2:
        print(f"最短経路が見つかりました: {result2}")
    else:
        print(f"開始: {start2} -> 目標: {goal2}")
        print("経路が見つかりませんでした。(dogで終わるgから始まる単語がない)")

run_test()