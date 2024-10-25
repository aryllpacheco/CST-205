#Aryll Pacheco CST205 10/14/24
#Searches through image_info and returns the image that matches the most
from image_info import image_info

def my_search(search_term):
    serach_term = search_term.lower()
    best_match = None 
    max_match = 0

    for image in image_info:
        title = image['title'].lower()
        tags = [tag.lower() for tag in image['tags']] 

        match_count = 0
        if search_term in title:
            match_count +=1
        match_count += tags.count(search_term)

        if match_count > max_match:
            best_match = image['id']
            max_match = match_count

    if best_match:
        return best_match
    else:
        return 'no_results'
        
