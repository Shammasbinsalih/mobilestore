from django.shortcuts import render
from django.views.generic import View,TemplateView,CreateView
from store.models import Products
from django.urls import reverse_lazy
from store.forms import ProductForm


# Create your views here.
class CustHome(TemplateView):
    template_name="custhome.html"
    success_url=reverse_lazy("ch")
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=Products

class ProductView(TemplateView):
    template_name='product.html'
    def get_context_data(self, **kwargs):
        id=kwargs.get('pk')
        context=super().get_context_data(**kwargs)
        context["data"]=Products.objects.get(id=id)
        # context["form"]=ReviewForm()
        # context['review']=Review.objects.all()
        # context['pst']=Purchase.objects.filter(user=self.request.user)
        # context["cdata"]=Cart.objects.filter(user=self.request.user)
        return context

