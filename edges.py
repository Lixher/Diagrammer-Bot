# edges.py

def add_edge(diagram: dict, from_node_id: int, to_node_id: int):
    """
    Добавляет новую связь (стрелку) в объект диаграммы.

    :param diagram: Словарь с данными диаграммы, который мы будем изменять.
    :param from_node_id: ID узла, ОТКУДА идет стрелка.
    :param to_node_id: ID узла, КУДА идет стрелка.
    """
    # Формируем словарь, описывающий новую связь
    new_edge = {
        "from": from_node_id,
        "to": to_node_id
    }

    # Ключевая проверка: добавляем связь, только если точно такой же еще нет.
    # Это предотвращает создание дубликатов стрелок между одними и теми же блоками.
    if new_edge not in diagram["edges"]:
        diagram["edges"].append(new_edge)

    # Функция ничего не возвращает, так как она напрямую изменяет
    # переданный ей объект 'diagram' (словари в Python передаются по ссылке).

    # edges.py (дополнить этой функцией)

def delete_edge(diagram: dict, from_node_id: int, to_node_id: int):
    """
    Удаляет связь между двумя узлами.

    :param diagram: Словарь с данными диаграммы.
    :param from_node_id: ID узла, откуда идет связь.
    :param to_node_id: ID узла, куда идет связь.
    """
    edge_to_delete = {"from": from_node_id, "to": to_node_id}
    # Создаем новый список, исключая ребро, которое нужно удалить
    diagram['edges'] = [edge for edge in diagram['edges'] if edge != edge_to_delete]