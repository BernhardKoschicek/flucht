from flask import url_for
from flask_babel import _

from flucht.data.newspaper import newspapers


def build_newspaper_tag():
    news_tag = {}
    for name, value in newspapers.items():
        teaser = (value['teaser'][:100] + '...') if len(
            value['teaser']) > 100 else value['teaser']
        news_tag[name] = f'''
        <div class="col-8" xmlns="http://www.w3.org/1999/html">
            <button class="border border-warning bg-warning rounded shadow-longer" 
                    data-bs-toggle="modal" 
                    data-bs-target="#{name}Modal">
                <div class="row">
                    <div class="col">
                     <blockquote>
                            <p class="source-text">                 
                                {teaser}
                            </p>
                        <figcaption class="blockquote-footer blockquote-footer-teaser ">
                                <cite title="{value['citation']}">
                                {value['citation']}
                                </cite>
                          
             
                        </figcaption>   
                      </div>
                      <div class="col-3">
                            <img src="../static/images/exhibition/news_person.png" 
                            class="img-fluid" alt="newspict" loading="lazy">
                      </div>

                </div>
            </button>
        </div>
            '''
    return news_tag


def build_modal_newspaper():
    news_tag = {}
    for name, value in newspapers.items():
        image_path = f"images/exhibition/newspaper/{value['filename']}"

        newspaper_image = f'''
            <div class="w-auto">
                <img src="{url_for('static', filename=image_path)}"
                    alt="{name}" loading="lazy" class="img-fluid">
            </div>
        '''

        page = f', {_("page")} {value["page"]}'

        modal_header = f'''
      <div class="modal-header">
        <h5 class="modal-title" id="{name}Modal">
            {value['citation']}
            {page if value["page"] else value["page"]}</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
        '''

        modal_body = f'''
              <div class="modal-body px-5">
              <div class="row justify-content-center">
                 <div class="col-6">
                    <h4 class="newspaper-header">{value['title']}</h4>
                    <blockquote class="newspaper-blockquote">
                        <p>                 
                           {value['content']}
                        </p>
                    </blockquote>
                </div>             
              </div>

                <div class="w-auto">
                    {newspaper_image if value['filename'] else ''}
                </div>
              </div>
            '''

        source_link = f'''
            <a href="{value['url']}" target="_blank">
                {value['source']}
               </a>
        '''

        modal_footer = f'''
           <div class="modal-footer modal-footer-image justify-content-between">
                <div class="col-10">
                    <p class="pic-source">
                     {source_link if value['url'] else value['source']}
                   </p>
                   <p class="fst-italic">Buchstabengetreu transkribiert, Orthographie und Zeichensetzung des Originals übernommen.</p>
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

        news_tag[name] = f'''
        <div class="col">
            <div class="modal fade" 
                id="{name}Modal"
                tabindex="-1" aria-labelledby="{name}Modal"
                 aria-hidden="true">
                <div class="modal-dialog modal-dialog-centered modal-xl modal-dialog-scrollable">
                    <div class="modal-content">
                    {modal_header}
                    {modal_body}
                    {modal_footer}
                    </div>
                </div>
            </div> 
        </div> 
            '''

    return news_tag
