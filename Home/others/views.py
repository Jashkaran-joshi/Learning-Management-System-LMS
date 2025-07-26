from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib import messages
from .models import Book, Sport, Hostel, Transport

# Library Section
def add_book(request):
    if request.method == "POST":
        title = request.POST.get('title')
        isbn = request.POST.get('isbn')
        genre = request.POST.get('genre')
        author = request.POST.get('author') 
        publisher = request.POST.get('publisher') 
        publish_date = request.POST.get('publish_date')
        number_of_pages = request.POST.get('number_of_pages')
        number_of_copies = request.POST.get('number_of_copies')
        language = request.POST.get('language')
        description = request.POST.get('description')

        Book.objects.create(
            title=title,
            isbn=isbn,
            genre=genre,
            author=author,
            publisher=publisher,
            publish_date=publish_date,
            number_of_pages=number_of_pages,
            number_of_copies=number_of_copies,
            language=language,
            description=description,
        )

        messages.success(request, "Book added successfully.")
        return redirect("book_list")

    return render(request, "others/library/add-library.html")


def book_list(request):
    books = Book.objects.all()
    return render(request, "others/library/librarys.html", {"books": books})


def edit_book(request, slug):
    book = get_object_or_404(Book, slug=slug)
    if request.method == "POST":
        book.title = request.POST.get('title')
        book.isbn = request.POST.get('isbn')
        book.genre = request.POST.get('genre')
        book.author = request.POST.get('author')
        book.publisher = request.POST.get('publisher')
        book.publish_date = request.POST.get('publish_date')
        book.number_of_pages = request.POST.get('number_of_pages')
        book.number_of_copies = request.POST.get('number_of_copies')
        book.language = request.POST.get('language')
        book.description = request.POST.get('description')

        book.save()
        messages.success(request, "Book updated successfully.")
        return redirect("book_list")

    return render(request, "others/library/edit-library.html", {"book": book})


def view_book(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, "others/library/library-details.html", {"book": book})


def delete_book(request, slug):
    if request.method == "POST":
        book = get_object_or_404(Book, slug=slug)
        book_title = book.title
        book.delete()
        messages.success(request, f"Book '{book_title}' deleted successfully.")
        return redirect("book_list")
    return HttpResponseForbidden()

# Sports Section
def add_sport(request):
    if request.method == "POST":
        name = request.POST.get('name')
        sport_type = request.POST.get('sport_type')
        number_of_players = request.POST.get('number_of_players')
        origin_country = request.POST.get('origin_country')
        equipment_required = request.POST.get('equipment_required')
        rules = request.POST.get('rules')
        governing_body = request.POST.get('governing_body')
        popularity_rank = request.POST.get('popularity_rank')
        olympic_sport = bool(request.POST.get('olympic_sport'))
        description = request.POST.get('description')
        image = request.FILES.get('image')

        Sport.objects.create(
            name=name,
            sport_type=sport_type,
            number_of_players=number_of_players,
            origin_country=origin_country,
            equipment_required=equipment_required,
            rules=rules,
            governing_body=governing_body,
            popularity_rank=popularity_rank or None,
            olympic_sport=olympic_sport,
            description=description,
            image=image
        )

        messages.success(request, "Sport added successfully.")
        return redirect("sport_list")

    return render(request, "others/sports/add-sport.html")


def sport_list(request):
    sports = Sport.objects.all()
    return render(request, "others/sports/sports.html", {"sports": sports})


def edit_sport(request, slug):
    sport = get_object_or_404(Sport, slug=slug)
    if request.method == "POST":
        sport.name = request.POST.get('name')
        sport.sport_type = request.POST.get('sport_type')
        sport.number_of_players = request.POST.get('number_of_players')
        sport.origin_country = request.POST.get('origin_country')
        sport.equipment_required = request.POST.get('equipment_required')
        sport.rules = request.POST.get('rules')
        sport.governing_body = request.POST.get('governing_body')
        sport.popularity_rank = request.POST.get('popularity_rank') or None
        sport.olympic_sport = bool(request.POST.get('olympic_sport'))
        sport.description = request.POST.get('description')

        if request.FILES.get('image'):
            sport.image = request.FILES.get('image')

        sport.save()
        messages.success(request, "Sport updated successfully.")
        return redirect("sport_list")

    return render(request, "others/sports/edit-sport.html", {"sport": sport})


def view_sport(request, slug):
    sport = get_object_or_404(Sport, slug=slug)
    return render(request, "others/sports/sport-details.html", {"sport": sport})


def delete_sport(request, slug):
    if request.method == "POST":
        sport = get_object_or_404(Sport, slug=slug)
        sport_name = sport.name
        sport.delete()
        messages.success(request, f"Sport '{sport_name}' deleted successfully.")
        return redirect("sport_list")
    return HttpResponseForbidden()

# Hostel Section
def add_hostel(request):
    if request.method == "POST":
        name = request.POST.get('name')
        hostel_type = request.POST.get('hostel_type')
        location = request.POST.get('location')
        warden_name = request.POST.get('warden_name')
        contact_number = request.POST.get('contact_number')
        email = request.POST.get('email')
        total_rooms = request.POST.get('total_rooms')
        available_rooms = request.POST.get('available_rooms')
        facilities = request.POST.get('facilities')
        rules = request.POST.get('rules')
        image = request.FILES.get('image')

        Hostel.objects.create(
            name=name,
            hostel_type=hostel_type,
            location=location,
            warden_name=warden_name,
            contact_number=contact_number,
            email=email,
            total_rooms=total_rooms,
            available_rooms=available_rooms,
            facilities=facilities,
            rules=rules,
            image=image
        )

        messages.success(request, "Hostel added successfully.")
        return redirect("hostel_list")

    return render(request, "others/hostels/add-hostel.html")


def hostel_list(request):
    hostels = Hostel.objects.all()
    return render(request, "others/hostels/hostels.html", {"hostels": hostels})


def edit_hostel(request, slug):
    hostel = get_object_or_404(Hostel, slug=slug)
    if request.method == "POST":
        hostel.name = request.POST.get('name')
        hostel.hostel_type = request.POST.get('hostel_type')
        hostel.location = request.POST.get('location')
        hostel.warden_name = request.POST.get('warden_name')
        hostel.contact_number = request.POST.get('contact_number')
        hostel.email = request.POST.get('email')
        hostel.total_rooms = request.POST.get('total_rooms')
        hostel.available_rooms = request.POST.get('available_rooms')
        hostel.facilities = request.POST.get('facilities')
        hostel.rules = request.POST.get('rules')

        if request.FILES.get('image'):
            hostel.image = request.FILES.get('image')

        hostel.save()
        messages.success(request, "Hostel updated successfully.")
        return redirect("hostel_list")

    return render(request, "others/hostels/edit-hostel.html", {"hostel": hostel})


def view_hostel(request, slug):
    hostel = get_object_or_404(Hostel, slug=slug)
    return render(request, "others/hostels/hostel-details.html", {"hostel": hostel})


def delete_hostel(request, slug):
    if request.method == "POST":
        hostel = get_object_or_404(Hostel, slug=slug)
        hostel_name = hostel.name
        hostel.delete()
        messages.success(request, f"Hostel '{hostel_name}' deleted successfully.")
        return redirect("hostel_list")
    return HttpResponseForbidden()

# Transport Pages
def add_transport(request):
    hostels = Hostel.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        transport_type = request.POST.get('transport_type')
        registration_number = request.POST.get('registration_number')
        capacity = request.POST.get('capacity')
        driver_name = request.POST.get('driver_name')
        driver_contact = request.POST.get('driver_contact')
        route_details = request.POST.get('route_details')
        available_timings = request.POST.get('available_timings')
        associated_hostel_id = request.POST.get('associated_hostel')
        image = request.FILES.get('image')

        associated_hostel = get_object_or_404(Hostel, id=associated_hostel_id)

        Transport.objects.create(
            name=name,
            transport_type=transport_type,
            registration_number=registration_number,
            capacity=capacity,
            driver_name=driver_name,
            driver_contact=driver_contact,
            route_details=route_details,
            available_timings=available_timings,
            associated_hostel=associated_hostel,
            image=image
        )

        messages.success(request, "Transport added successfully.")
        return redirect("transport_list")

    return render(request, "others/transport/add-transport.html", {"hostels": hostels})

def transport_list(request):
    transports = Transport.objects.select_related('associated_hostel').all()
    return render(request, "others/transport/transports.html", {"transports": transports})

def edit_transport(request,  registration_number):
    transport = get_object_or_404(Transport,  registration_number= registration_number)
    hostels = Hostel.objects.all()

    if request.method == "POST":
        transport.name = request.POST.get('name')
        transport.transport_type = request.POST.get('transport_type')
        transport.registration_number = request.POST.get('registration_number')
        transport.capacity = request.POST.get('capacity')
        transport.driver_name = request.POST.get('driver_name')
        transport.driver_contact = request.POST.get('driver_contact')
        transport.route_details = request.POST.get('route_details')
        transport.available_timings = request.POST.get('available_timings')
        associated_hostel_id = request.POST.get('associated_hostel')

        transport.associated_hostel = get_object_or_404(Hostel, id=associated_hostel_id)

        if request.FILES.get('image'):
            transport.image = request.FILES.get('image')

        transport.save()
        messages.success(request, "Transport updated successfully.")
        return redirect("transport_list")

    return render(request, "others/transport/edit-transport.html", {
        "transport": transport,
        "hostels": hostels
    })

def view_transport(request,  registration_number):
    transport = get_object_or_404(Transport,  registration_number= registration_number)
    return render(request, "others/transport/transport-details.html", {"transport": transport})

def delete_transport(request,  registration_number):
    if request.method == "POST":
        transport = get_object_or_404(Transport,  registration_number= registration_number)
        transport_name = transport.name
        transport.delete()
        messages.success(request, f"Transport '{transport_name}' deleted successfully.")
        return redirect("transport_list")
    return HttpResponseForbidden()