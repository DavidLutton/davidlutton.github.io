from datetime import datetime
from email.utils import format_datetime, formatdate  # for RFC2822 formatting
from pathlib import Path
from pprint import pprint

# import commonmark
import jinja2
import yaml
from markdown_it import MarkdownIt
from markdown_it.extensions.amsmath import amsmath_plugin
# from markdown_it.extensions.dollarmath.index import dollarmath_plugin
from markdown_it.extensions.footnote import footnote_plugin
from markdown_it.extensions.front_matter import front_matter_plugin
# from markdown_it.extensions.texmath.index import texmath_plugin


class Site:
    
    def __enter__(self):
        self.posts = []
        return self
    
    def post(self, front_matter, url):
        post_date = datetime.strptime(
            front_matter['blog_publish_date'], '%Y/%m/%d'
        )
        
        self.posts.append(
            dict(**front_matter, 
                 date=post_date, 
                 rfc2822_date=format_datetime(post_date), 
                 link=f"{BASE_URL}{url}",
                 rellink=f"{url}"),
        )
    
    def __exit__(self, a, b, c):
        self.posts.sort(key=lambda item: item['date'], reverse=True)
        # Make the RSS feed
        Path(folder / 'rss.xml').write_text(
            env.get_template(FEED_TEMPLATE_FILE).render(
                posts=self.posts, date=formatdate()
            )
        )
        INDEX_TEMPLATE_FILE = "_template/index_template.html"

        Path(folder / 'index.html').write_text(
            env.get_template(INDEX_TEMPLATE_FILE).render(
                posts=self.posts, date=formatdate()
            )
        )
    


md = (
    MarkdownIt()
    .use(front_matter_plugin)
    .use(footnote_plugin)
    .use(amsmath_plugin)
    # .use(texmath_plugin)
    # .use(dollarmath_plugin)
    .enable('table')
)


folder = Path()
TEMPLATE_FILE = "_template/post_template.html"
FEED_TEMPLATE_FILE = "_template/rss_feed_template.xml"
BASE_URL = "https://www.dalun.space/"

templateLoader = jinja2.FileSystemLoader(searchpath='.')
env = jinja2.Environment(loader=templateLoader, autoescape=False)

if __name__ == '__main__':
    for post in Path('post/').glob('*.html'):
         post.unlink()

    with Site() as site:
        for post in (folder / '_post').glob('*.md'):
            print(f'Rendering {post.stem}')
            url = f'post/{post.stem}.html'

            text = post.read_text()
            html_text = md.render(text)

            tokens = md.parse(text)
            front_matter = yaml.load(tokens[0].content, Loader=yaml.SafeLoader)

            output = env.get_template(TEMPLATE_FILE).render(
                content=html_text, baseurl=BASE_URL, url=url, **front_matter
            )
            site.post(front_matter, url)
            Path(folder / url).write_text(output)

