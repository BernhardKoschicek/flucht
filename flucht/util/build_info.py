from flucht.data.info import info


def build_info_btn():
    news_tag = {}
    for name, value in info.items():
        news_tag[name] = f'''
        <div class="col-8 mx-auto py-3" xmlns="http://www.w3.org/1999/html">
            <button class="border  border-warning bg-warning rounded shadow-longer" 
                    data-bs-toggle="modal" 
                    data-bs-target="#{name}Modal">
                     <div class="row ">
                        <div class="col-9 ">
                            <h4>{value['title']}</h4>
                        </div>
                        <div class="col-2">
                                 <img src="../static/images/exhibition/info.png" 
                                     class="img-fluid" alt="newspict" loading="lazy">   
                        </div>
                    </div>
            </button>
        </div>

            '''
    return news_tag


def build_modal_info():
    news_tag = {}
    for name, value in info.items():
        modal_header = f'''
      <div class="modal-header">
        <h5 class="modal-title" id="{name}Modal">
           <h4 class="newspaper-header">{value['title']}</h4>
        </h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
        '''

        modal_body = f'''
              <div class="modal-body px-5">
              <div class="row justify-content-center">
                 <div class="col-6">
                   
                    <blockquote class="newspaper-blockquote">
                        <p>                 
                           {value['text']}
                        </p>
                    </blockquote>
                </div>             
              </div>

                
              </div>
            '''

        modal_footer = f'''
           <div class="modal-footer modal-footer-image justify-content-between">
                <div class="col-10">

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
