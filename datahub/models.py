from unittest.util import _MAX_LENGTH
from django.db import models
from django.db.models.deletion import CASCADE

gender_Choice = (
    ("Tgn", "Tagane"),
    ("Ylw", "Yalewa")
)

tutu_Choice = (
    ("sigadina", "Siga Dina"),
    ("sigatuberi", "Siga Tuberi")
)

tavi_Choice = (
    ("talcg", "Talatala Vakacegu"),
    ("talyc","Talata Yaco"),
    ("taltv","Talatala Vakatovolei"),
    ("vktwcg","Vakatawa Vakacegu"),
    ("vktwyc", "Vakatawa Yaco"),
    ("vktwcv", "Vakatawa Cavuti"),
    ("vktwtv", "Vakatawa Vakatovolei"),
    ("dvncg", "Dauvunau Vakacegu"),
    ("dvnyc", "Dauvunau Yaco"),
    ("dvntv", "Dauvunau Vakatovolei"),
    ("dcms", "Daucaka Masumasu"),
    ("lwnvk","Leweni Vavakoso")
)

toki_Choice = (
    ("tm", "Toki Mai"),
    ("ty", "Toki Yani")

)
papitaiso_Choice = (
    ("io", "Io"),
    ("sega", "Sega"),
    ("str", "Sega ni kilai")
)
cula_Choice = (
    ("io", "Io"),
    ("sega", "Sega")
)
ka_e_yaco_Choice = (
    ("tm", "Toki Mai"),
    ("ty", "Toki Yani"),
    ("vkm", "Vakamau"),
    ("mt", "Mate"),
    ("vkt", "Veika Tale Eso")
)


class DatahubLewenilotu(models.Model):
    id = models.AutoField(primary_key=True)
    yaca_ni_vuvale = models.CharField(max_length=255, blank=True, help_text='Na yaca ni vuvale vakamau kina/ se tiko kina')
    yaca_ni_vavakoso = models.CharField(max_length=255, blank=True, null=True, help_text='Na yacana kece mai nai vola ni sucu')
    date_of_birth=models.DateField(null=True, max_length=50, blank=True, help_text='Na nona tikini siga ni sucu - Dd/Mm/Yy eg 23/03/2010')
    tagane_se_yalewa = models.CharField(choices=gender_Choice,max_length=50, blank=True)
    cula = models.BooleanField(blank=True)
    sega_ni_via_cula = models.BooleanField(blank=True)
    tabu_ni_cula = models.BooleanField(blank=True, help_text='Oqo ira na peipei lalai kei ira era vakatabui vakavuniwai me ra cula')
    papitaiso = models.CharField(choices=papitaiso_Choice, max_length=50, blank=True, help_text='Me kilai e sa Papitaiso oti se sega')
    date_papitaiso_kina = models.DateField(null=True, max_length=50, blank=True, help_text='Na tikini siga ka Papitaiso kina/ ke kilai ga na yabaki ia me vaka na 01/01/2002 e vakaraitaka ni yabaki 2002')
    tutu_vakalotu = models.CharField(choices=tutu_Choice, max_length=50, blank=True)
    date_sigadina_kina = models.DateField(null=True, max_length=50, blank=True, help_text='Na tikini siga ka Siga Dina kina/ ke kilai ga na yabaki ia me vaka na 01/01/2002 e vakaraitaka ni yabaki 2002')
    tavi_vakalotu = models.CharField(choices=tavi_Choice, max_length=50, blank=True)
    yabaki_tekivu_kina = models.CharField(max_length=255, blank=True, help_text='Na yabaki ka tekivu kacivi kina me qarava nai tavivakalotu ka taura tiko nikua')
    yabaki_lutu_kina = models.CharField(max_length=255, blank=True, help_text='Na yabaki ka se lutu mai kina enai tavivakalotu ka taura tiko')
    nona_tukutuku_tavivakalotu = models.TextField(blank=True, help_text='Na nona i tukutuku ena vuku ni nona i tavi vakalotu')
    nona_matasiga= models.ForeignKey('DatahubMatasiga', null=True, on_delete=CASCADE, blank=True)
    nona_valenilotu = models.ForeignKey('DatahubValenilotu', on_delete=CASCADE, null=True, blank=True)
    nona_veitokani = models.ForeignKey('DatahubVeitokani', on_delete=CASCADE, null=True, blank=True)
    nona_cakacaka_valenilotu = models.CharField(max_length=255, null=True, blank=True, help_text='Na cakacaka vakalotu me vaka na Daunisere, Liuliu ni dua nai Soqosoqo')
    yabaki_tekivu_cakacaka = models.CharField(max_length=255, null=True, blank=True, help_text='Na yabaki ka tekivu taura mai kina na cakacaka ka tiko kina ni  kua')
    nona_tukutuku_cakacaka = models.TextField(blank=True, help_text='Na nona i tukutuku ena vuku ni nona cakacaka vakalotu')
    email_contact = models.CharField(max_length=255, blank=True)
    home_address = models.CharField(max_length=255, blank=True)
    phone_contact = models.CharField(max_length=255, blank=True)
    vakamacala_tale_eso = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.yaca_ni_vavakoso}, {self.date_of_birth}, {self.tutu_vakalotu }, {self.tavi_vakalotu}, {self.nona_matasiga}, {self.nona_veitokani}, {self.nona_valenilotu}"

    class Meta:
        db_table = 'datahub_lewenilotu'
        verbose_name_plural = "1. Lewe ni Lotu"


class DatahubMatasiga(models.Model):
    id = models.AutoField(primary_key=True)
    matasiga = models.CharField(max_length=255)
    valenilotu = models.ForeignKey('DatahubValenilotu', on_delete=models.CASCADE, blank=True, null=True)
    liuliu_ni_matasiga = models.CharField(max_length=255,blank=True)
    vanua_dau_soqoni_kina = models.TextField(blank=True)
    veika_dau_qaravi = models.TextField(blank=True)
    vakamacala_tale_eso = models.TextField(blank=True)
    

    def __str__(self):
        return f"{self.matasiga}, {self.valenilotu}"
    
    class Meta:
        db_table = 'datahub_matasiga'
        verbose_name_plural = "2. Matasiga"


class DatahubValenilotu(models.Model):
    id = models.AutoField(primary_key=True)
    valenilotu = models.CharField(max_length=255, blank=True)
    yaca_ni_vakatawa = models.CharField(max_length=255, blank=True)
    vukevuke_ni_vakatawa = models.CharField(max_length=255, blank=True)
    tuirara = models.CharField(max_length=255, blank=True)
    vukevuke_ni_tuirara = models.CharField(max_length=255, blank=True)
    vunivola = models.CharField(max_length=255, blank=True)
    dauniyau = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    phone_contact = models.CharField(max_length=255, blank=True)
    vakamacala_tale_eso = models.TextField(blank=True)

    def __str__(self):
        return f"{self.valenilotu}"
    
    class Meta:
        db_table = 'datahub_valenilotu'
        verbose_name_plural = "3. Valenilotu"


class DatahubVeitokani(models.Model):
    id = models.AutoField(primary_key=True)
    veitokani = models.CharField(max_length=255, blank=True)
    valenilotu = models.ForeignKey(DatahubValenilotu, on_delete=models.CASCADE, blank=True, null=True)
    liuliu_ni_veitokani = models.CharField(max_length=255, blank=True)
    vunivola_ni_veitokani = models.CharField(max_length=255, blank=True)
    dauniyau_ni_veitokani = models.CharField(max_length=255, blank=True)
    levu_ni_lavo_bula = models.CharField(max_length=255, blank=True)
    veika_dau_qaravi = models.TextField(blank=True)
    vakamacala_tale_eso = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.veitokani}, {self.valenilotu}"
    
    class Meta:
        db_table = 'datahub_veitokani'
        verbose_name_plural = "4. Veitokani"

class DatahubVeikaeyaco(models.Model):
    id = models.AutoField(primary_key=True)
    veika_e_yaco = models.CharField(choices=ka_e_yaco_Choice, max_length=50, blank=True, help_text='Na ka e yaco e na loma ni Tabacakacaka')
    veika_tale_eso= models.CharField(max_length=255, blank=True)
    valenilotu = models.ForeignKey(DatahubValenilotu, on_delete=models.CASCADE, blank=True, null=True)
    veika_e_vakayacori = models.TextField(blank=True)
    vakamacala_tale_eso = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.veika_e_yaco}, {self.valenilotu}, {self.created_at}"
    
    class Meta:
        db_table = 'datahub_veika_e_yaco'
        verbose_name_plural = "5. Na Veika e Yaco"
