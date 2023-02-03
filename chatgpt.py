import openai
from bing_image_urls import bing_image_urls

def get_article(keyword, paragraph, apikey):
    openai.api_key = apikey

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt='i want to make article for seo purpose and ranking on google search engine.\ncreate an article about \"' + str(keyword) + '\" in relaxed english language.\nthe article consist of at least ' + str(paragraph) + ' paragraphs.\ncreate in html file form without html and body tag.\nfirst title using <h1> tag.\ninsert <br> tag after first title.\nsub title using <h2> tags.\nparagraphs must use <p> tags.',
        temperature=0.7,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response['choices'][0]['text']

def get_image(keyword):
    image = bing_image_urls(keyword, limit=2)
    return image[0]