import wikipedia

#print(wikipedia.summary('Python (programming language'))

def print_wikipedia_results(word):
    # searches for pages that match the specified word
    results = wikipedia.search(word)
    for result in results:
        try:
            page = wikipedia.page(result)
        except wikipedia.exceptions.DisambiguationError:
            print('Disambiguation error')
            continue
        except wikipedia.exceptions.PageError:
            print('Page error for result ' + result)
            continue
        print(page.summary)

if __name__ == '__main__':
    page = 'Python (programming language)'
    print(page.title())
    #print(page.url)
    print_wikipedia_results(page)

