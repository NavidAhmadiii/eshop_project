from site_module.models import SiteSetting, FooterLinkBox, Slider
from product_module.models import Product, ProductCategory
from django.views.generic.base import TemplateView
from utils.convertors import group_list
from django.shortcuts import render
from django.db.models import Count, Sum


class HomeView(TemplateView):
    template_name = 'home_module/index_page.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['sliders'] = Slider.objects.filter(is_active=True)
        sliders = Slider.objects.filter(is_active=True)
        context['sliders'] = sliders
        latest_product = Product.objects.filter(is_active=True, is_delete=False).order_by('-id')[:12]
        most_visited_product = Product.objects.filter(is_active=True, is_delete=False).annotate(
            visit_count=Count('productvisit')).order_by('visit_count')[:12]
        context['latest_product'] = group_list(latest_product)
        context['most_visited_product'] = group_list(most_visited_product)
        categories = list(
            ProductCategory.objects.annotate(products_count=Count('product_categories'))
            .filter(is_active=True, is_delete=False, products_count__gt=0)[:6])
        categories_products = []
        for category in categories:
            item = {
                'id': category.id,
                'title': category.title,
                'products': list(category.product_categories.all()[:4])
            }
            categories_products.append(item)

        context['categories_products'] = categories_products

        context['most_bought_product'] = categories_products
        most_bought_product = Product.objects.filter(orderdetail__order__is_paid=True).annotate(order_count=Sum(
            'orderdetail__count'
        )).order_by('-order_count')[:12]

        context['most_bought_product'] = group_list(most_bought_product)
        return context


def contact_page(request):
    return render(request, 'home_module/contact_page.html')


def site_header_component(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    contex = {
        'site_setting': setting
    }
    return render(request, 'shared/site_header_component.html', contex)


def site_footer_component(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    footer_link_boxes = FooterLinkBox.objects.all()
    for item in footer_link_boxes:
        item.footerlink_set
    context = {
        'site_setting': setting,
        'footer_link_boxes': footer_link_boxes,
    }
    return render(request, 'shared/site_footer_component.html', context)


class AboutView(TemplateView):
    template_name = 'home_module/about_page.html'

    # for: send variable to template side
    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        site_setting = SiteSetting.objects.filter(is_main_setting=True).first()
        context['site_setting'] = site_setting
        return context
