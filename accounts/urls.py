from django.urls import path
from django.contrib.auth.views import (
    LoginView, PasswordChangeView,
    PasswordChangeDoneView,

    PasswordResetView,PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)


from .views import (
    user_login,
    logout_view,
    dashboard_view,
    user_register,
    SignUpView,
    edit_user,
    EditUserView,




)
urlpatterns = [
    # path('login/', user_login, name="login"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', logout_view, name="logout"),

    # parolni o'zgartirish
    path("password-change", PasswordChangeView.as_view(), name="password_change"),
    path("password-change-done", PasswordChangeDoneView.as_view(), name="password_change_done"),

    # Parolni tiklash
    path("password-reset/", PasswordResetView.as_view(), name="password_reset"),
    path("password-reset/done/", PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("password-reset/<uidb64>/<token>/", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("password_reset/complete/", PasswordResetCompleteView.as_view(), name="password_reset_complete"),

    path('profile/', dashboard_view, name="user_profile"),
    path('signup/', user_register, name="user_register"),
    # path('profile/edit/', edit_user, name='edit_user_information'),
    # path('signup/', SignUpView.as_view(), name="user_register"),
    path('profile/edit/', EditUserView.as_view(), name='edit_user_information')


]