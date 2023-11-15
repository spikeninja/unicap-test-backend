import requests
from bs4 import BeautifulSoup

from app.ext.parsing import get_random_user_agent


def retrieve_page(url: str, referer: str | None) -> str:
    """"""
    print("Getting url: ", url)

    # add proxy?
    user_agent = get_random_user_agent('/usr/src/app/ext/user_agents.txt')
    headers = {
        'User-Agent': user_agent,
        'Accept-Encoding': 'gzip, deflate',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'Referer': referer or 'https://www.google.com/',
    }
    print("Headers Used: ", headers)
    response = requests.get('https://www.olx.pl/moda/zegarki/', headers=headers)
    print("Response: ", response.status_code)

    with open('brow5.html', 'w') as f:
        f.write(response.text)

    if not response.ok:
        raise ValueError(f'Cannot retrieve the page {url}, response: {response}')

    return response.text


def l_card_to_dict(l_card: BeautifulSoup) -> dict:
    """"""

    # href to the product
    a_tag = l_card.find('a')
    href = a_tag.get('href', None)

    product_url = ''
    if href:
        product_url = f'https://olx.pl{href}'

    # image
    image = l_card.find('img')
    image_src = image.get('src', None)

    # price and name
    price_tag = l_card.find('p', {'data-testid': 'ad-price'})
    price = price_tag.getText()
    name = l_card.find('h6').getText()

    list_divs = l_card.find_all('div', {'type': 'list'})

    # article body
    main_div = next(div for div in list_divs if len(div) == 4)

    # state
    state_span = main_div.select('div > span')[0]
    state = state_span.getText()

    # get location
    location_tag = l_card.find('p', {'data-testid': 'location-date'})
    location = location_tag.getText()

    return {
        'price': price,
        'name': name,
        'state': state,
        'location': location,
        'image_src': image_src,
        'product_url': product_url,
    }


def fix_all_thumbnails(products: list[dict]) -> list[dict]:
    """"""

    for product in [products[-1], products[-2]]:
        if 'no_thumbnail' in product['image_src']:
            # go to the src
            print('Product: ', product['product_url'])
            html = retrieve_page(url=product['product_url'], referer=None)

            # extract image from .swiper-zoom-container > img
            soup = BeautifulSoup(html, "html.parser")
            swiper_div = soup.find('div', {'class': 'swiper-zoom-container'})
            print("swiper_div: ", swiper_div)
            return
            image = swiper_div.find('img')
            image_src = image.get('src')
            print("image_src: ", image_src)

            *url_parts, _ = image_src.split('/')
            image_base = '/'.join(url_parts)
            updated_image_url = f'{image_base}/image;s=200x0;q=50'
            print('updated_url: ', updated_image_url)
            # set new query params /image;s=200x0;q=50

    return products

# https://ireland.apollo.olxcdn.com/v1/files/u07537y6vyfd2-PL/image;s=200x0;q=50
# /app/static/media/no_thumbnail.15f456ec5.svg


def parse_olx(url: str) -> list[dict]:
    """"""

    html = retrieve_page(url=url, referer=None)
    soup = BeautifulSoup(html, "html.parser")

    # 'data-cy' can be used also
    l_cards = soup.find_all('div', {'data-testid': 'l-card'})

    cards_dicts = [l_card_to_dict(l_card) for l_card in l_cards]

    return cards_dicts


if __name__ == "__main__":
    # retrieve_page(url='https://www.olx.pl/moda/zegarki/')
    res = parse_olx(url='https://www.olx.pl/moda/zegarki/')
    print("Res: ", res)
    # fix_all_thumbnails(products=res)
