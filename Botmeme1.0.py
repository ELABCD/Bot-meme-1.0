import os
import random
import discord
import requests

# Configuración del cliente
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Conectado como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '/memeprog':
        try:
            # Ruta completa a la carpeta de imágenes
            image_folder = 'C:/User/OneDrive/Escritorio/Proyecto/Memes-Programacion-1.0'
            
            # Obtener todos los archivos de la carpeta
            image_files = os.listdir(image_folder)
            
            # Filtrar solo archivos .jpg
            image_files = [file for file in image_files if file.endswith('.jpg')]

            if image_files:
                # Seleccionar un archivo aleatorio
                selected_image = random.choice(image_files)
                file_path = os.path.join(image_folder, selected_image)

                # Imprimir la ruta para depuración
                print(f'Intentando abrir: {file_path}')

                # Abrir y enviar la imagen seleccionada
                with open(file_path, 'rb') as f:
                    picture = discord.File(f)
                    await message.channel.send(file=picture)
            else:
                await message.channel.send("No se encontraron imágenes en la carpeta.")

        except Exception as e:
            await message.channel.send(f"Ocurrió un error: {e}")

    elif message.content == '/duck':
        try:
            # Obtener URL de imagen de pato
            image_url = get_duck_image_url()
            await message.channel.send(image_url)
        except Exception as e:
            await message.channel.send(f"Ocurrió un error: {e}")

def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

client.run('TOKEN')
