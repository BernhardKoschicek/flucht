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
                        <figcaption class="blockquote-footer">
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

        modal_header= f'''
      <div class="modal-header">
        <h5 class="modal-title" id="{name}Modal">{value['title']}</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
        '''
        modal_body =  f'''
              <div class="modal-body">
                <p>{value['content']}</p>
                <p>{value['citation']}</p>
                <p>{value['url']}</p>
              </div>
            '''

        modal_footer = f'''
          <div class="modal-footer justify-content-center">
            <button type="button" class="btn btn-secondary " data-bs-dismiss="modal">Close</button>
          </div>
        '''

        news_tag[name] = f'''
            {figure}
            <div class="modal fade" 
                id="{name}Modal"
                tabindex="-1" aria-labelledby="{name}Modal"
                 aria-hidden="true">
                <div class="modal-dialog modal-xl modal-dialog-centered">
                    <div class="modal-content">
                    {modal_header}
                    {modal_body}
                    {modal_footer}
                    </div>
                </div>
            </div> 
            '''

    return news_tag
