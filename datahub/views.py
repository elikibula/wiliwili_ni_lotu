from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Sum, Count
from .models import *
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, "You are now logged in")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="datahub/login.html", context={"login_form":form})

@login_required(login_url='login')
def index(request):
    DatahubLewenilotus = DatahubLewenilotu.objects.all()
    total_lewenilotu = DatahubLewenilotus.count()   # Wilwwili ni Tabacakacaka

    DatahubValenilotus = DatahubValenilotu.objects.all()
    total_valenilotu = DatahubValenilotus.count() # Wilwwili ni Valenilotu Tabacakacaka

    DatahubMatasigas = DatahubMatasiga.objects.all()
    total_matasiga = DatahubMatasigas.count() # Wilwwili ni Matasiga Tabacakacaka

    DatahubVeitokanis = DatahubVeitokani.objects.all()
    total_veitokani = DatahubVeitokanis.count() # Wilwwili ni Veitokani Tabacakacaka

    # Nai Wiliwili ni Sunday School ena loma ni Tabacakacaka
    total_sundayschool = DatahubLewenilotus.filter(nona_veitokani__in=[1,2,3,4,5,6,7,8,9,10,12]).count() # count ni Sunday School

    # Nai Wiliwili ni MYF ena loma ni Tabacakacaka
    total_myf = DatahubLewenilotus.filter(nona_veitokani__in=[13,14,15,16,17,18,19,20,21,22,24]).count() # count ni MYF

    # Nai Wiliwili ni Marama ena loma ni Tabacakacaka
    total_marama = DatahubLewenilotus.filter(nona_veitokani__in=[37,38,39,40,41,42,43,44,45,46,48]).count() # count ni Marama

    # Nai Wiliwili ni Marama ena loma ni Tabacakacaka
    total_turaga = DatahubLewenilotus.filter(nona_veitokani__in=[25,26,27,27,28,29,30,31,32,33,34,36]).count() # count ni Turaga

    #Wiliwili ni Siga Dina kei na Siga Tuberi
    total_sigadina = DatahubLewenilotus.filter(tutu_vakalotu ='sigadina').count() # count ni Siga Dina
    total_sigatuberi = DatahubLewenilotus.filter(tutu_vakalotu ='sigatuberi').count() # count ni Siga Tuberi

    total_talatalavakacegu = DatahubLewenilotus.filter(tavi_vakalotu ='talcg').count() # count ni Talatala Vakacegu
    total_talatalayaco = DatahubLewenilotus.filter(tavi_vakalotu ='talyc').count() # count ni Talatala Yaco
    total_talatalavakatovolei = DatahubLewenilotus.filter(tavi_vakalotu ='taltv').count() # count ni Talatala Vakatovolei
    total_vakatawavakacegu = DatahubLewenilotus.filter(tavi_vakalotu ='vktwcg').count() # count ni Vakatawa Vakacegu
    total_vakatawayaco = DatahubLewenilotus.filter(tavi_vakalotu ='vktwyc').count() # count ni Vakatawa Yaco
    total_vakatawacavuti = DatahubLewenilotus.filter(tavi_vakalotu ='vktwcv').count() # count ni Vakatawa Cavuti
    total_vakatawavakatovolei = DatahubLewenilotus.filter(tavi_vakalotu ='vktwtv').count() # count ni Vakatawa Vakatovolei
    total_dauvunauvakacegu = DatahubLewenilotus.filter(tavi_vakalotu ='dvncg').count() # count ni Dauvunau Vakacegu
    total_dauvunauyaco = DatahubLewenilotus.filter(tavi_vakalotu ='dvnyc').count() # count ni Dauvunau Yaco
    total_dauvunautovolei = DatahubLewenilotus.filter(tavi_vakalotu ='dvntv').count() # count ni Dauvunau Vakatovolei
    total_daucakamasumasu = DatahubLewenilotus.filter(tavi_vakalotu ='dcms').count() # count ni Daucaka Masumasu
    total_lewenivavakoso = DatahubLewenilotus.filter(tavi_vakalotu ='lwnvk').count() # count ni Leweni Vavakoso

    context = { "total_lewenilotu": total_lewenilotu, "total_valenilotu": total_valenilotu, 
    "total_matasiga": total_matasiga, "total_veitokani": total_veitokani, "total_sigadina": total_sigadina,
    "total_sigatuberi" : total_sigatuberi, "total_talatalavakacegu" : total_talatalavakacegu, "total_talatalayaco": total_talatalayaco,
    "total_talatalavakatovolei" : total_talatalavakatovolei, "total_vakatawavakacegu" : total_vakatawavakacegu, "total_vakatawayaco" : total_vakatawayaco,
    "total_vakatawavakatovolei" : total_vakatawavakatovolei, "total_dauvunauyaco" : total_dauvunauyaco, "total_dauvunautovolei" : total_dauvunautovolei,
    "total_daucakamasumasu" : total_daucakamasumasu, "total_lewenivavakoso" : total_lewenivavakoso, "total_vakatawacavuti" : total_vakatawacavuti,
    "total_dauvunauvakacegu" : total_dauvunauvakacegu, "total_sundayschool": total_sundayschool, "total_myf": total_myf,
    "total_marama" :  total_marama, "total_turaga" : total_turaga }

    return render(request, 'datahub/index.html',context)


@login_required(login_url='login')
def lewenilotu(request):
    DatahubLewenilotus = DatahubLewenilotu.objects.all()
    context = {"DatahubLewenilotus" : DatahubLewenilotus }

    return render(request, 'datahub/lewenilotu.html', context)

@login_required(login_url='login')
def duavata(request):
    DatahubLewenilotus = DatahubLewenilotu.objects.all()
    total_lewenilotu = DatahubLewenilotus.filter(nona_valenilotu=14).count() #Wiliwili ni Vavakoso
    total_sundayschool = DatahubLewenilotus.filter(nona_veitokani=1).count() #Wiliwili ni Sunday School
    total_myf = DatahubLewenilotus.filter(nona_veitokani=13).count() #Wiliwili ni MYF
    total_marama = DatahubLewenilotus.filter(nona_veitokani=37).count() #Wiliwili ni Marama
    total_turaga = DatahubLewenilotus.filter(nona_veitokani=25).count() #Wiliwili ni Marama
    total_sigadina = DatahubLewenilotus.filter(nona_valenilotu=14, tutu_vakalotu ='sigadina').count() #Wiliwili ni Siga DIna
    total_sigatuberi = DatahubLewenilotus.filter(nona_valenilotu=14, tutu_vakalotu ='sigatuberi').count() #Wiliwili ni Siga Tuberi

    total_talatalavakacegu = DatahubLewenilotus.filter(nona_valenilotu=14, tavi_vakalotu ='talcg').count() # count ni Talatala Vakacegu
    total_talatalayaco = DatahubLewenilotus.filter(nona_valenilotu=14, tavi_vakalotu ='talyc').count() # count ni Talatala Yaco
    total_talatalavakatovolei = DatahubLewenilotus.filter(nona_valenilotu=14, tavi_vakalotu ='taltv').count() # count ni Talatala Vakatovolei
    total_vakatawavakacegu = DatahubLewenilotus.filter(nona_valenilotu=14, tavi_vakalotu ='vktwcg').count() # count ni Vakatawa Vakacegu
    total_vakatawayaco = DatahubLewenilotus.filter(nona_valenilotu=14, tavi_vakalotu ='vktwyc').count() # count ni Vakatawa Yaco
    total_vakatawacavuti = DatahubLewenilotus.filter(nona_valenilotu=14, tavi_vakalotu ='vktwcv').count() # count ni Vakatawa Cavuti
    total_vakatawavakatovolei = DatahubLewenilotus.filter(nona_valenilotu=14, tavi_vakalotu ='vktwtv').count() # count ni Vakatawa Vakatovolei
    total_dauvunauvakacegu = DatahubLewenilotus.filter(nona_valenilotu=14, tavi_vakalotu ='dvncg').count() # count ni Dauvunau Vakacegu
    total_dauvunauyaco = DatahubLewenilotus.filter(nona_valenilotu=14, tavi_vakalotu ='dvnyc').count() # count ni Dauvunau Yaco
    total_dauvunautovolei = DatahubLewenilotus.filter(nona_valenilotu=14, tavi_vakalotu ='dvntv').count() # count ni Dauvunau Vakatovolei
    total_daucakamasumasu = DatahubLewenilotus.filter(nona_valenilotu=14, tavi_vakalotu ='dcms').count() # count ni Daucaka Masumasu
    total_lewenivavakoso = DatahubLewenilotus.filter(nona_valenilotu=14, tavi_vakalotu ='lwnvk').count() # count ni Leweni Vavakoso


    context = { "total_lewenilotu":total_lewenilotu, "total_sundayschool": total_sundayschool, "total_myf" : total_myf,
    "total_marama" : total_marama, "total_turaga" : total_turaga, "total_sigadina" : total_sigadina, "total_sigatuberi" : total_sigatuberi,
    "total_talatalavakacegu" : total_talatalavakacegu, "total_talatalayaco": total_talatalayaco,
    "total_talatalavakatovolei" : total_talatalavakatovolei, "total_vakatawavakacegu" : total_vakatawavakacegu, "total_vakatawayaco" : total_vakatawayaco,
    "total_vakatawavakatovolei" : total_vakatawavakatovolei, "total_dauvunauyaco" : total_dauvunauyaco, "total_dauvunautovolei" : total_dauvunautovolei,
    "total_daucakamasumasu" : total_daucakamasumasu, "total_lewenivavakoso" : total_lewenivavakoso, "total_vakatawacavuti" : total_vakatawacavuti,
    "total_dauvunauvakacegu" : total_dauvunauvakacegu }

    return render(request, 'datahub/duavata.html', context)

@login_required(login_url='login')
def efiraca(request):
    DatahubLewenilotus = DatahubLewenilotu.objects.all()
    total_lewenilotu = DatahubLewenilotus.filter(nona_valenilotu=13).count() #Wiliwili ni Vavakoso
    total_sundayschool = DatahubLewenilotus.filter(nona_veitokani=2).count() #Wiliwili ni Sunday School
    total_myf = DatahubLewenilotus.filter(nona_veitokani=14).count() #Wiliwili ni MYF
    total_marama = DatahubLewenilotus.filter(nona_veitokani=38).count() #Wiliwili ni Marama
    total_turaga = DatahubLewenilotus.filter(nona_veitokani=26).count() #Wiliwili ni Marama
    total_sigadina = DatahubLewenilotus.filter(nona_valenilotu=13, tutu_vakalotu ='sigadina').count() #Wiliwili ni Siga DIna
    total_sigatuberi = DatahubLewenilotus.filter(nona_valenilotu=13, tutu_vakalotu ='sigatuberi').count() #Wiliwili ni Siga Tuberi

    total_talatalavakacegu = DatahubLewenilotus.filter(nona_valenilotu=13, tavi_vakalotu ='talcg').count() # count ni Talatala Vakacegu
    total_talatalayaco = DatahubLewenilotus.filter(nona_valenilotu=13, tavi_vakalotu ='talyc').count() # count ni Talatala Yaco
    total_talatalavakatovolei = DatahubLewenilotus.filter(nona_valenilotu=13, tavi_vakalotu ='taltv').count() # count ni Talatala Vakatovolei
    total_vakatawavakacegu = DatahubLewenilotus.filter(nona_valenilotu=13, tavi_vakalotu ='vktwcg').count() # count ni Vakatawa Vakacegu
    total_vakatawayaco = DatahubLewenilotus.filter(nona_valenilotu=13, tavi_vakalotu ='vktwyc').count() # count ni Vakatawa Yaco
    total_vakatawacavuti = DatahubLewenilotus.filter(nona_valenilotu=13, tavi_vakalotu ='vktwcv').count() # count ni Vakatawa Cavuti
    total_vakatawavakatovolei = DatahubLewenilotus.filter(nona_valenilotu=13, tavi_vakalotu ='vktwtv').count() # count ni Vakatawa Vakatovolei
    total_dauvunauvakacegu = DatahubLewenilotus.filter(nona_valenilotu=13, tavi_vakalotu ='dvncg').count() # count ni Dauvunau Vakacegu
    total_dauvunauyaco = DatahubLewenilotus.filter(nona_valenilotu=13, tavi_vakalotu ='dvnyc').count() # count ni Dauvunau Yaco
    total_dauvunautovolei = DatahubLewenilotus.filter(nona_valenilotu=13, tavi_vakalotu ='dvntv').count() # count ni Dauvunau Vakatovolei
    total_daucakamasumasu = DatahubLewenilotus.filter(nona_valenilotu=13, tavi_vakalotu ='dcms').count() # count ni Daucaka Masumasu
    total_lewenivavakoso = DatahubLewenilotus.filter(nona_valenilotu=13, tavi_vakalotu ='lwnvk').count() # count ni Leweni Vavakoso


    context = { "total_lewenilotu":total_lewenilotu, "total_sundayschool": total_sundayschool, "total_myf" : total_myf,
    "total_marama" : total_marama, "total_turaga" : total_turaga, "total_sigadina" : total_sigadina, "total_sigatuberi" : total_sigatuberi,
    "total_talatalavakacegu" : total_talatalavakacegu, "total_talatalayaco": total_talatalayaco,
    "total_talatalavakatovolei" : total_talatalavakatovolei, "total_vakatawavakacegu" : total_vakatawavakacegu, "total_vakatawayaco" : total_vakatawayaco,
    "total_vakatawavakatovolei" : total_vakatawavakatovolei, "total_dauvunauyaco" : total_dauvunauyaco, "total_dauvunautovolei" : total_dauvunautovolei,
    "total_daucakamasumasu" : total_daucakamasumasu, "total_lewenivavakoso" : total_lewenivavakoso, "total_vakatawacavuti" : total_vakatawacavuti,
    "total_dauvunauvakacegu" : total_dauvunauvakacegu }

    return render(request, 'datahub/efiraca.html', context)

@login_required(login_url='login')
def jiovajaire(request):
    DatahubLewenilotus = DatahubLewenilotu.objects.all()
    total_lewenilotu = DatahubLewenilotus.filter(nona_valenilotu=12).count() #Wiliwili ni Vavakoso
    total_sundayschool = DatahubLewenilotus.filter(nona_veitokani=3).count() #Wiliwili ni Sunday School
    total_myf = DatahubLewenilotus.filter(nona_veitokani=15).count() #Wiliwili ni MYF
    total_marama = DatahubLewenilotus.filter(nona_veitokani=39).count() #Wiliwili ni Marama
    total_turaga = DatahubLewenilotus.filter(nona_veitokani=27).count() #Wiliwili ni Marama
    total_sigadina = DatahubLewenilotus.filter(nona_valenilotu=12, tutu_vakalotu ='sigadina').count() #Wiliwili ni Siga DIna
    total_sigatuberi = DatahubLewenilotus.filter(nona_valenilotu=12, tutu_vakalotu ='sigatuberi').count() #Wiliwili ni Siga Tuberi

    total_talatalavakacegu = DatahubLewenilotus.filter(nona_valenilotu=12, tavi_vakalotu ='talcg').count() # count ni Talatala Vakacegu
    total_talatalayaco = DatahubLewenilotus.filter(nona_valenilotu=12, tavi_vakalotu ='talyc').count() # count ni Talatala Yaco
    total_talatalavakatovolei = DatahubLewenilotus.filter(nona_valenilotu=12, tavi_vakalotu ='taltv').count() # count ni Talatala Vakatovolei
    total_vakatawavakacegu = DatahubLewenilotus.filter(nona_valenilotu=12, tavi_vakalotu ='vktwcg').count() # count ni Vakatawa Vakacegu
    total_vakatawayaco = DatahubLewenilotus.filter(nona_valenilotu=12, tavi_vakalotu ='vktwyc').count() # count ni Vakatawa Yaco
    total_vakatawacavuti = DatahubLewenilotus.filter(nona_valenilotu=12, tavi_vakalotu ='vktwcv').count() # count ni Vakatawa Cavuti
    total_vakatawavakatovolei = DatahubLewenilotus.filter(nona_valenilotu=12, tavi_vakalotu ='vktwtv').count() # count ni Vakatawa Vakatovolei
    total_dauvunauvakacegu = DatahubLewenilotus.filter(nona_valenilotu=12, tavi_vakalotu ='dvncg').count() # count ni Dauvunau Vakacegu
    total_dauvunauyaco = DatahubLewenilotus.filter(nona_valenilotu=12, tavi_vakalotu ='dvnyc').count() # count ni Dauvunau Yaco
    total_dauvunautovolei = DatahubLewenilotus.filter(nona_valenilotu=12, tavi_vakalotu ='dvntv').count() # count ni Dauvunau Vakatovolei
    total_daucakamasumasu = DatahubLewenilotus.filter(nona_valenilotu=12, tavi_vakalotu ='dcms').count() # count ni Daucaka Masumasu
    total_lewenivavakoso = DatahubLewenilotus.filter(nona_valenilotu=12, tavi_vakalotu ='lwnvk').count() # count ni Leweni Vavakoso


    context = { "total_lewenilotu":total_lewenilotu, "total_sundayschool": total_sundayschool, "total_myf" : total_myf,
    "total_marama" : total_marama, "total_turaga" : total_turaga, "total_sigadina" : total_sigadina, "total_sigatuberi" : total_sigatuberi,
    "total_talatalavakacegu" : total_talatalavakacegu, "total_talatalayaco": total_talatalayaco,
    "total_talatalavakatovolei" : total_talatalavakatovolei, "total_vakatawavakacegu" : total_vakatawavakacegu, "total_vakatawayaco" : total_vakatawayaco,
    "total_vakatawavakatovolei" : total_vakatawavakatovolei, "total_dauvunauyaco" : total_dauvunauyaco, "total_dauvunautovolei" : total_dauvunautovolei,
    "total_daucakamasumasu" : total_daucakamasumasu, "total_lewenivavakoso" : total_lewenivavakoso, "total_vakatawacavuti" : total_vakatawacavuti,
    "total_dauvunauvakacegu" : total_dauvunauvakacegu }

    return render(request, 'datahub/jiovajaire.html', context)

@login_required(login_url='login')
def kecisemani(request):
    DatahubLewenilotus = DatahubLewenilotu.objects.all()
    total_lewenilotu = DatahubLewenilotus.filter(nona_valenilotu=11).count() #Wiliwili ni Vavakoso
    total_sundayschool = DatahubLewenilotus.filter(nona_veitokani=4).count() #Wiliwili ni Sunday School
    total_myf = DatahubLewenilotus.filter(nona_veitokani=16).count() #Wiliwili ni MYF
    total_marama = DatahubLewenilotus.filter(nona_veitokani=40).count() #Wiliwili ni Marama
    total_turaga = DatahubLewenilotus.filter(nona_veitokani=28).count() #Wiliwili ni Marama
    total_sigadina = DatahubLewenilotus.filter(nona_valenilotu=11, tutu_vakalotu ='sigadina').count() #Wiliwili ni Siga DIna
    total_sigatuberi = DatahubLewenilotus.filter(nona_valenilotu=11, tutu_vakalotu ='sigatuberi').count() #Wiliwili ni Siga Tuberi

    total_talatalavakacegu = DatahubLewenilotus.filter(nona_valenilotu=11, tavi_vakalotu ='talcg').count() # count ni Talatala Vakacegu
    total_talatalayaco = DatahubLewenilotus.filter(nona_valenilotu=11, tavi_vakalotu ='talyc').count() # count ni Talatala Yaco
    total_talatalavakatovolei = DatahubLewenilotus.filter(nona_valenilotu=11, tavi_vakalotu ='taltv').count() # count ni Talatala Vakatovolei
    total_vakatawavakacegu = DatahubLewenilotus.filter(nona_valenilotu=11, tavi_vakalotu ='vktwcg').count() # count ni Vakatawa Vakacegu
    total_vakatawayaco = DatahubLewenilotus.filter(nona_valenilotu=11, tavi_vakalotu ='vktwyc').count() # count ni Vakatawa Yaco
    total_vakatawacavuti = DatahubLewenilotus.filter(nona_valenilotu=11, tavi_vakalotu ='vktwcv').count() # count ni Vakatawa Cavuti
    total_vakatawavakatovolei = DatahubLewenilotus.filter(nona_valenilotu=11, tavi_vakalotu ='vktwtv').count() # count ni Vakatawa Vakatovolei
    total_dauvunauvakacegu = DatahubLewenilotus.filter(nona_valenilotu=11, tavi_vakalotu ='dvncg').count() # count ni Dauvunau Vakacegu
    total_dauvunauyaco = DatahubLewenilotus.filter(nona_valenilotu=11, tavi_vakalotu ='dvnyc').count() # count ni Dauvunau Yaco
    total_dauvunautovolei = DatahubLewenilotus.filter(nona_valenilotu=11, tavi_vakalotu ='dvntv').count() # count ni Dauvunau Vakatovolei
    total_daucakamasumasu = DatahubLewenilotus.filter(nona_valenilotu=11, tavi_vakalotu ='dcms').count() # count ni Daucaka Masumasu
    total_lewenivavakoso = DatahubLewenilotus.filter(nona_valenilotu=11, tavi_vakalotu ='lwnvk').count() # count ni Leweni Vavakoso


    context = { "total_lewenilotu":total_lewenilotu, "total_sundayschool": total_sundayschool, "total_myf" : total_myf,
    "total_marama" : total_marama, "total_turaga" : total_turaga, "total_sigadina" : total_sigadina, "total_sigatuberi" : total_sigatuberi,
    "total_talatalavakacegu" : total_talatalavakacegu, "total_talatalayaco": total_talatalayaco,
    "total_talatalavakatovolei" : total_talatalavakatovolei, "total_vakatawavakacegu" : total_vakatawavakacegu, "total_vakatawayaco" : total_vakatawayaco,
    "total_vakatawavakatovolei" : total_vakatawavakatovolei, "total_dauvunauyaco" : total_dauvunauyaco, "total_dauvunautovolei" : total_dauvunautovolei,
    "total_daucakamasumasu" : total_daucakamasumasu, "total_lewenivavakoso" : total_lewenivavakoso, "total_vakatawacavuti" : total_vakatawacavuti,
    "total_dauvunauvakacegu" : total_dauvunauvakacegu }

    return render(request, 'datahub/kecisemani.html', context)

@login_required(login_url='login')
def meeneimi(request):
    DatahubLewenilotus = DatahubLewenilotu.objects.all()
    total_lewenilotu = DatahubLewenilotus.filter(nona_valenilotu=10).count() #Wiliwili ni Vavakoso
    total_sundayschool = DatahubLewenilotus.filter(nona_veitokani=5).count() #Wiliwili ni Sunday School
    total_myf = DatahubLewenilotus.filter(nona_veitokani=17).count() #Wiliwili ni MYF
    total_marama = DatahubLewenilotus.filter(nona_veitokani=41).count() #Wiliwili ni Marama
    total_turaga = DatahubLewenilotus.filter(nona_veitokani=29).count() #Wiliwili ni Marama
    total_sigadina = DatahubLewenilotus.filter(nona_valenilotu=10, tutu_vakalotu ='sigadina').count() #Wiliwili ni Siga DIna
    total_sigatuberi = DatahubLewenilotus.filter(nona_valenilotu=10, tutu_vakalotu ='sigatuberi').count() #Wiliwili ni Siga Tuberi

    total_talatalavakacegu = DatahubLewenilotus.filter(nona_valenilotu=10, tavi_vakalotu ='talcg').count() # count ni Talatala Vakacegu
    total_talatalayaco = DatahubLewenilotus.filter(nona_valenilotu=10, tavi_vakalotu ='talyc').count() # count ni Talatala Yaco
    total_talatalavakatovolei = DatahubLewenilotus.filter(nona_valenilotu=10, tavi_vakalotu ='taltv').count() # count ni Talatala Vakatovolei
    total_vakatawavakacegu = DatahubLewenilotus.filter(nona_valenilotu=10, tavi_vakalotu ='vktwcg').count() # count ni Vakatawa Vakacegu
    total_vakatawayaco = DatahubLewenilotus.filter(nona_valenilotu=10, tavi_vakalotu ='vktwyc').count() # count ni Vakatawa Yaco
    total_vakatawacavuti = DatahubLewenilotus.filter(nona_valenilotu=10, tavi_vakalotu ='vktwcv').count() # count ni Vakatawa Cavuti
    total_vakatawavakatovolei = DatahubLewenilotus.filter(nona_valenilotu=10, tavi_vakalotu ='vktwtv').count() # count ni Vakatawa Vakatovolei
    total_dauvunauvakacegu = DatahubLewenilotus.filter(nona_valenilotu=10, tavi_vakalotu ='dvncg').count() # count ni Dauvunau Vakacegu
    total_dauvunauyaco = DatahubLewenilotus.filter(nona_valenilotu=10, tavi_vakalotu ='dvnyc').count() # count ni Dauvunau Yaco
    total_dauvunautovolei = DatahubLewenilotus.filter(nona_valenilotu=10, tavi_vakalotu ='dvntv').count() # count ni Dauvunau Vakatovolei
    total_daucakamasumasu = DatahubLewenilotus.filter(nona_valenilotu=10, tavi_vakalotu ='dcms').count() # count ni Daucaka Masumasu
    total_lewenivavakoso = DatahubLewenilotus.filter(nona_valenilotu=10, tavi_vakalotu ='lwnvk').count() # count ni Leweni Vavakoso


    context = { "total_lewenilotu":total_lewenilotu, "total_sundayschool": total_sundayschool, "total_myf" : total_myf,
    "total_marama" : total_marama, "total_turaga" : total_turaga, "total_sigadina" : total_sigadina, "total_sigatuberi" : total_sigatuberi,
    "total_talatalavakacegu" : total_talatalavakacegu, "total_talatalayaco": total_talatalayaco,
    "total_talatalavakatovolei" : total_talatalavakatovolei, "total_vakatawavakacegu" : total_vakatawavakacegu, "total_vakatawayaco" : total_vakatawayaco,
    "total_vakatawavakatovolei" : total_vakatawavakatovolei, "total_dauvunauyaco" : total_dauvunauyaco, "total_dauvunautovolei" : total_dauvunautovolei,
    "total_daucakamasumasu" : total_daucakamasumasu, "total_lewenivavakoso" : total_lewenivavakoso, "total_vakatawacavuti" : total_vakatawacavuti,
    "total_dauvunauvakacegu" : total_dauvunauvakacegu }

    return render(request, 'datahub/meeneimi.html', context)

@login_required(login_url='login')
def mountsinai(request):
    DatahubLewenilotus = DatahubLewenilotu.objects.all()
    total_lewenilotu = DatahubLewenilotus.filter(nona_valenilotu=9).count() #Wiliwili ni Vavakoso
    total_sundayschool = DatahubLewenilotus.filter(nona_veitokani=6).count() #Wiliwili ni Sunday School
    total_myf = DatahubLewenilotus.filter(nona_veitokani=18).count() #Wiliwili ni MYF
    total_marama = DatahubLewenilotus.filter(nona_veitokani=42).count() #Wiliwili ni Marama
    total_turaga = DatahubLewenilotus.filter(nona_veitokani=30).count() #Wiliwili ni Marama
    total_sigadina = DatahubLewenilotus.filter(nona_valenilotu=9, tutu_vakalotu ='sigadina').count() #Wiliwili ni Siga DIna
    total_sigatuberi = DatahubLewenilotus.filter(nona_valenilotu=9, tutu_vakalotu ='sigatuberi').count() #Wiliwili ni Siga Tuberi

    total_talatalavakacegu = DatahubLewenilotus.filter(nona_valenilotu=9, tavi_vakalotu ='talcg').count() # count ni Talatala Vakacegu
    total_talatalayaco = DatahubLewenilotus.filter(nona_valenilotu=9, tavi_vakalotu ='talyc').count() # count ni Talatala Yaco
    total_talatalavakatovolei = DatahubLewenilotus.filter(nona_valenilotu=9, tavi_vakalotu ='taltv').count() # count ni Talatala Vakatovolei
    total_vakatawavakacegu = DatahubLewenilotus.filter(nona_valenilotu=9, tavi_vakalotu ='vktwcg').count() # count ni Vakatawa Vakacegu
    total_vakatawayaco = DatahubLewenilotus.filter(nona_valenilotu=9, tavi_vakalotu ='vktwyc').count() # count ni Vakatawa Yaco
    total_vakatawacavuti = DatahubLewenilotus.filter(nona_valenilotu=9, tavi_vakalotu ='vktwcv').count() # count ni Vakatawa Cavuti
    total_vakatawavakatovolei = DatahubLewenilotus.filter(nona_valenilotu=9, tavi_vakalotu ='vktwtv').count() # count ni Vakatawa Vakatovolei
    total_dauvunauvakacegu = DatahubLewenilotus.filter(nona_valenilotu=9, tavi_vakalotu ='dvncg').count() # count ni Dauvunau Vakacegu
    total_dauvunauyaco = DatahubLewenilotus.filter(nona_valenilotu=9, tavi_vakalotu ='dvnyc').count() # count ni Dauvunau Yaco
    total_dauvunautovolei = DatahubLewenilotus.filter(nona_valenilotu=9, tavi_vakalotu ='dvntv').count() # count ni Dauvunau Vakatovolei
    total_daucakamasumasu = DatahubLewenilotus.filter(nona_valenilotu=9, tavi_vakalotu ='dcms').count() # count ni Daucaka Masumasu
    total_lewenivavakoso = DatahubLewenilotus.filter(nona_valenilotu=9, tavi_vakalotu ='lwnvk').count() # count ni Leweni Vavakoso


    context = { "total_lewenilotu":total_lewenilotu, "total_sundayschool": total_sundayschool, "total_myf" : total_myf,
    "total_marama" : total_marama, "total_turaga" : total_turaga, "total_sigadina" : total_sigadina, "total_sigatuberi" : total_sigatuberi,
    "total_talatalavakacegu" : total_talatalavakacegu, "total_talatalayaco": total_talatalayaco,
    "total_talatalavakatovolei" : total_talatalavakatovolei, "total_vakatawavakacegu" : total_vakatawavakacegu, "total_vakatawayaco" : total_vakatawayaco,
    "total_vakatawavakatovolei" : total_vakatawavakatovolei, "total_dauvunauyaco" : total_dauvunauyaco, "total_dauvunautovolei" : total_dauvunautovolei,
    "total_daucakamasumasu" : total_daucakamasumasu, "total_lewenivavakoso" : total_lewenivavakoso, "total_vakatawacavuti" : total_vakatawacavuti,
    "total_dauvunauvakacegu" : total_dauvunauvakacegu }

    return render(request, 'datahub/mountsinai.html', context)

@login_required(login_url='login')
def nauluvatu(request):
    DatahubLewenilotus = DatahubLewenilotu.objects.all()
    total_lewenilotu = DatahubLewenilotus.filter(nona_valenilotu=8).count() #Wiliwili ni Vavakoso
    total_sundayschool = DatahubLewenilotus.filter(nona_veitokani=7).count() #Wiliwili ni Sunday School
    total_myf = DatahubLewenilotus.filter(nona_veitokani=19).count() #Wiliwili ni MYF
    total_marama = DatahubLewenilotus.filter(nona_veitokani=43).count() #Wiliwili ni Marama
    total_turaga = DatahubLewenilotus.filter(nona_veitokani=31).count() #Wiliwili ni Marama
    total_sigadina = DatahubLewenilotus.filter(nona_valenilotu=8, tutu_vakalotu ='sigadina').count() #Wiliwili ni Siga DIna
    total_sigatuberi = DatahubLewenilotus.filter(nona_valenilotu=8, tutu_vakalotu ='sigatuberi').count() #Wiliwili ni Siga Tuberi

    total_talatalavakacegu = DatahubLewenilotus.filter(nona_valenilotu=8, tavi_vakalotu ='talcg').count() # count ni Talatala Vakacegu
    total_talatalayaco = DatahubLewenilotus.filter(nona_valenilotu=8, tavi_vakalotu ='talyc').count() # count ni Talatala Yaco
    total_talatalavakatovolei = DatahubLewenilotus.filter(nona_valenilotu=8, tavi_vakalotu ='taltv').count() # count ni Talatala Vakatovolei
    total_vakatawavakacegu = DatahubLewenilotus.filter(nona_valenilotu=8, tavi_vakalotu ='vktwcg').count() # count ni Vakatawa Vakacegu
    total_vakatawayaco = DatahubLewenilotus.filter(nona_valenilotu=8, tavi_vakalotu ='vktwyc').count() # count ni Vakatawa Yaco
    total_vakatawacavuti = DatahubLewenilotus.filter(nona_valenilotu=8, tavi_vakalotu ='vktwcv').count() # count ni Vakatawa Cavuti
    total_vakatawavakatovolei = DatahubLewenilotus.filter(nona_valenilotu=8, tavi_vakalotu ='vktwtv').count() # count ni Vakatawa Vakatovolei
    total_dauvunauvakacegu = DatahubLewenilotus.filter(nona_valenilotu=8, tavi_vakalotu ='dvncg').count() # count ni Dauvunau Vakacegu
    total_dauvunauyaco = DatahubLewenilotus.filter(nona_valenilotu=8, tavi_vakalotu ='dvnyc').count() # count ni Dauvunau Yaco
    total_dauvunautovolei = DatahubLewenilotus.filter(nona_valenilotu=8, tavi_vakalotu ='dvntv').count() # count ni Dauvunau Vakatovolei
    total_daucakamasumasu = DatahubLewenilotus.filter(nona_valenilotu=8, tavi_vakalotu ='dcms').count() # count ni Daucaka Masumasu
    total_lewenivavakoso = DatahubLewenilotus.filter(nona_valenilotu=8, tavi_vakalotu ='lwnvk').count() # count ni Leweni Vavakoso


    context = { "total_lewenilotu":total_lewenilotu, "total_sundayschool": total_sundayschool, "total_myf" : total_myf,
    "total_marama" : total_marama, "total_turaga" : total_turaga, "total_sigadina" : total_sigadina, "total_sigatuberi" : total_sigatuberi,
    "total_talatalavakacegu" : total_talatalavakacegu, "total_talatalayaco": total_talatalayaco,
    "total_talatalavakatovolei" : total_talatalavakatovolei, "total_vakatawavakacegu" : total_vakatawavakacegu, "total_vakatawayaco" : total_vakatawayaco,
    "total_vakatawavakatovolei" : total_vakatawavakatovolei, "total_dauvunauyaco" : total_dauvunauyaco, "total_dauvunautovolei" : total_dauvunautovolei,
    "total_daucakamasumasu" : total_daucakamasumasu, "total_lewenivavakoso" : total_lewenivavakoso, "total_vakatawacavuti" : total_vakatawacavuti,
    "total_dauvunauvakacegu" : total_dauvunauvakacegu }

    return render(request, 'datahub/nauluvatu.html', context)

@login_required(login_url='login')
def peceseita(request):
    DatahubLewenilotus = DatahubLewenilotu.objects.all()
    total_lewenilotu = DatahubLewenilotus.filter(nona_valenilotu=7).count() #Wiliwili ni Vavakoso
    total_sundayschool = DatahubLewenilotus.filter(nona_veitokani=1).count() #Wiliwili ni Sunday School
    total_myf = DatahubLewenilotus.filter(nona_veitokani=20).count() #Wiliwili ni MYF
    total_marama = DatahubLewenilotus.filter(nona_veitokani=44).count() #Wiliwili ni Marama
    total_turaga = DatahubLewenilotus.filter(nona_veitokani=32).count() #Wiliwili ni Marama
    total_sigadina = DatahubLewenilotus.filter(nona_valenilotu=7, tutu_vakalotu ='sigadina').count() #Wiliwili ni Siga DIna
    total_sigatuberi = DatahubLewenilotus.filter(nona_valenilotu=7, tutu_vakalotu ='sigatuberi').count() #Wiliwili ni Siga Tuberi

    total_talatalavakacegu = DatahubLewenilotus.filter(nona_valenilotu=7, tavi_vakalotu ='talcg').count() # count ni Talatala Vakacegu
    total_talatalayaco = DatahubLewenilotus.filter(nona_valenilotu=7, tavi_vakalotu ='talyc').count() # count ni Talatala Yaco
    total_talatalavakatovolei = DatahubLewenilotus.filter(nona_valenilotu=7, tavi_vakalotu ='taltv').count() # count ni Talatala Vakatovolei
    total_vakatawavakacegu = DatahubLewenilotus.filter(nona_valenilotu=7, tavi_vakalotu ='vktwcg').count() # count ni Vakatawa Vakacegu
    total_vakatawayaco = DatahubLewenilotus.filter(nona_valenilotu=7, tavi_vakalotu ='vktwyc').count() # count ni Vakatawa Yaco
    total_vakatawacavuti = DatahubLewenilotus.filter(nona_valenilotu=7, tavi_vakalotu ='vktwcv').count() # count ni Vakatawa Cavuti
    total_vakatawavakatovolei = DatahubLewenilotus.filter(nona_valenilotu=7, tavi_vakalotu ='vktwtv').count() # count ni Vakatawa Vakatovolei
    total_dauvunauvakacegu = DatahubLewenilotus.filter(nona_valenilotu=7, tavi_vakalotu ='dvncg').count() # count ni Dauvunau Vakacegu
    total_dauvunauyaco = DatahubLewenilotus.filter(nona_valenilotu=7, tavi_vakalotu ='dvnyc').count() # count ni Dauvunau Yaco
    total_dauvunautovolei = DatahubLewenilotus.filter(nona_valenilotu=7, tavi_vakalotu ='dvntv').count() # count ni Dauvunau Vakatovolei
    total_daucakamasumasu = DatahubLewenilotus.filter(nona_valenilotu=7, tavi_vakalotu ='dcms').count() # count ni Daucaka Masumasu
    total_lewenivavakoso = DatahubLewenilotus.filter(nona_valenilotu=7, tavi_vakalotu ='lwnvk').count() # count ni Leweni Vavakoso


    context = { "total_lewenilotu":total_lewenilotu, "total_sundayschool": total_sundayschool, "total_myf" : total_myf,
    "total_marama" : total_marama, "total_turaga" : total_turaga, "total_sigadina" : total_sigadina, "total_sigatuberi" : total_sigatuberi,
    "total_talatalavakacegu" : total_talatalavakacegu, "total_talatalayaco": total_talatalayaco,
    "total_talatalavakatovolei" : total_talatalavakatovolei, "total_vakatawavakacegu" : total_vakatawavakacegu, "total_vakatawayaco" : total_vakatawayaco,
    "total_vakatawavakatovolei" : total_vakatawavakatovolei, "total_dauvunauyaco" : total_dauvunauyaco, "total_dauvunautovolei" : total_dauvunautovolei,
    "total_daucakamasumasu" : total_daucakamasumasu, "total_lewenivavakoso" : total_lewenivavakoso, "total_vakatawacavuti" : total_vakatawacavuti,
    "total_dauvunauvakacegu" : total_dauvunauvakacegu }

    return render(request, 'datahub/peceseita.html', context)

@login_required(login_url='login')
def revcaleb(request):
    DatahubLewenilotus = DatahubLewenilotu.objects.all()
    total_lewenilotu = DatahubLewenilotus.filter(nona_valenilotu=6).count() #Wiliwili ni Vavakoso
    total_sundayschool = DatahubLewenilotus.filter(nona_veitokani=9).count() #Wiliwili ni Sunday School
    total_myf = DatahubLewenilotus.filter(nona_veitokani=21).count() #Wiliwili ni MYF
    total_marama = DatahubLewenilotus.filter(nona_veitokani=45).count() #Wiliwili ni Marama
    total_turaga = DatahubLewenilotus.filter(nona_veitokani=33).count() #Wiliwili ni Marama
    total_sigadina = DatahubLewenilotus.filter(nona_valenilotu=6, tutu_vakalotu ='sigadina').count() #Wiliwili ni Siga DIna
    total_sigatuberi = DatahubLewenilotus.filter(nona_valenilotu=6, tutu_vakalotu ='sigatuberi').count() #Wiliwili ni Siga Tuberi

    total_talatalavakacegu = DatahubLewenilotus.filter(nona_valenilotu=6, tavi_vakalotu ='talcg').count() # count ni Talatala Vakacegu
    total_talatalayaco = DatahubLewenilotus.filter(nona_valenilotu=6, tavi_vakalotu ='talyc').count() # count ni Talatala Yaco
    total_talatalavakatovolei = DatahubLewenilotus.filter(nona_valenilotu=6, tavi_vakalotu ='taltv').count() # count ni Talatala Vakatovolei
    total_vakatawavakacegu = DatahubLewenilotus.filter(nona_valenilotu=6, tavi_vakalotu ='vktwcg').count() # count ni Vakatawa Vakacegu
    total_vakatawayaco = DatahubLewenilotus.filter(nona_valenilotu=6, tavi_vakalotu ='vktwyc').count() # count ni Vakatawa Yaco
    total_vakatawacavuti = DatahubLewenilotus.filter(nona_valenilotu=6, tavi_vakalotu ='vktwcv').count() # count ni Vakatawa Cavuti
    total_vakatawavakatovolei = DatahubLewenilotus.filter(nona_valenilotu=6, tavi_vakalotu ='vktwtv').count() # count ni Vakatawa Vakatovolei
    total_dauvunauvakacegu = DatahubLewenilotus.filter(nona_valenilotu=6, tavi_vakalotu ='dvncg').count() # count ni Dauvunau Vakacegu
    total_dauvunauyaco = DatahubLewenilotus.filter(nona_valenilotu=6, tavi_vakalotu ='dvnyc').count() # count ni Dauvunau Yaco
    total_dauvunautovolei = DatahubLewenilotus.filter(nona_valenilotu=6, tavi_vakalotu ='dvntv').count() # count ni Dauvunau Vakatovolei
    total_daucakamasumasu = DatahubLewenilotus.filter(nona_valenilotu=6, tavi_vakalotu ='dcms').count() # count ni Daucaka Masumasu
    total_lewenivavakoso = DatahubLewenilotus.filter(nona_valenilotu=6, tavi_vakalotu ='lwnvk').count() # count ni Leweni Vavakoso


    context = { "total_lewenilotu":total_lewenilotu, "total_sundayschool": total_sundayschool, "total_myf" : total_myf,
    "total_marama" : total_marama, "total_turaga" : total_turaga, "total_sigadina" : total_sigadina, "total_sigatuberi" : total_sigatuberi,
    "total_talatalavakacegu" : total_talatalavakacegu, "total_talatalayaco": total_talatalayaco,
    "total_talatalavakatovolei" : total_talatalavakatovolei, "total_vakatawavakacegu" : total_vakatawavakacegu, "total_vakatawayaco" : total_vakatawayaco,
    "total_vakatawavakatovolei" : total_vakatawavakatovolei, "total_dauvunauyaco" : total_dauvunauyaco, "total_dauvunautovolei" : total_dauvunautovolei,
    "total_daucakamasumasu" : total_daucakamasumasu, "total_lewenivavakoso" : total_lewenivavakoso, "total_vakatawacavuti" : total_vakatawacavuti,
    "total_dauvunauvakacegu" : total_dauvunauvakacegu }

    return render(request, 'datahub/revcaleb.html', context)

@login_required(login_url='login')
def saika(request):
    DatahubLewenilotus = DatahubLewenilotu.objects.all()
    total_lewenilotu = DatahubLewenilotus.filter(nona_valenilotu=5).count() #Wiliwili ni Vavakoso
    total_sundayschool = DatahubLewenilotus.filter(nona_veitokani=10).count() #Wiliwili ni Sunday School
    total_myf = DatahubLewenilotus.filter(nona_veitokani=22).count() #Wiliwili ni MYF
    total_marama = DatahubLewenilotus.filter(nona_veitokani=46).count() #Wiliwili ni Marama
    total_turaga = DatahubLewenilotus.filter(nona_veitokani=34).count() #Wiliwili ni Marama
    total_sigadina = DatahubLewenilotus.filter(nona_valenilotu=5, tutu_vakalotu ='sigadina').count() #Wiliwili ni Siga DIna
    total_sigatuberi = DatahubLewenilotus.filter(nona_valenilotu=5, tutu_vakalotu ='sigatuberi').count() #Wiliwili ni Siga Tuberi

    total_talatalavakacegu = DatahubLewenilotus.filter(nona_valenilotu=5, tavi_vakalotu ='talcg').count() # count ni Talatala Vakacegu
    total_talatalayaco = DatahubLewenilotus.filter(nona_valenilotu=5, tavi_vakalotu ='talyc').count() # count ni Talatala Yaco
    total_talatalavakatovolei = DatahubLewenilotus.filter(nona_valenilotu=5, tavi_vakalotu ='taltv').count() # count ni Talatala Vakatovolei
    total_vakatawavakacegu = DatahubLewenilotus.filter(nona_valenilotu=5, tavi_vakalotu ='vktwcg').count() # count ni Vakatawa Vakacegu
    total_vakatawayaco = DatahubLewenilotus.filter(nona_valenilotu=5, tavi_vakalotu ='vktwyc').count() # count ni Vakatawa Yaco
    total_vakatawacavuti = DatahubLewenilotus.filter(nona_valenilotu=5, tavi_vakalotu ='vktwcv').count() # count ni Vakatawa Cavuti
    total_vakatawavakatovolei = DatahubLewenilotus.filter(nona_valenilotu=5, tavi_vakalotu ='vktwtv').count() # count ni Vakatawa Vakatovolei
    total_dauvunauvakacegu = DatahubLewenilotus.filter(nona_valenilotu=5, tavi_vakalotu ='dvncg').count() # count ni Dauvunau Vakacegu
    total_dauvunauyaco = DatahubLewenilotus.filter(nona_valenilotu=5, tavi_vakalotu ='dvnyc').count() # count ni Dauvunau Yaco
    total_dauvunautovolei = DatahubLewenilotus.filter(nona_valenilotu=5, tavi_vakalotu ='dvntv').count() # count ni Dauvunau Vakatovolei
    total_daucakamasumasu = DatahubLewenilotus.filter(nona_valenilotu=5, tavi_vakalotu ='dcms').count() # count ni Daucaka Masumasu
    total_lewenivavakoso = DatahubLewenilotus.filter(nona_valenilotu=5, tavi_vakalotu ='lwnvk').count() # count ni Leweni Vavakoso


    context = { "total_lewenilotu":total_lewenilotu, "total_sundayschool": total_sundayschool, "total_myf" : total_myf,
    "total_marama" : total_marama, "total_turaga" : total_turaga, "total_sigadina" : total_sigadina, "total_sigatuberi" : total_sigatuberi,
    "total_talatalavakacegu" : total_talatalavakacegu, "total_talatalayaco": total_talatalayaco,
    "total_talatalavakatovolei" : total_talatalavakatovolei, "total_vakatawavakacegu" : total_vakatawavakacegu, "total_vakatawayaco" : total_vakatawayaco,
    "total_vakatawavakatovolei" : total_vakatawavakatovolei, "total_dauvunauyaco" : total_dauvunauyaco, "total_dauvunautovolei" : total_dauvunautovolei,
    "total_daucakamasumasu" : total_daucakamasumasu, "total_lewenivavakoso" : total_lewenivavakoso, "total_vakatawacavuti" : total_vakatawacavuti,
    "total_dauvunauvakacegu" : total_dauvunauvakacegu }

    return render(request, 'datahub/saika.html', context)

@login_required(login_url='login')
def vunivau(request):
    DatahubLewenilotus = DatahubLewenilotu.objects.all()
    total_lewenilotu = DatahubLewenilotus.filter(nona_valenilotu=3).count() #Wiliwili ni Vavakoso
    total_sundayschool = DatahubLewenilotus.filter(nona_veitokani=12).count() #Wiliwili ni Sunday School
    total_myf = DatahubLewenilotus.filter(nona_veitokani=24).count() #Wiliwili ni MYF
    total_marama = DatahubLewenilotus.filter(nona_veitokani=48).count() #Wiliwili ni Marama
    total_turaga = DatahubLewenilotus.filter(nona_veitokani=36).count() #Wiliwili ni Marama
    total_sigadina = DatahubLewenilotus.filter(nona_valenilotu=3, tutu_vakalotu ='sigadina').count() #Wiliwili ni Siga DIna
    total_sigatuberi = DatahubLewenilotus.filter(nona_valenilotu=3, tutu_vakalotu ='sigatuberi').count() #Wiliwili ni Siga Tuberi

    total_talatalavakacegu = DatahubLewenilotus.filter(nona_valenilotu=3, tavi_vakalotu ='talcg').count() # count ni Talatala Vakacegu
    total_talatalayaco = DatahubLewenilotus.filter(nona_valenilotu=3, tavi_vakalotu ='talyc').count() # count ni Talatala Yaco
    total_talatalavakatovolei = DatahubLewenilotus.filter(nona_valenilotu=3, tavi_vakalotu ='taltv').count() # count ni Talatala Vakatovolei
    total_vakatawavakacegu = DatahubLewenilotus.filter(nona_valenilotu=3, tavi_vakalotu ='vktwcg').count() # count ni Vakatawa Vakacegu
    total_vakatawayaco = DatahubLewenilotus.filter(nona_valenilotu=3, tavi_vakalotu ='vktwyc').count() # count ni Vakatawa Yaco
    total_vakatawacavuti = DatahubLewenilotus.filter(nona_valenilotu=3, tavi_vakalotu ='vktwcv').count() # count ni Vakatawa Cavuti
    total_vakatawavakatovolei = DatahubLewenilotus.filter(nona_valenilotu=3, tavi_vakalotu ='vktwtv').count() # count ni Vakatawa Vakatovolei
    total_dauvunauvakacegu = DatahubLewenilotus.filter(nona_valenilotu=3, tavi_vakalotu ='dvncg').count() # count ni Dauvunau Vakacegu
    total_dauvunauyaco = DatahubLewenilotus.filter(nona_valenilotu=3, tavi_vakalotu ='dvnyc').count() # count ni Dauvunau Yaco
    total_dauvunautovolei = DatahubLewenilotus.filter(nona_valenilotu=3, tavi_vakalotu ='dvntv').count() # count ni Dauvunau Vakatovolei
    total_daucakamasumasu = DatahubLewenilotus.filter(nona_valenilotu=3, tavi_vakalotu ='dcms').count() # count ni Daucaka Masumasu
    total_lewenivavakoso = DatahubLewenilotus.filter(nona_valenilotu=3, tavi_vakalotu ='lwnvk').count() # count ni Leweni Vavakoso


    context = { "total_lewenilotu":total_lewenilotu, "total_sundayschool": total_sundayschool, "total_myf" : total_myf,
    "total_marama" : total_marama, "total_turaga" : total_turaga, "total_sigadina" : total_sigadina, "total_sigatuberi" : total_sigatuberi,
    "total_talatalavakacegu" : total_talatalavakacegu, "total_talatalayaco": total_talatalayaco,
    "total_talatalavakatovolei" : total_talatalavakatovolei, "total_vakatawavakacegu" : total_vakatawavakacegu, "total_vakatawayaco" : total_vakatawayaco,
    "total_vakatawavakatovolei" : total_vakatawavakatovolei, "total_dauvunauyaco" : total_dauvunauyaco, "total_dauvunautovolei" : total_dauvunautovolei,
    "total_daucakamasumasu" : total_daucakamasumasu, "total_lewenivavakoso" : total_lewenivavakoso, "total_vakatawacavuti" : total_vakatawacavuti,
    "total_dauvunauvakacegu" : total_dauvunauvakacegu }

    return render(request, 'datahub/vunivau.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')



def charts(request):
    return render(request, 'datahub/charts.html')


def widgets(request):
    return render(request, 'datahub/widgets.html')




def tables(request):
    return render(request, "datahub/tables.html")




def grid(request):
    return render(request, "datahub/grid.html")




def form_basic(request):
    return render(request, "datahub/form_basic.html")




def form_wizard(request):
    return render(request, "datahub/form_wizard.html")




def buttons(request):
    return render(request, "datahub/buttons.html")




def icon_material(request):
    return render(request, "datahub/icon-material.html")




def icon_fontawesome(request):
    return render(request, "datahub/icon-fontawesome.html")




def elements(request):
    return render(request, "datahub/elements.html")




def gallery(request):
    return render(request, "datahub/gallery.html")





def invoice(request):
    return render(request, "datahub/invoice.html")



def chat(request):
    return render(request, "datahub/chat.html")