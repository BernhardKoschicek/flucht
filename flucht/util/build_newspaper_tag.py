from flucht.data.newspaper import newspapers


def build_newspaper_tag():
    news_tag = {}
    for name, value in newspapers.items():
        teaser = (value['teaser'][:100] + '...') if len(
            value['teaser']) > 100 else value['teaser']
        news_tag[name] = f'''
        <button class="border border-warning rounded px-3 pt-2 bg-kaisergelb" 
                data-toggle="modal" 
                data-target="#{name}">
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

        news_tag[name] = news_tag[name] + f'''
        <div class="modal fade" id="{name}" 
        tabindex="-1" aria-labelledby="{name}Label" aria-hidden="true">
          <div class="modal-dialog modal-dialog-scrollable">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="{name}Label">Modal title</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                  <span aria-hidden="true">&times;</span>
                </button>
              </div>
              <div class="modal-body">
                ...
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary">Save changes</button>
              </div>
            </div>
          </div>
        </div>
            
            '''
    return news_tag
