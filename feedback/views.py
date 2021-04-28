from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from feedback.forms import FeedbackForm


class FeedbackView(TemplateView):
    template_name = 'feedback.html'

    def get_context_data(self, **kwargs):
        context = super(FeedbackView, self).get_context_data()
        context['form'] = FeedbackForm()
        return context

    def post(self, request):
        context = {}
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            context['data'] = form.cleaned_data
            value = form.cleaned_data['gender']
            if value == 1:
                context['data']['gender'] = 'Мужской'
            else:
                context['data']['gender'] = 'Женский'
            value = form.cleaned_data['service']
            if value == 1:
                context['data']['service'] = "Покупка квартиры"
            elif value == 2:
                context['data']['service'] = "Работа персонала"
            elif value == 3:
                context['data']['service'] = "Использование сайта"
            elif value == 4:
                context['data']['service'] = "Прочее"
        return render(request, "feedback.html", context)
