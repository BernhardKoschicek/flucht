from flask import url_for
from flask_babel import _

from flucht.data.newspaper import newspapers


def build_newspaper_tag():
    news_tag = {}
    for name, value in newspapers.items():
        teaser = (value['teaser'][:100] + '...') if len(
            value['teaser']) > 100 else value['teaser']
        figure = f'''
        <button class="border border-warning rounded px-3 pt-2 bg-kaisergelb" 
                data-bs-toggle="modal" 
                data-bs-target="#{name}Modal">
            <figure class="newspaper">
                <p class="source-header">{value['title']}<p>
                <div class="row">
                    <div class="col-9">
                        <blockquote>
                            <p class="source-text">                 
                                {teaser}
                            </p>
                        </blockquote>
                        <figcaption class="blockquote-footer blockquote-footer-teaser">
                            <cite title="{value['citation']}">
                                {value['citation']}
                            </cite>
                        </figcaption>
                    </div>
                    <div class="col-3">
                        <img src="../static/images/exhibition/news_person.png" class="img-fluid">
                    </div>
                 </div>
            </figure>
        </button>
            '''

        newspaper_image = f'''
            <div class="d-flex justify-content-between">
                <img src="{url_for('static', filename=value['image_path'])}"
                    alt="{name}">
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
                <h4 class="newspaper-header">{value['title']}</h4>
                <blockquote class="newspaper-blockquote">
                    <p>                 
                       {value['content']}
                    </p>
                </blockquote>
                {newspaper_image if value['image_path'] else ''}
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
            {figure}
            <div class="modal fade" 
                id="{name}Modal"
                tabindex="-1" aria-labelledby="{name}Modal"
                 aria-hidden="true">
                <div class="modal-dialog modal-dialog-centered modal-lg">
                    <div class="modal-content">
                    {modal_header}
                    {modal_body}
                    {modal_footer}
                    </div>
                </div>
            </div> 
            '''

    return news_tag
