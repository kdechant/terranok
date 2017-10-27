from mezzanine.pages.page_processors import processor_for
from mezzanine.blog.models import BlogPost
from projects.models import Project


@processor_for('/')
def add_blog(request, page):
    blog_posts = BlogPost.objects.published()
    prefetch = ("categories", "keywords__keyword")
    blog_posts = blog_posts.prefetch_related(*prefetch).all()

    projects = Project.objects.all()

    return {"blog_posts": blog_posts, "projects": projects}


@processor_for('projects')
def add_projects(request, page):
    projects = Project.objects.all()
    return {"projects": projects}
