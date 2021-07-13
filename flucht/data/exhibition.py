from flask import url_for
from flask_babel import _


def build_img_tag():
    img_tag = {}
    for name, value in pictures_exhibition.items():
        img_tag[name] = f'''
            <figure>
                <img id={name} data-bs-toggle="modal" data-bs-target="#{name}Modal" class="img-thumbnail"
                     src="{url_for('static', filename=value['filepath'])}" alt="{value['text']}">
            </figure>
            <div class="modal fade" id="{name}Modal" tabindex="-1" aria-labelledby="{name}Modal"
                 aria-hidden="true">
                <div class="modal-dialog modal-xl modal-dialog-centered">
                    <div class="modal-content">
                        <div class="modal-body">
                            <div class="img_container">
                                <img id={name} class="modal-image" src="{url_for('static',
                                filename=value['filepath'])}" alt="{_(value['text'])}">
                            </div>
                        </div>
                        <div class="modal-footer justify-content-between">
                                <div class="col-10">
                                    <p class="pic-source"><a href="{value['url']}">{value['url']}</a>
                                        ({value['licensing']})
                                    </p>
                                    <figcaption>{_(value['text'])}</figcaption>
                                </div>
                                <div class="col-1">
                                    <button type="button" class="btn btn-secondary justify-content-end"
                                            data-bs-dismiss="modal">Close
                                    </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div> 
            '''
    return img_tag


citations = {
    'pfarrchronik_oberhollabrunn_1916': 'Pfarrchronik Oberhollabrunn, 1916',
    'wochenzeitung24031916': 'Wochen-Zeitung für das Viertel unter dem Manhartsberg, 24. März 1916',
    'eggenburger_zeitung29091916': 'Eggenburger Zeitung, 29. September 1916',
    'eggenburger_zeitung17111916': 'Eggenburger Zeitung, 17. November 1916',
    'allgemeiner_tiroler18071917': 'Allgemeiner Tiroler Anzeiger, 18. Juli 1917',
    'kremser_zeitung05021916': 'Kremser Zeitung, 5. Februar 1916',
    'pfarrchronik_oberhollabrunn1917': 'Pfarrchronik Oberhollabrunn, 1917',
    'wochenzeitung24051918': 'Wochen-Zeitung für das Viertel unter dem Manhartsberg, 24. Mai 1918'}

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