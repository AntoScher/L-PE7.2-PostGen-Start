import os
os.environ['PYTHONHTTPSVERIFY'] = '0'  # Отключаем проверку SSL (если нужно)

from generators.text_gen import PostGenerator
from generators.image_gen import ImageGenerator
import config as conf
from unittest.mock import patch

# Создаем экземпляры
post_gen = PostGenerator(
    conf.openai_key,
    tone="позитивный и весёлый",
    topic="Новая коллекция кухонных ножей от компании ZeroKnifes"
)
img_gen = ImageGenerator(conf.openai_key)

# Мокаем методы
with patch.object(post_gen, 'generate_post', return_value="🔥 Новая коллекция ножей уже в продаже! Идеальные для вашей кухни!") as mock_post, \
     patch.object(post_gen, 'generate_post_image_description', return_value="Современные кухонные ножи на светлом фоне") as mock_img_desc, \
     patch.object(img_gen, 'generate_image', return_value="https://example.com/fake-image.jpg") as mock_image:

    # Вызываем методы
    content = post_gen.generate_post()
    img_desc = post_gen.generate_post_image_description()
    image_url = img_gen.generate_image(img_desc)

    print(content)
    print(image_url)