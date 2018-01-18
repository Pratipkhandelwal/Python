#### Final code for the working 

names = []
years = []
imdb_ratings = []
metascores = []
votes = []

start_time = time()
requests = 0

for year_url in years_url :
    for page in pages:
        
        response = get( 'http://www.imdb.com/search/title?release_date='+ year_url +'&sort=num_votes,desc&page='+page, headers=headers)
        
        
        sleep(randint(8,15))
        
        #Monitor 
        requests += 1
        elapsed_time = time() - start_time
        print('Request: {}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
        clear_output(wait=True)
        
        #Warning for non 200 status
        
        if response.status_code!=200:
            warn('Request: {}: Status code: {}'.format(requests),response.status_code)
        
        if requests > 40 :
            warn("Number of requests greater than expected")
            break
            
        page_html = BeautifulSoup (response.text,'html.parser')
        
        mv_containers = page_html.find_all('div',class_='lister-item mode-advanced')
        
        for container in mv_containers:
            
            if container.find('div',class_='ratings-metascore') is not None:
        
               name = container.h3.a.text
               names.append(name)
        
               year = container.h3.find('span',class_='lister-item-year text-muted unbold')
               years.append(year.text)
        
               imdb_rating = float(container.strong.text)
               imdb_ratings.append(imdb_rating)
        
               metascore = container.find('span',class_='metascore').text
               metascores.append(int(metascore))
        
               vote = container.find('span', attrs = {'name':'nv'})
               votes.append(int(vote['data-value']))
        
    
            
            
        
