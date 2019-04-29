current = { 'temperature': 67.2,
            'precib_prob': '40%',
            'location': {
             'city': 'London',
            'country' : 'UK'
                }
            }

loc = current['location']
print ( 'In',
        loc['city'] + ', ' + loc['country'],
        'it is',
        current['temperature'], 'degrees')