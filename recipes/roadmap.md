

1. Create django app called meal plans
2. Create a MealPlanModel
    - We have a breakdown of th 4 pieces of data
3. Create our 5 paths
4. Create ListView
    - Only show meal plans that were created by the user
    - Add a link to the createview
    - Each meal plan should be a link to its detail view
5. Create CreateView
    - This view will show a form that allows the user to enter a name, a date, and select the recipes they want to put in this meal plan
    - Whem the user sabves the meal plan, their user object should be automatically saved to the owner property of the meal plan
    - The user should be redirected to the detail page for the newly-created meal plan
    - There is also an extra piece of code...
6. Detail View