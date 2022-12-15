from django.urls import path

from kitchen.views import (index, DishTypeList,
                           IngredientList, DishList,
                           CookList, IngredientCreate,
                           IngredientUpdate, IngredientDelete,
                           DishTypeCreate, DishTypeUpdate,
                           DishTypeDelete, CookCreate, CookDetail, CookDelete, DishDetail, DishCreate, DishUpdate,
                           DishDelete, toggle_assign_to_dish)


urlpatterns = [
    path("", index, name="index"),
    path("dish_types/",
         DishTypeList.as_view(),
         name="dish-types-list"),
    path("dish_types/create/",
         DishTypeCreate.as_view(),
         name="dish-types-create"),
    path("dish_types/<int:pk>/update/",
         DishTypeUpdate.as_view(),
         name="dish-types-update"),
    path("dish_types/<int:pk>/delete/",
         DishTypeDelete.as_view(),
         name="dish-types-delete"),
    path("ingredients/",
         IngredientList.as_view(),
         name="ingredients-list"),
    path("ingredients/create/",
         IngredientCreate.as_view(),
         name="ingredients-create"
         ),
    path("ingredients/<int:pk>/update",
         IngredientUpdate.as_view(),
         name="ingredients-update"
         ),
    path("ingredients/<int:pk>/delete/",
         IngredientDelete.as_view(),
         name="ingredients-delete"
         ),
    path("dishes/",
         DishList.as_view(),
         name="dish-list"),
    path("dishes/<int:pk>/detail/",
         DishDetail.as_view(),
         name="dish-detail"),
    path(
        "dishes/<int:pk>/assign/",
        toggle_assign_to_dish,
        name="dish-assign",
    ),
    path("dishes/create/",
         DishCreate.as_view(),
         name="dish-create"),
    path("dishes/<int:pk>/update",
         DishUpdate.as_view(),
         name="dish-update"),
    path("dishes/<int:pk>/delete",
         DishDelete.as_view(),
         name="dish-delete"),
    path("cooks/",
         CookList.as_view(),
         name="cook-list"),
    path("cooks/create",
         CookCreate.as_view(),
         name="cook-create"),
    path("cooks/<int:pk>/",
         CookDetail.as_view(),
         name="cook-detail"),
    path("cooks/<int:pk>/delete",
         CookDelete.as_view(),
         name="cook-delete"),
               ]

app_name = "kitchen"
