def bidirectional_search(graph, start, goal):
    # İleri yönde kullanılacak BFS için gerekli veri yapıları
    forward_queue = [start]
    forward_visited = {start}
    forward_path = [start]
    print(f"İleri yönde kuyruk başlatıldı: {forward_queue}")

    # Geri yönde kullanılacak BFS için gerekli veri yapıları
    backward_queue = [goal]
    backward_visited = {goal}
    backward_path = [goal]
    print(f"Geri yönde kuyruk başlatıldı: {backward_queue}")

    while forward_queue and backward_queue:
        # İleri yönde BFS adımı
        current_forward = forward_queue.pop(0)
        print(f"Ileri Yönde: {current_forward} düğümü genişletiliyor")

        for neighbor in graph[current_forward]:
            if neighbor not in forward_visited:
                forward_visited.add(neighbor)
                forward_queue.append(neighbor)
                forward_path.append(neighbor)
                print(f"  {neighbor} komşusu ileri yönde kuyruğa eklendi")

                # İki yönlü arama noktası
                if neighbor in backward_visited:
                    print(f"Hedef düğüm {neighbor} üzerinden bulundu!")
                    print("İleri Yol:", forward_path)
                    print("Geri Yol:", backward_path)
                    return True

        # Geri yönde BFS adımı
        current_backward = backward_queue.pop(0)
        print(f"Geri Yönde: {current_backward} düğümü genişletiliyor")

        for neighbor in graph[current_backward]:
            if neighbor not in backward_visited:
                backward_visited.add(neighbor)
                backward_queue.append(neighbor)
                backward_path.append(neighbor)
                print(f"  {neighbor} komşusu geri yönde kuyruğa eklendi")

                # İki yönlü arama noktası
                if neighbor in forward_visited:
                    print(f"Hedef düğüm {neighbor} üzerinden bulundu!")
                    print("İleri Yol:", forward_path)
                    print("Geri Yol:", backward_path)
                    return True

    print("İki yönde de kesişme noktası bulunamadı")
    print("İleri Yol:", forward_path)
    print("Geri Yol:", backward_path)
    return False  # Hedef düğüm bulunamadı


# Kullanıcıdan graf girdisini alma
def get_user_input():
    graph = {}
    vertices = int(input("Düğüm sayısını girin: "))

    for i in range(vertices):
        node = input(f"{i + 1}. düğümü girin: ")
        connections = input(f"{node} düğümünün komşularını girin (virgülle ayrılmış): ").split(',')
        graph[node] = connections

    return graph


# Kullanıcıdan alınan graf üzerinde bidirectional search uygulama
def main():
    graph = get_user_input()
    start_node = input("Başlangıç düğümünü girin: ")
    goal_node = input("Hedef düğümü girin: ")

    print("Bidirectional Search Sonucu:")
    result = bidirectional_search(graph, start_node, goal_node)

    if not result:
        print("Hedef düğüm belirtilen yolda bulunamadı.")


if __name__ == "__main__":
    main()
