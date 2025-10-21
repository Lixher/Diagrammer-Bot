# nodes.py (новая версия с поддержкой типов узлов)

def add_node(diagram: dict, content_type: str, content_data: str):
    """
    Добавляет новый узел (блок) в диаграмму.

    :param diagram: Словарь с данными диаграммы.
    :param content_type: Тип узла, 'text' или 'image'.
    :param content_data: Текст для узла или путь к файлу изображения.
    """
    diagram["node_counter"] += 1
    new_node_id = diagram["node_counter"]
    
    # Новая структура узла
    new_node = {
        "id": new_node_id,
        "type": content_type,
        "content": content_data # Здесь либо текст, либо путь к картинке
    }
    
    diagram["nodes"].append(new_node)

def delete_node(diagram: dict, node_id: int):
    # Логика удаления узла остается прежней, так как мы удаляем по ID
    diagram['nodes'] = [node for node in diagram['nodes'] if node['id'] != node_id]
    diagram['edges'] = [
        edge for edge in diagram['edges'] 
        if edge['from'] != node_id and edge['to'] != node_id
    ]

def edit_node_text(diagram: dict, node_id: int, new_label: str):
    # Теперь эта функция работает только для текстовых узлов
    for node in diagram['nodes']:
        if node['id'] == node_id and node['type'] == 'text':
            node['content'] = new_label
            break