from django.urls import path, re_path
from .views import PortfolioList, PortfolioDetail, get_portfolios_by_category


app_name = 'portfolio'
urlpatterns = [
    path('', PortfolioList.as_view(), name='portfolio_list'),
    re_path(r'detail/(?P<portfolio_slug>[-\w]+)/', PortfolioDetail.as_view(), name='portfolio_detail'),
    path('get_portfolios_by_categpry/<int:category_id>/', get_portfolios_by_category, name='get_portfolios_by_category_api')
    
]