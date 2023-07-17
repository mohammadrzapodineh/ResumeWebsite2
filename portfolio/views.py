from .serializers import PortfolioSerializer
from django.shortcuts import render, get_object_or_404
from .models import Portfolio, Category, ImageGallery
from django.views.generic import ListView, DetailView
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework import status
from rest_framework.response import Response


class PortfolioList(ListView):
    template_name = 'portfolio/portfolio_list.html'
    model = Portfolio
    context_object_name = 'portfolios'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class PortfolioDetail(DetailView):
    template_name = 'portfolio/portfolio_detail.html'
    model = Portfolio
    slug_url_kwarg = 'portfolio_slug'
    context_object_name = 'portfolio'
    

@api_view(['GET'])
@renderer_classes([JSONRenderer, TemplateHTMLRenderer])
def get_portfolios_by_category(request, category_id, format=None):
    '''
    This Api Can Get Portfolios By Category For Use In Portfolio List Page
    Return -> JsonResponse And TemplateResponse
    '''
    category = get_object_or_404(Category, pk=category_id)
    portfolios = category.portfolio.all()
    
    if request.accepted_renderer.format == 'html':
        context = {
            'portfolios': portfolios
        }
        return Response(context, template_name='components/portfolio/portfolio_list_component.html')
    serializer = PortfolioSerializer(portfolios, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    
    