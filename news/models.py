from django.db import models
import datetime as dt 

# details of the Person writing the news article
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)
    
    def __str__(self): 
        return self.first_name

    class Meta:
        ordering = ['first_name']

    def save_editor(self):
        self.save()



# details about different tags contained in an Article 
class Tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
    
    def save_tag(self):
        self.save() 


# details concerning a news Article
class Article(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    editor = models.ForeignKey('Editor', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags) 
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to = 'articles/') 
    
    
    def __str__(self):
        return self.title
    
    def save_article(self):
        self.save()

    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date = today)
        return news

    @classmethod
    def days_news(cls,date):
        news = cls.objects.filter(pub_date__date = date)
        return news
    
    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains = search_term)
        return news
