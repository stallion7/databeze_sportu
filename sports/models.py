from django.db import models


def sportPath (instance, filename):
    return 'obrazky/' + str(instance.nazev_sportu)+'/img/'+filename


class Udalost(models.Model):
    nazev_akce = models.CharField(verbose_name="Název akce", max_length=45)

    datum_akce = models.DateField(verbose_name="Datum začátku akce")

    misto_konani = models.CharField(max_length=45, verbose_name="Místo konání akce")

    informace = models.TextField(verbose_name="Informace o události")

    class Meta:
        ordering = ['nazev_akce']

    def __str__(self):
        return self.nazev_akce


class Sporty(models.Model):
    nazev_sportu = models.CharField(max_length=45, verbose_name="Název sportu")

    OBDOBI = (
        ("jaro", "Jaro"),
        ("leto", "Léto"),
        ("podzim", "Podzim"),
        ("zima", "Zima")
    )

    obdobi = models.CharField(max_length=10, choices=OBDOBI, verbose_name="Roční období")

    historie = models.TextField(verbose_name="Historie sportu")

    udalosti = models.ManyToManyField(Udalost, verbose_name="Událost")

    obrazek = models.ImageField(upload_to=sportPath, null=True, blank=True, verbose_name='Obrázky')

    class Meta:
        ordering = ['nazev_sportu']

    def __str__(self):
        return self.nazev_sportu


class Hvezdy(models.Model):
    jmeno = models.CharField(max_length=30, verbose_name="Jméno hvězdy")

    prijmeni = models.CharField(max_length=30, verbose_name="Příjmení hvězdy")

    narozeni = models.DateField(verbose_name="Datum narození hvězdy")

    zeme_puvod_sportu_zkratka = models.CharField(max_length=5, verbose_name="Země průvodu zkratka")

    pocet_medaili = models.IntegerField(verbose_name="Počet získaných medailí")

    POHLAVI = (
        ("zena", "Žena"),
        ("muz", "Muž"),
        ("jine", "Jiné")
    )

    pohlavi = models.CharField(max_length=5, verbose_name="Pohlaví", choices=POHLAVI)

    kariera = models.TextField(verbose_name="Kariéra")

    sport_nazev = models.ForeignKey(Sporty, on_delete=models.CASCADE, verbose_name="Sport")

    class Meta:
        ordering = ['prijmeni', 'jmeno']

    def __str__(self):
        return f"{self.prijmeni} {self.jmeno}"
