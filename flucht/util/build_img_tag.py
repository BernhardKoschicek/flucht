from flask import url_for
from flask_babel import _

from flucht.data.images import pictures_exhibition


def build_img_tag():
    img_tag = {}
    for name, value in pictures_exhibition.items():
        figure = f'''
            <figure>
                <img 
                    id={name} 
                    data-bs-toggle="modal" 
                    data-bs-target="#{name}Modal" 
                    class="img-thumbnail"
                    src="{url_for('static', filename=value['filepath'])}" 
                    alt="{name}"
                    loading="lazy">
            </figure>
        '''
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
            {figure}
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
            '''
    return img_tag
