from mezzanine.pages.page_processors import processor_for
from mezzanine.blog.models import BlogPost

@processor_for('/')
def add_blog(request, page):
    blog_posts = BlogPost.objects.published()
    prefetch = ("categories", "keywords__keyword")
    blog_posts = blog_posts.select_related("user").prefetch_related(*prefetch).all()
    return {"blog_posts": blog_posts}
