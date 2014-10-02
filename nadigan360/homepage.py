import os
from nadigan360.settings import *
from nd360.models import *

os.environ['DJANGO_SETTINGS_MODULE'] = 'nadigan360.settings'



def main():
	news_articles = News_Article.objects.orderby('dateCreated')

	print news_articles






if __name__ == "__main__":
	main()



