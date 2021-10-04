from flask_babel import _

from flucht.data.newspaper import newspapers


def build_newspaper_tag():
    news_tag = {}
    for name, value in newspapers.items():
        news_tag[name] = f'''
            <figure>
                <blockquote class="blockquote">
                    <p class="source-text">
                        <b>{value['title']}<b>
                        <br>
                        {_(name)}
                    </p>
                </blockquote>
                <figcaption class="blockquote-footer">
                    <cite title="{value['citation']}">
                        {value['citation']}
                    </cite>
                </figcaption>
            </figure>
            '''
    return news_tag
