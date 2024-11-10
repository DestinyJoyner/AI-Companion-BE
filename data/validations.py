from .keywords import keywords

def validate_relevance (prompt):
    # keywords_found = 0
    
    for word in keywords:
        if word in prompt:
            # keywords_found += 1
            return True
    # if keywords_found > 0:
    #     return True
    return False