# from django.shortcuts import render
from django.shortcuts import redirect
from meal_plans.models import MealPlan
from django.urls import reverse_lazy

from django.views.generic.list import ListView

from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# , DeleteView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin


class MealPlanListView(LoginRequiredMixin, ListView):
    model = MealPlan
    template_name = "meal_plans/list.html"
    context_object_name = "meal_plans_list"
    paginate_by = 2


class MealPlanCreateView(LoginRequiredMixin, CreateView):
    model = MealPlan
    template_name = "meal_plans/new.html"
    fields = ["name", "date", "recipes"]
    success_url = reverse_lazy("meal_plan_detail")
    # don't know if above is right. may need to redirect

    def form_valid(self, form):
        # Save the meal plan, but don't put it in the database
        plan = form.save(commit=False)
        # Assign the owner to the meal plan
        plan.owner = self.request.user
        # Now, save it to the database
        plan.save()
        # Save all of the many-to-many relationships
        form.save_m2m()
        # Redirect to the detail page for the meal plan
        return redirect("meal_plan_detail", pk=plan.id)

    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)


class MealPlanDetailView(LoginRequiredMixin, DetailView):
    model = MealPlan
    template_name = "meal_plans/detail.html"
    fields = ["name", "date", "recipes"]

    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)


class MealPlanUpdateView(LoginRequiredMixin, UpdateView):
    model = MealPlan
    template_name = "meal_plans/edit.html"
    success_url = reverse_lazy("meal_plans_list")


class MealPlanDeleteView(LoginRequiredMixin, DeleteView):
    model = MealPlan
    template_name = "meal_plans/delete.html"
    success_url = reverse_lazy("meal_plans_list")
