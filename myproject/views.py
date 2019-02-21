from django.shortcuts import redirect


def logged_out_redirect(request):
    return redirect('/forecast/logout')
