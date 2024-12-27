from collections import deque

# BFS fonksiyonu
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    visited_order = []  # Ziyaret edilen düğümlerin sırasını takip etmek için bir liste
    print(f"Başlangıç düğümü: {start}")

    while queue:
        node = queue.popleft()
        print(f"Ziyaret edilen düğüm: {node}")
        visited_order.append(node)

        for neighbor in graph[node]:
            print(f"{node} düğümünün komşusu: {neighbor}")
            if neighbor not in visited:
                print(f"  {neighbor} daha önce ziyaret edilmedi, kuyruğa ekleniyor")
                queue.append(neighbor)
                visited.add(neighbor)

    print("Ziyaret edilen düğümlerin sırası:", visited_order)

# Kullanıcıdan graf girdisi alınması için fonksiyon
def get_user_input():
    graph = {}
    vertices = int(input("Düğüm sayısını girin: "))
    for i in range(vertices):
        node = input(f"{i+1}. düğümü girin: ")
        connections = input(f"{node} düğümünün komşularını girin (virgülle ayrılmış): ").split(',')
        graph[node] = connections
        print(f"{node} düğümü ve bağlantıları: {connections}")

    return graph

# Ana fonksiyon
def main():
    graph = get_user_input()
    start_node = input("Başlangıç düğümünü girin: ")
    bfs(graph, start_node)

if __name__ == "__main__":
    main()
