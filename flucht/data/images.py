from flask import url_for
from flask_babel import _




def build_img_tag():
    img_tag = {}
    for name, value in pictures_exhibition.items():
        img_tag[name] = f'''
            <figure>
            <img class="img-thumbnail" src="{url_for("static", filename=value["filepath"])}" alt="{_(value['text'])}">
            <footer class="pic-source"><a href="{value['url']}">{value['url']}</a> ({value['licensing']})</footer>
            <figcaption>{_(value['text'])}</figcaption>
            </figure>
            '''
    return img_tag


licensing = {'public_domain': 'Public Domain'}

pictures_exhibition = {
    'kundmachung19071915': {
        'filepath': 'images/exhibition/kundmachung19071915.jpg',
        'text': 'kundmachung19071915',
        'url': 'https://digital.onb.ac.at/rep/access/preview/BAG_14257396',
        'licensing': licensing['public_domain']
    },
    'kuk_maschinengewehr': {
        'filepath': 'images/exhibition/1024px-01915_Maschinengewehr_Abteilung_Lawoczne.jpg',
        'text': 'maschinengewher_lawoczne',
        'url': 'https://commons.wikimedia.org/wiki/File:01915_Maschinengewehr_Abteilung,_Lawoczne.jpg',
        'licensing': licensing['public_domain']
    },
    'kundmachung20051916': {
        'filepath': 'images/exhibition/kundmachung20051916.jpg',
        'text': 'kundmachung20051916',
        'url': 'https://digital.onb.ac.at/rep/access/preview/BAG_14258692',
        'licensing': licensing['public_domain']
    },
    'kriegsschaeden1917': {
        'filepath': 'images/exhibition/kriegsschaeden1917.jpg',
        'text': 'kriegsschaeden1917',
        'url': 'https://digital.onb.ac.at/rep/access/preview/BAG_15568812',
        'licensing': licensing['public_domain']
    },
    'ansicht_oberhollabrunn1910': {
        'filepath': 'images/exhibition/ansicht_oberhollabrunn1910.jpg',
        'text': 'ansicht_oberhollabrunn1910',
        'url': 'https://akon.onb.ac.at/#id=AKON_AK063_199',
        'licensing': licensing['public_domain']
    },
    'lagertor': {
        'filepath': 'images/exhibition/lagertor.jpg',
        'text': 'lagertor',
        'url': '',
        'licensing': ''
    },
    'lagertor_oberhollabrunn1916': {
        'filepath': 'images/exhibition/lagertor_oberhollabrunn1916.jpg',
        'text': 'lagertor_oberhollabrunn1916',
        'url': 'https://upload.wikimedia.org/wikipedia/de/e/e3/Stockerau_Fl%C3%BCchtlingslager.jpg',
        'licensing': licensing['public_domain']
    }

}
