import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
from search import search_news

load_dotenv()

pesquisa = search_news('M1TA34')

EMAIL_ADDRESS = os.getenv('EMAIL_USER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASS')

news_body = ''

for news in pesquisa:
    news_body += f'''
        <col align="center">
            <h4>
                {news["title"]}
            </h4>
            <figure>
                <img src="{news["img"]}"/>
                <figcaption>
                    <a href="{news["link"]}">Link da notícia</a>
                </figcaption>
            </figure>
        </col>
    '''

html = """
<html>

<head>
    <style>
    </style>
</head>

<body>
    <center>
        <h2>Notícias das suas ações dos últimos 7 dias</h2>
        %s
    </center>
</body>

</html>
""" % news_body


msg = EmailMessage()
msg['Subject'] = 'Últimas notícias da sua carteira de ações'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'guilhermewaizbart@gmail.com'
msg.set_content(html, subtype='html')

with smtplib.SMTP('smtp.sapo.pt', 587) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
