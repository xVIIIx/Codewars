def domain_name(url):
    if url.count('.')==2:
        return url[url.find('.')+1:url.rfind('.')]
    else:
        return url[url.rfind('/')+1:url.rfind('.')]
