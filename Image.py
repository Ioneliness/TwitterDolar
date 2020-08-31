from PIL import Image, ImageDraw, ImageFont
from random import choice

lista = [
r'Images/Cinco.jpg',
r'Images/Dez.jpg',
r'Images/Dezenove.jpg',
r'Images/Dezesseis.jpg',
r'Images/Dezessete.jpg',
r'Images/Dezoito.jpg',
r'Images/Dois.jpg',
r'Images/Doze.jpg',
r'Images/Nove.jpg',
r'Images/Oito.jpg',
r'Images/Onze.jpg',
r'Images/Quatorze.jpg',
r'Images/Quatro.jpg',
r'Images/Quinze.jpg',
r'ImagesSeis.jpg',
r'Images/\Sete.jpg',
r'Images/Tres.jpg',
r'Images/Treze.jpg',
r'Images/Trinta.jpg',
r'Images/Um.jpg',
r'Images/Vinte.jpg',
r'Images/VinteCinco.jpg',
r'Images/VinteDois.jpg',
r'Images/VinteNove.jpg',
r'Images/VinteOito.jpg',
r'Images/VinteQuatro.jpg',
r'Images/VinteSeis.jpg',
r'Images/VinteSete.jpg',
r'Images/VinteTres.jpg',
r'Images/VinteUm.jpg']

def create_image(dolar):
    image = choice(lista)
    if image == r'Images/Um.jpg':
        img = Image.open(image)
        font = ImageFont.truetype('Fonts/Roboto-Medium.ttf', 85)
        draw = ImageDraw.Draw(img)
        draw.text((453, 336), dolar, font=font, fill=(255, 255, 255))
        img.save('atual.png', 'PNG')

    if image == r'Images/Dois.jpg':
        img = Image.open(image)
        font = ImageFont.truetype('Fonts/Roboto-Medium.ttf', 85)
        draw = ImageDraw.Draw(img)
        draw.text((455, 300), dolar, font=font, fill=(255, 255, 255))
        img.save('atual.png', 'PNG')
    
    if image == r'Images/Tres.jpg':
        img = Image.open(image)
        font = ImageFont.truetype('Fonts/Roboto-Medium.ttf', 85)
        draw = ImageDraw.Draw(img)
        draw.text((465, 337), dolar, font=font, fill=(255, 255, 255))
        img.save('atual.png', 'PNG')
    
    if image == r'Images/Quatro.jpg':
        img = Image.open(image)
        font = ImageFont.truetype('Fonts/Roboto-Medium.ttf', 105)
        draw = ImageDraw.Draw(img)
        draw.text((200, 345), dolar, font=font, fill=(255, 255, 255))
        img.save('atual.png', 'PNG')

    if image == r'Images/Cinco.jpg':
        img = Image.open(image)
        font = ImageFont.truetype('Fonts/Roboto-Medium.ttf', 105)
        draw = ImageDraw.Draw(img)
        draw.text((445, 308), dolar, font=font, fill=(255, 255, 255))
        draw.text((510, 524), '>//<', font=font, fill=(255, 255, 255))
        img.save('atual.png', 'PNG')

    if image == r'Images/Seis.jpg':
        img = Image.open(image)
        font = ImageFont.truetype('Fonts/Roboto-Medium.ttf', 115)
        draw = ImageDraw.Draw(img)
        draw.text((400, 320), dolar, font=font, fill=(255, 255, 255))
        img.save('atual.png', 'PNG')

    if image == r'Images/Sete.jpg':
        img = Image.open(image)
        font = ImageFont.truetype('Fonts/Roboto-Medium.ttf', 165)
        draw = ImageDraw.Draw(img)
        draw.text((335, 320), dolar, font=font, fill=(255, 255, 255))
        img.save('atual.png', 'PNG')

    if image == r'Images/Oito.jpg':
        img = Image.open(image)
        font = ImageFont.truetype('Fonts/Roboto-Medium.ttf', 75)
        draw = ImageDraw.Draw(img)
        draw.text((548, 295), dolar, font=font, fill=(255, 255, 255))
        img.save('atual.png', 'PNG')
    
    if image == r'Images/Nove.jpg':
        img = Image.open(image)
        font = ImageFont.truetype('Fonts/Roboto-Medium.ttf', 110)
        draw = ImageDraw.Draw(img)
        draw.text((410, 315), dolar, font=font, fill=(255, 255, 255))
        img.save('atual.png', 'PNG')
    
    if image == r'Images/Dez.jpg':
        img = Image.open(image)
        font = ImageFont.truetype('Fonts/Roboto-Medium.ttf', 90)
        draw = ImageDraw.Draw(img)
        draw.text((400, 280), dolar, font=font, fill=(255, 255, 255))
        img.save('atual.png', 'PNG')

    if image == r'Images/Onze.jpg':
        img = Image.open(image)
        font = ImageFont.truetype('Fonts/Roboto-Medium.ttf', 110)
        draw = ImageDraw.Draw(img)
        draw.text((475, 282), dolar, font=font, fill=(255, 255, 255))
        img.save('atual.png', 'PNG')

    if image == r'Images/Doze.jpg':
        img = Image.open(image)
        font = ImageFont.truetype('Fonts/Roboto-Medium.ttf', 105)
        draw = ImageDraw.Draw(img)
        draw.text((434, 225), dolar, font=font, fill=(255, 255, 255))
        img.save('atual.png', 'PNG')

    if image == r'Images/Treze.jpg':
        img = Image.open(image)
        font = ImageFont.truetype('Fonts/Roboto-Medium.ttf', 85)
        draw = ImageDraw.Draw(img)
        draw.text((495, 335), dolar, font=font, fill=(255, 255, 255))
        img.save('atual.png', 'PNG')
    
    if image == r'Images/Quatorze.jpg':
        img = Image.open(image)
        font = ImageFont.truetype('Fonts/Roboto-Medium.ttf', 155)
        draw = ImageDraw.Draw(img)
        draw.text((290, 299), dolar, font=font, fill=(255, 255, 255))
        img.save('atual.png', 'PNG')
    
    if image == r'Images/Quinze.jpg':
        img = Image.open(image)
        font = ImageFont.truetype('Fonts/Roboto-Medium.ttf', 85)
        draw = ImageDraw.Draw(img)
        draw.text((450, 465), dolar, font=font, fill=(255, 255, 255))
        img.save('atual.png', 'PNG')

    if image == r'Images/Dezesseis.jpg':
        img = Image.open(image)
        font = ImageFont.truetype('Fonts/Roboto-Medium.ttf', 95)
        draw = ImageDraw.Draw(img)
        draw.text((423, 265), dolar, font=font, fill=(255, 255, 255))
        img.save('atual.png', 'PNG')

    if image == r'Images/Dezessete.jpg':
        img = Image.open(image)
        font = ImageFont.truetype('Fonts/Roboto-Medium.ttf', 75)
        draw = ImageDraw.Draw(img)
        draw.text((527, 245), dolar, font=font, fill=(255, 255, 255))
        img.save('atual.png', 'PNG')

    if image == r'Images/Dezoito.jpg':
        img = Image.open(image)
        font = ImageFont.truetype('Fonts/Roboto-Medium.ttf', 85)
        draw = ImageDraw.Draw(img)
        draw.text((465,375), dolar, font=font, fill=(255, 255, 255))
        img.save('atual.png', 'PNG')

    if image == r'Images/Dezenove.jpg':
        img = Image.open(image)
        font = ImageFont.truetype('Fonts/Roboto-Medium.ttf', 140)
        draw = ImageDraw.Draw(img)
        draw.text((290,375), dolar, font=font, fill=(255, 255, 255))
        img.save('atual.png', 'PNG')

    if image == r'Images/Vinte.jpg':
        img = Image.open(image)
        font = ImageFont.truetype('Fonts/Roboto-Medium.ttf', 120)
        draw = ImageDraw.Draw(img)
        draw.text((390,465), dolar, font=font, fill=(255, 255, 255))
        img.save('atual.png', 'PNG')

    if image == r'Images/VinteUm.jpg':
        img = Image.open(image)
        font = ImageFont.truetype('Fonts/Roboto-Medium.ttf', 140)
        draw = ImageDraw.Draw(img)
        draw.text((580,135), dolar, font=font, fill=(255, 255, 255))
        img.save('atual.png', 'PNG')
    
    if image == r'Images//VinteDois.jpg':
        img = Image.open(image)
        font = ImageFont.truetype('Fonts/Roboto-Medium.ttf', 105)
        draw = ImageDraw.Draw(img)
        draw.text((245,395), dolar, font=font, fill=(255, 255, 255))
        img.save('atual.png', 'PNG')

    if image == r'Images/VinteTres.jpg':
        img = Image.open(image)
        font = ImageFont.truetype('Fonts/Roboto-Medium.ttf', 105)
        draw = ImageDraw.Draw(img)
        draw.text((435,435), dolar, font=font, fill=(255, 255, 255))
        img.save('atual.png', 'PNG')

    if image == r'Images/VinteQuatro.jpg':
        img = Image.open(image)
        font = ImageFont.truetype('Fonts/Roboto-Medium.ttf', 115)
        draw = ImageDraw.Draw(img)
        draw.text((375,465), dolar, font=font, fill=(255, 255, 255))
        img.save('atual.png', 'PNG')

    if image == r'Images/VinteCinco.jpg':
        img = Image.open(image)
        font = ImageFont.truetype('Fonts/Roboto-Medium.ttf', 95)
        draw = ImageDraw.Draw(img)
        draw.text((425,290), dolar, font=font, fill=(255, 255, 255))
        img.save('atual.png', 'PNG')
    
    if image == r'Images/VinteSeis.jpg':
        img = Image.open(image)
        font = ImageFont.truetype('Fonts/Roboto-Medium.ttf', 95)
        draw = ImageDraw.Draw(img)
        draw.text((385,455), dolar, font=font, fill=(255, 255, 255))
        img.save('atual.png', 'PNG')

    if image == r'Images/VinteSete.jpg':
        img = Image.open(image)
        font = ImageFont.truetype('Fonts/Roboto-Medium.ttf', 92)
        draw = ImageDraw.Draw(img)
        draw.text((465,235), dolar, font=font, fill=(255, 255, 255))
        img.save('atual.png', 'PNG')

    if image == r'Images/VinteOito.jpg':
        img = Image.open(image)
        font = ImageFont.truetype('Fonts/Roboto-Medium.ttf', 83)
        draw = ImageDraw.Draw(img)
        draw.text((552,310), dolar, font=font, fill=(255, 255, 255))
        img.save('atual.png', 'PNG')
    
    if image == r'Images/VinteNove.jpg':
        img = Image.open(image)
        font = ImageFont.truetype('Fonts/Roboto-Medium.ttf', 83)
        draw = ImageDraw.Draw(img)
        draw.text((485,275), dolar, font=font, fill=(255, 255, 255))
        img.save('atual.png', 'PNG')
    
    if image == r'Images/Trinta.jpg':
        img = Image.open(image)
        font = ImageFont.truetype('Fonts/Roboto-Medium.ttf', 83)
        draw = ImageDraw.Draw(img)
        draw.text((455,365), dolar, font=font, fill=(255, 255, 255))
        img.save('atual.png', 'PNG')
