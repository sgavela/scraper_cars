import scrapy

class CarsSpider(scrapy.Spider):
    name = 'cars'
    start_urls = ['https://www.autocasion.com/coches-ocasion?page=2']

    def parse(self, response):
        for car in response.css('div.contenido-anuncio'):
            yield {
                'brand_and_model': car.css('h2::text').get(),
                'price': car.css('span.price::text').get().replace('€',''),

                'province': car.css('li').getall()[0].replace('<li>Provincia: <span>', '').replace('</span></li>', ''),
                'matriculation': car.css('li').getall()[1].replace('<li>Matriculación: <span>', '').replace('</span></li>', ''),
                'fuel': car.css('li').getall()[2].replace('<li>Combustible: <span>', '').replace('</span></li>', ''),
                'kilometres': car.css('li').getall()[3].replace('<li>Kilómetros: <span>', '').replace('</span></li>', ''),
                'gear': car.css('li').getall()[4].replace('<li>Cambio: <span>', '').replace('</span></li>', ''),
                #'power': car.css('li').getall()[5].replace('<li>Potencia: <span>', '').replace('</span></li>', '')
            }
       
        base_url = 'https://www.autocasion.com'
        next_page = base_url + response.xpath('//div[@class="paginacion"]//a')[1].attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
        