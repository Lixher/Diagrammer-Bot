import os
from graphviz import Digraph
from PIL import Image, ImageDraw, ImageFont

if not os.path.exists('diagrams'): os.makedirs('diagrams')
if not os.path.exists('user_images'): os.makedirs('user_images')

def _add_watermark(image_path: str, text: str, theme: str):
    try:
        base_image = Image.open(image_path).convert("RGBA")
        txt_layer = Image.new("RGBA", base_image.size, (255, 255, 255, 0))
        font_size = 30
        try: font = ImageFont.truetype("arial.ttf", font_size)
        except IOError: font = ImageFont.load_default()
        draw = ImageDraw.Draw(txt_layer)
        fill_color = (255, 255, 255, 90) if theme == 'dark' else (0, 0, 0, 90)
        img_width, img_height = base_image.size
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]; text_height = text_bbox[3] - text_bbox[1]
        position = (img_width - text_width - 15, img_height - text_height - 15)
        draw.text(position, text, font=font, fill=fill_color)
        watermarked_image = Image.alpha_composite(base_image, txt_layer)
        watermarked_image.convert("RGB").save(image_path)
    except Exception as e:
        print(f"Ошибка при добавлении вотермарки: {e}")


def render_diagram(diagram_data: dict, user_id: int, theme: str = 'dark'):
    """
    Создает диаграмму с поддержкой изображений, используя АБСОЛЮТНЫЕ пути.
    """
    try:
        dot = Digraph(comment=f'Diagram for user {user_id}')
        
        if theme == 'dark':
            palette = {'bgcolor':'#1E1E2E','node_fill':'#2A2A3C','node_border':'#5E81AC','font_color':'#ECEFF4','edge_color':'#81A1C1','label_color':'#8899A6'}
            dot.attr('node', shape='rect', style='rounded,filled', penwidth='1.4', fontname='Inter, Helvetica, Arial, sans-serif', fontsize='12', margin='0.3,0.15')
            dot.attr('edge', arrowhead='vee', arrowsize='0.8', penwidth='1.1')
        else:
            palette = {'bgcolor':'#FAFAFA','node_fill':'#FFFFFF','node_border':'#CBD5E0','font_color':'#1A202C','edge_color':'#A0AEC0','label_color':'#667788'}
            dot.attr('node', shape='rect', style='rounded,filled', penwidth='1.2', fontname='Inter, Helvetica, Arial, sans-serif', fontsize='12', margin='0.25,0.15')
            dot.attr('edge', arrowhead='vee', arrowsize='0.7', penwidth='1.0')

        dot.attr('graph', bgcolor=palette['bgcolor'], pad='0.5', dpi='300', splines='spline', rankdir='TB', label='НАЧАЛО', fontcolor=palette['label_color'], fontsize='10')
        dot.attr('node', fillcolor=palette['node_fill'], color=palette['node_border'], fontcolor=palette['font_color'])
        dot.attr('edge', color=palette['edge_color'])

        for node in diagram_data.get('nodes', []):
            node_id_str = str(node.get('id'))
            
            if node.get('type') == 'image':
                relative_image_path = node.get('content')
                if os.path.exists(relative_image_path):

                    absolute_image_path = os.path.abspath(relative_image_path)
                    
                    dot.node(node_id_str, 
                             label='',
                             image=absolute_image_path,
                             shape='none',
                             width='1.5', height='1.5', fixedsize='true'
                    )
                else:
                    dot.node(node_id_str, '❗️ Изображение\nне найдено', shape='box', style='filled', fillcolor='#FFCCCC')
            else:
                dot.node(node_id_str, node.get('content', ''))

        for edge in diagram_data.get('edges', []):
            dot.edge(str(edge.get('from')), str(edge.get('to')))

        output_path = os.path.join('diagrams', f'user_{user_id}_{theme}')
        image_path = dot.render(output_path, format='png', cleanup=True)

        if image_path:
            _add_watermark(image_path, "@diagrammer_robot", theme)

        return image_path

    except Exception as e:
        print(f"Ошибка при рендеринге диаграммы: {e}")
        return None