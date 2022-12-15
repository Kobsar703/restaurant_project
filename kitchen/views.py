from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen.forms import CookCreationForm, DishForm, DishSearchForm, CookSearchForm
from kitchen.models import DishType, Ingredient, Dish, Cook


def index(request):
    return render(request, "home.html")


class DishTypeList(LoginRequiredMixin, generic.ListView):
    model = DishType
    context_object_name = "dish_type_list"
    template_name = "kitchen/dish_type_list.html"
    paginate_by = 4


class DishTypeCreate(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    template_name = "kitchen/dish_type_form.html"
    success_url = reverse_lazy("kitchen:dish-types-list")


class DishTypeUpdate(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = "__all__"
    template_name = "kitchen/dish_type_form.html"
    success_url = reverse_lazy("kitchen:dish-types-list")


class DishTypeDelete(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    template_name = "kitchen/dish_type_confirm_delete.html"
    success_url = reverse_lazy("kitchen:dish-types-list")


class IngredientList(LoginRequiredMixin, generic.ListView):
    model = Ingredient
    paginate_by = 4


class IngredientCreate(LoginRequiredMixin, generic.CreateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("kitchen:ingredients-list")


class IngredientUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("kitchen:ingredients-list")


class IngredientDelete(LoginRequiredMixin, generic.DeleteView):
    model = Ingredient
    success_url = reverse_lazy("kitchen:ingredients-list")


class DishList(generic.ListView):
    model = Dish
    paginate_by = 4
    queryset = Dish.objects.all().select_related("dish_type")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DishList, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")
        context["search_form"] = DishSearchForm(
            initial={
                "name": name
            }
        )
        return context

    def get_queryset(self):
        form = DishSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )


class DishDetail(LoginRequiredMixin, generic.DetailView):
    model = Dish
    queryset = Dish.objects.all().select_related("dish_type").prefetch_related("ingredients")


class DishCreate(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen:dish-list")


class DishUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishForm
    success_url = reverse_lazy("kitchen:dish-list")


class DishDelete(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")


class CookList(generic.ListView):
    model = Cook
    paginate_by = 4
    queryset = get_user_model().objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CookList, self).get_context_data(**kwargs)

        last_name = self.request.GET.get("last_name_cook", "")
        context["search_form"] = CookSearchForm(
            initial={
                "last_name_cook": last_name
            }
        )
        return context

    def get_queryset(self):
        form = CookSearchForm(self.request.GET)

        if form.is_valid():
            return self.queryset.filter(
                last_name__icontains=form.cleaned_data["last_name_cook"]
            )


class CookCreate(generic.CreateView):
    model = Cook
    form_class = CookCreationForm
    success_url = reverse_lazy("kitchen:cook-list")


class CookDetail(generic.DetailView):
    model = Cook
    queryset = Cook.objects.all().prefetch_related("dishes__dish_type")


class CookDelete(generic.DeleteView):
    model = Cook
    success_url = reverse_lazy("kitchen:cook-list")
