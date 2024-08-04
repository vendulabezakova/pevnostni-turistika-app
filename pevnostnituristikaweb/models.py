from django.db import models

class Museum(models.Model):
    location_choices = (
        ("JČ", "Jihočeský"),
        ("JM", "Jihomoravský"),
        ("KH", "Královéhradecký"),
        ("LB", "Liberecký"),
        ("MK", "Moravskoslezský"),
        ("OL", "Olomoucký"),
        ("PA", "Pardubický"),
        ("PJ", "Plzeňský"),
        ("PR", "Praha"),
        ("ST", "Středočeský"),
        ("UT", "Ústecký"),
        ("EV", "Evropa")
    )

    name = models.CharField(max_length=100)
    location = models.CharField(max_length=2, default="JČ", choices=location_choices)
    web = models.CharField(max_length=50, null=True, blank=True)

class Route(models.Model):
    location_choices = (
        ("JČ", "Jihočeský"),
        ("JM", "Jihomoravský"),
        ("KH", "Královéhradecký"),
        ("LB", "Liberecký"),
        ("MK", "Moravskoslezský"),
        ("OL", "Olomoucký"),
        ("PA", "Pardubický"),
        ("PJ", "Plzeňský"),
        ("PR", "Praha"),
        ("ST", "Středočeský"),
        ("UT", "Ústecký"),
        ("EV", "Evropa")
    )

    difficulty_choices = (
        ("EA", "Snadná"),
        ("MD", "Středně náročná"),
        ("HD", "Náročná")
    )

    location = models.CharField(max_length=2, default="JČ", choices=location_choices)
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=2, default="EA", choices=difficulty_choices)