import scrapy


class DesafioSpider(scrapy.Spider):
    name = "desafio"
    start_urls = [
        'https://www.reddit.com/r/all/top/',
    ]
    lista = []
    lista_telegram = []
    dicionario = {}

    def parse(self, response):
        
        for desafio in response.css('div.thing'):
            score = desafio.css('div.score.likes::text').extract_first()
            if score[-1] == 'k':
                score = float(score[0:-1]) * 1000
            else:
                score = float(score)

            if score >= 5000:
                self.dicionario = {                
                    'upvotes': desafio.css('div.score.likes::text').extract_first(),
                    'subreddit': desafio.css('a.subreddit.hover.may-blank::text').extract(),
                    'title': desafio.css('a.title.may-blank::text').extract_first(),
                    'comments': desafio.css('a.bylink.comments.may-blank::attr(href)').extract(),
                }

                self.lista.append(self.dicionario)
                self.lista_telegram.append(self.dicionario['subreddit'])

                #print(lista)
                yield self.dicionario


        next_page = response.css('span.next-button a::attr(href)').extract_first()

        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


        for item in range(len(self.lista)):
            arquivo = open('scrapylist.txt', 'a')
            arquivo.write(str(self.lista[item]) + '\n')
            arquivo.close()

            arquivo = open('scrapylist_telegram.txt', 'a')
            arquivo.write(str(self.lista_telegram[item]) + '\n')
            arquivo.close()

    def getLista():
        return self.lista

    
    
'''
    def FormatScoreLikes(score):
            if score[-1] == 'k':
                score = float(score[0:-1]) * 1000
                return score
            else:
                return float(score)
'''
        

