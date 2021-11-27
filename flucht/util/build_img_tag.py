from flask import url_for
from flask_babel import _

from flucht.data.images import pictures_exhibition


def build_img_tag():
    img_tag = {}
    for name, value in pictures_exhibition.items():
        img_tag[name] = f'''
 
        <div class="col-10 py-3 mx-auto h-auto">
        <span class="img-button">
                <img 
                    id={name} 
                    data-bs-toggle="modal" 
                    data-bs-target="#{name}Modal" 
                    class="img-thumbnail shadow-longer"
                    src="{url_for('static', filename=value['filepath'])}" 
                    alt="{name}"
                    loading="lazy">
        </button>

        </div>
        '''

    return img_tag


def build_modal_img():
    img_tag = {}
    for name, value in pictures_exhibition.items():
        modal_body = f'''
            <div class="modal-body-image">
                <div class="img_container">
                    <img 
                        class="modal-image"
                        src="{url_for(
            'static',
            filename=value['filepath'])}"
                        alt="{_(name)}">
                </div>
            </div>
        '''
        modal_footer = f'''
            <div class="modal-footer modal-footer-image justify-content-between">
                    <div class="col-10">
                        <p class="pic-source">
                            <a 
                                href="{value['url']}"
                                 target="_blank">
                                {value['source']}         
                            </a>
                            {value['licensing']}
                        </p>
                        <figcaption>
                            {_(name)}
                        </figcaption>
                    </div>
                    <div class="col-1">
                        <button 
                            type="button" 
                            class="btn btn-secondary 
                                justify-content-end"
                            data-bs-dismiss="modal">
                                Close
                        </button>
                </div>
            </div>        
        '''
        img_tag[name] = f'''
        <div class="col">
            <div class="modal fade" 
                id="{name}Modal"
                tabindex="-1" aria-labelledby="{name}Modal"
                 aria-hidden="true">
                <div class="modal-dialog  modal-dialog-centered modal-xl">
                    <div class="modal-content">
                    {modal_body}
                    {modal_footer}
                    </div>
                </div>
            </div> 
        </div> 
            '''
    return img_tag
