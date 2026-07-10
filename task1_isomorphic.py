def is_isomorphic(s: str, t: str) -> bool:
    # Если длины строк разные, они не могут быть изоморфными
    if len(s) != len(t):
        return False
    
    # Словари для хранения взаимно однозначного соответствия (биекции)
    map_s_to_t = {}
    map_t_to_s = {}
    
    for char_s, char_t in zip(s, t):
        # Проверяем отображение из s в t
        if char_s in map_s_to_t:
            if map_s_to_t[char_s] != char_t:
                return False
        else:
            map_s_to_t[char_s] = char_t
            
        # Проверяем отображение из t в s
        if char_t in map_t_to_s:
            if map_t_to_s[char_t] != char_s:
                return False
        else:
            map_t_to_s[char_t] = char_s
            
    return True

# Пример из условия
if __name__ == "__main__":
    s = 'paper'
    t = 'title'
    print(is_isomorphic(s, t))  # Вывод: True
