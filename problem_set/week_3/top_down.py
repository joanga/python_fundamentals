def get_month_season(month):
    '''
    Input:  Str - Abbreviation of month
    Output: Str - Season of inputted month
    '''
    season = none
    if month == 'jan' or month == 'feb' or month == 'dec':
        season = 'winter'
    elif month == 'mar' or month == 'apr' or month == 'may':
        season = 'spring'
    elif month == 'mar' or month == 'apr' or month == 'may':
        season = 'fall'
    elif month == 'mar' or month == 'apr' or month == 'may':

get_month_season('february')

def month_info(month, category):
    '''
    Input:  Str - Abbreviation of month, Str - information category to get for month
    Output: Str - category information for the specified month

    Categories supported: 'full name'   ex: month_info('jan', 'full_name') -----> 'January'
                          'num_month'   ex: month_info('may', 'num_month') ----->  5
                          'birth_stone' ex: month_info('jul', 'birth_stone') ---> 'Ruby'
                          'season'      ex: month_info('oct', 'season') --------> 'Fall'
    '''
    full_names = {'jan': 'January', 'feb': 'February', 'mar': 'March', 'apr': 'April',
                  'may': 'May', 'jun': 'June', 'jul': 'July', 'aug': 'August',
                  'sep': 'September', 'oct': 'October', 'nov': 'November', 'dec': 'December'}

    month_nums = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
                  'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12}

    birth_stones = {'jan': 'Garnet', 'feb': 'Amethyst', 'mar': 'Aquamarine', 'apr': 'Diamond',
                    'may': 'Emerald', 'jun': 'Pearl', 'jul': 'Ruby', 'aug': 'Peridot',
                    'sep': 'Sapphire', 'oct': 'Opal', 'nov': 'Topaz', 'dec': 'Turquoise'}

    # Depending on the category get information about month from correct source and return
    pass
