# from django.shortcuts import render
from meal_plans.models import MealPlan

from django.views.generic.list import ListView

# from django.views.generic.detail import DetailView
# from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin


class MealPlanListView(LoginRequiredMixin, ListView):
    model = MealPlan
    template_name = "meal_plans/list.html"
    paginate_by = 7

    # def get(self, request):
    #     return self.render_to_response({})


# class MealPlanDetailView(DetailView):
#     model = MealPlan
#     template_name = "meal_plans/detail.html"
