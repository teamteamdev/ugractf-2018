from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from notes.models import Note
from django.core.exceptions import ObjectDoesNotExist


def login_page(request):
    if request.user.is_authenticated:
        return get_profile(request)

    class Actions:
        LOGIN = 0
        REGISTER = 1

    error = None

    if request.method == "POST":
        username = request.POST.get("username", "").strip().lower()
        password = request.POST.get("password", "").strip()
        if username == "" or password == "":
            error = "Empty username or password"
        else:
            try:
                User.objects.get(username=username)
                action = Actions.LOGIN
            except ObjectDoesNotExist:
                action = Actions.REGISTER

            if action == Actions.LOGIN:
                user = authenticate(request, username=username, password=password)
                if user is None:
                    error = "Invalid username or password"
                else:
                    login(request, user)
                    return get_profile(request)
            else:
                # TODO: fix registration
                user = User(username=username)
                user.set_password(password)
                user.save()
                login(request, user)
                return get_profile(request)

    return render(request, "login.html", {"error": error})


@login_required(login_url="/login/")
def get_profile(request):
    return redirect("/profile/{}/".format(request.user.id))


@login_required(login_url="/login/")
def profile_page(request, user_id):
    user = get_object_or_404(User, id=user_id)

    context = {"profile": user}

    if user == request.user:
        context["own"] = True
        context["notes"] = user.note_set.all()
        context["title"] = "My profile"
        context["active"] = "profile"
    else:
        context["own"] = False
        context["title"] = "User {}".format(user.username)

    return render(request, "profile.html", context)


@login_required(login_url="/login/")
def change_password(request, user_id):
    user = get_object_or_404(User, id=user_id)

    error = ""

    if request.method == "POST":
        password = request.POST.get("password", "").strip()
        if user.is_superuser:
            error = "Superuser password cannot be changed"
        elif password == "":
            error = "Empty password"
        else:
            user.set_password(password)
            user.save()

            logout(request)

            return render(request, "changed.html", {
                "title": "Settings",
                "active": "settings"
            })

    return render(request, "change_password.html", {
        "error": error,
        "title": "Settings",
        "active": "settings"
    })


@login_required(login_url="/login/")
def edit_note(request, note_id=None):
    context = {}

    note = None
    if note_id is not None:
        note = get_object_or_404(Note, id=note_id)
        context["title"] = "{} · Editing".format(note.title)

        if note.owner != request.user:
            return get_profile(request)
    else:
        context["title"] = "New note"
        context["active"] = "edit"

    context["note"] = note or {}

    if request.method == "POST":
        try:
            title = request.POST["title"]
            description = request.POST["description"]

            if note is None:
                note = Note(title=title, description=description, owner=request.user)
                note.save()

                return get_profile(request)
            else:
                note.title = title
                note.description = description
                note.save()

                return redirect("/note/{}/".format(note_id))
        except KeyError:
            context["error"] = "Fill in all the fields"

    return render(request, "edit_note.html", context)


@login_required(login_url="/login/")
def read_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)

    if note.owner != request.user:
        return get_profile(request)

    return render(request, "note.html", {
        "note": note,
        "title": note.title
    })


def logout_page(request):
    logout(request)
    return redirect("/login/")
