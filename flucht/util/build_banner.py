from flask import url_for
from flask_babel import _

from flucht.data.images import pictures_exhibition


def build_banner():
    img_tag = {}
    for name, value in pictures_exhibition.items():
        img_tag[name] = f'''
        <div class="row h-100 w-100 d-flex align-items-center justify-content-center align-content-center">
                <img 
                    id={name} 
                    data-bs-toggle="modal" 
                    data-bs-target="#{name}BannerModal" 
                    class="h-75 w-75"
                    style="cursor: pointer;"
                    src="{url_for('static', filename=value['filepath'])}" 
                    alt="{name}"
                    loading="lazy">
        </div>
        '''
    return img_tag


def build_modal_banner():
    img_tag = {}
    for name, value in pictures_exhibition.items():
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
                    id="{name}BannerModal"
                    tabindex="-1" aria-labelledby="{name}BannerModal"
                     aria-hidden="true">
                    <div class="modal-dialog  modal-dialog-centered modal-xl">
                        <div class="modal-content">
                        {modal_footer}
                        </div>
                    </div>
                </div> 
            </div> 
            '''
    return img_tag
