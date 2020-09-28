from django.db import models

class Music(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    time = models.CharField(max_length=22)
    
    
    class Meta:
        verbose_name = "music"
        ordering = ['auteur']
    
    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard dans l'administration
        """
        return self.titre