from django.views.generic import CreateView
from .forms import CreateUserForm
# D:\Movies\bootproj\everycheese\todoenv\Scripts\activate
from django.urls import reverse_lazy


class SignUp(CreateView):
    form_class = CreateUserForm
    success_url = reverse_lazy("home")
    template_name = "signup.html"
