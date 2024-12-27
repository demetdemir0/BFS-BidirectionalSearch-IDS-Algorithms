# Derinlik öncelikli arama (DFS) fonksiyonu
def dfs(graph, node, goal, depth):
    print(f"DFS: Şu anki düğüm {node}, derinlik {depth}")
    if depth == 0 and node == goal:
        print(f"Hedef düğüm {node} bulundu!")
        return True  # Hedef düğümü bulundu

    if depth > 0:
        for neighbor in graph[node]:
            print(f"{node} düğümünden {neighbor} komşusuna geçiş")
            if dfs(graph, neighbor, goal, depth - 1):
                return True  # Hedef düğümü bulundu
    return False  # Hedef düğümü bulunamadı


# Iteratif Derinleşen Arama (IDF) fonksiyonu
def idf(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"IDF: Derinlik sınırı {depth}")
        if dfs(graph, start, goal, depth):
            return True  # Hedef düğümü bulundu
    return False  # Hedef düğümü belirtilen derinlikte bulunamadı


# Kullanıcıdan graf girdisini alma
def get_user_input():
    graph = {}
    vertices = int(input("Düğüm sayısını girin: "))

    for i in range(vertices):
        node = input(f"{i + 1}. düğümü girin: ")
        connections = input(f"{node} düğümünün komşularını girin (virgülle ayrılmış): ").split(',')
        graph[node] = connections
        print(f"{node} düğümü ve bağlantıları: {connections}")

    return graph


# Kullanıcıdan alınan graf üzerinde IDF uygulama
def main():
    graph = get_user_input()
    start_node = input("Başlangıç düğümünü girin: ")
    goal_node = input("Hedef düğümü girin: ")
    max_depth = int(input("Maksimum derinlik seviyesini girin: "))

    print("IDDFS Sonucu:")
    result = idf(graph, start_node, goal_node, max_depth)

    if result:
        print("Hedef düğüm bulundu!")
    else:
        print("Hedef düğüm belirtilen derinlikte bulunamadı.")


if __name__ == "__main__":
    main()
