from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .models import Product, Review
from .forms import ReviewForm


class ProductsList(ListView):
    model = Product
    context_object_name = 'product_list'


class ProductView(DetailView):
    model = Product
    form_class = ReviewForm

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        product = context['product']
        context['reviews'] = Review.objects.filter(product=product)
        context['is_review_exist'] = False
        if 'reviewed_products' in self.request.session:
            if product.id in self.request.session['reviewed_products']:
                context['is_review_exist'] = True
        if not context['is_review_exist']:
            context['form'] = self.form_class
        return context

    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        text = request.POST['text']
        product_id = kwargs['pk']
        product = Product.objects.get(id=product_id)
        if form.is_valid():
            Review.objects.create(text=text, product=product)
        request.session.modified = True
        if 'reviewed_products' in request.session:
            request.session['reviewed_products'].append(product_id)
        else:
            request.session['reviewed_products'] = []
        return redirect('product_detail', pk=product_id)

