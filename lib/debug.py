#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

def magazine_summary(magazine):
    print(f"{magazine.name} Magazine ")
    print(f"{magazine.category} Category")
    print(f"{magazine.name} Authors: ", [author.name for author in magazine.authors()])
    print(f"{magazine.name} articles: ", [article.title for article in magazine.articles()])
    

def author_summary(author):
    print(f"{author.name}")
    print(f"Articles: ", [article.title for article in author.articles()])
    print(f"Publishing Magazines: ", [magazine.name for magazine in author.magazines()])
    print(f"Magazine Categories: {author.topic_areas()}")
   

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    author1 = Author("Martin Shein")
    author2 = Author("Jonathan Ian") 
    author3 = Author("Noella Sky")
    author4 = Author("Murphy Steve")


    magazine1 = Magazine("TechToday", "Tech")
    magazine2 = Magazine("SmartReads", "Education")
    magazine3 = Magazine("UrbanLiving", "Lifestyle")
    magazine4 = Magazine("NaturalLiving", "Health")
    magazine5 = Magazine("GlobalWatch", "News")
    magazine6 = Magazine("CultureCore", "Art")


    article1 = Article( author1, magazine1, "The Future of Quantum Computing")
    article2 = Article( author4, magazine2, "AI and the Job Market Shift")
    article3 = Article( author3, magazine4, "Cybersecurity in 2025")
    article4 = Article( author1, magazine5, "Modern Tools for Remote Learning")
    article5 = Article( author2, magazine2, "Why Coding Should Be Taught Early")
    article6 = Article( author1, magazine6, "Reimagining Higher Education")
    article7 = Article( author1, magazine3, "10 Small Apartment Hacks That Work")
    article8 = Article( author3, magazine6, "The Rise of Smart Cities")
    article9 = Article( author3, magazine1, "Minimalist Living in a Big City")
    article10 = Article( author4, magazine3, "Holistic Remedies That Actually Help")
    article11 = Article( author2, magazine6, "Clean Eating for a Balanced Life")
    article12 = Article( author4, magazine4, "Benefits of a Plant-Based Diet")
    article13 = Article( author3, magazine2, "Geopolitics in the Post-Pandemic Era")
    article14 = Article( author3, magazine3, "Climate Policy in Global Talks")
    article15 = Article( author4, magazine5, "How Tech Impacts Free Speech")
    article16 = Article( author1, magazine6, "Modern Art in the Digital Age")
    article17 = Article( author2, magazine4, "Street Art as Political Expression")
    article18 = Article( author2, magazine6, "The Return of Analog Photography")


    author_summary(author1)
    author_summary(author2)
    author_summary(author3)
    author_summary(author4)


    magazine_summary(magazine1)
    magazine_summary(magazine2)
    magazine_summary(magazine3)
    magazine_summary(magazine4)
    magazine_summary(magazine5)
    magazine_summary(magazine6)


    print("Top publisher: ", Magazine.top_publisher().name if Magazine.top_publisher else None)

    # don't remove this line, it's for debugging!
    ipdb.set_trace()
