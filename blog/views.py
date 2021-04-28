from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, DetailView

from blog.models import Publication, Comment


class BaseView(TemplateView):
    pass


class PostList(ListView):
    template_name = 'article_list.html'
    model = Publication


class PostDetail(DetailView):
    template_name = 'article_detail.html'
    model = Publication

    def post(self, request, slug):
        comment = Comment()
        comment.user = request.user
        comment.publication = self.get_object()
        comment.text = request.POST.get("text")
        comment.save()
        return redirect(f"/blog/{self.get_object().slug}/")