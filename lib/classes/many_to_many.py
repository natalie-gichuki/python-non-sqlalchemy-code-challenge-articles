class Article:

    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def author(self): 
        return self._author 
    
    @author.setter 
    def author(self, value): 
        if not isinstance(value, Author): 
            raise Exception("author must be an instance of Author.")
        
        self._author = value

    
    @property
    def magazine(self): 
        return self._magazine
    
    @magazine.setter 
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise Exception("magazine ,must be an instance of Magazine.")
        
        self._magazine = value


    @property 
    def title(self):
        return self._title 
    
    @title.setter 
    def title(self, value):
        if hasattr(self, '_title'):
            raise Exception("Article title cannot be changed once it has been instantiated.")
        
        if not isinstance(value, str):
            raise Exception("Article title must be a string.")
        
        if len(value) < 5 or len(value) > 50:
            raise Exception("Article title can only be 5 to 50 characters long.")
        
        self._title = value

    #def __repr__(self):
    #    return f"<Article: '{self.title}' by '{self.author.name}' in '{self.magazine.name}'>"

        
        
class Author:
    def __init__(self, name):

        self.name = name

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, value): 
        if hasattr(self, '_name'):
            raise Exception("Author's name cannot be changed once it has been instantiated.")
        
        if not isinstance(value, str):
            raise Exception("Author's name must be a string.")
        
        if len(value) < 1:
            raise Exception("Author's name must be at least 1 character long.")
        
        self._name = value

    def articles(self):
        return [article for article in Article.all if article.author == self]
     

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))
        

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        return list(set(article.magazine.category for article in self.articles()))

class Magazine:

    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)


    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise Exception("Magazine name must be a string.")
        
        if len(new_name) < 2 or len(new_name) > 16:
            raise Exception("Magazine name must be between 2 to 16 characters long.")
        
        self._name = new_name

    
    @property 
    def category(self): 
        return self._category
    
    @category.setter
    def category(self, new_category): 
        if not isinstance(new_category, str): 
            raise Exception("Magazine category must be a string.")
        
        if len(new_category) < 1:
            raise Exception("Magazine category must be at least one character long.")
        
        self._category = new_category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        if not self.articles():
            return None
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        authors = [article.author for article in self.articles()]
        get_total_authors = [author for author in set(authors) if authors.count(author) > 2]
        return get_total_authors if get_total_authors else None
    
    @classmethod
    def top_publisher(cls):
        def article_count(magazine):
            return len(magazine.articles())
        
        if not Article.all:
            return None
        
        return max(cls.all, key = article_count)
