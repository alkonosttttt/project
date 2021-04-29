from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, DetailView

from blog.forms import PublicationForm
from blog.models import Publication, Comment


class BaseView(TemplateView):
    def get_context_data(self, *args, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        if self.request.user.is_staff:
            context['admin'] = True

        return context


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


class ArticleAddView(BaseView):
    template_name = "add_article.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PublicationForm()

        return context

    def post(self, request):
        print(request.FILES)
        form = PublicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(f"/blog/{form.data.get('slug')}/")

        return redirect('/')