from flask import url_for
from flask_babel import _

from flucht.data.images import pictures_exhibition


def build_banner():
    img_tag = {}
    for name, value in pictures_exhibition.items():
        img_tag[name] = f'''
        <div class="row vh-100 d-flex align-items-center justify-content-center align-content-center">
                <img 
                    id={name} 
                    data-bs-toggle="modal" 
                    data-bs-target="#{name}Modal" 
                    class="h-75 w-50"
                    src="{url_for('static', filename=value['filepath'])}" 
                    alt="{name}"
                    loading="lazy">
        </div>
        '''

    return img_tag

