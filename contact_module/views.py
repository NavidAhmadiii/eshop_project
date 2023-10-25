from django.views.generic.edit import CreateView
from site_module.models import SiteSetting
from .forms import ContactUsModelForm


# Create your views here.

# class base view
class ContactUsView(CreateView):
    #  address template render in html page
    template_name = 'contact_module/contact_us_page.html'
    # owen form
    form_class = ContactUsModelForm
    # redirection system
    success_url = '/contact-us/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        context['site_setting'] = setting
        return context
