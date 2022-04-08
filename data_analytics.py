

total = 0
count = 0
year_life_high = 0
year_life_low = 1000
average = 0
lowest_life = 1000
highest_life = 0
lines = int(0)
year_select = int(input('What year would you like to see? '))
country_select = input('Which country would you like to see? ').lower()
print()
with open('life-expectancy.csv') as life_file:
    for line in life_file:
        parts = line.split(',')
        if len(parts) > 0:
            lines +=1 
                
            if lines > 1:
                country = parts[0].strip()
                year = int(parts[2])
                life_expectancy = float(parts[3])

                #finding Lowest
                if life_expectancy < lowest_life:
                    lowest_life = life_expectancy
                    lowest_year = int(parts[2])
                    lowest_country = parts[0]

                #finding highest
                if life_expectancy > highest_life:
                    highest_life = life_expectancy
                    highest_year = int(parts[2])
                    highest_country = parts[0]

                #year select average
                if year == year_select:
                    count += 1
                    total += life_expectancy
                    average = total / count
                    if life_expectancy > year_life_high:
                        year_life_high = life_expectancy
                        country_high = parts[0]
                    if life_expectancy < year_life_low:
                        year_life_low = life_expectancy
                        country_low = parts[0]
                
                #country selection
                if country_select == country.lower():
                    print(f'Country: {country:10} Year: {year}  Life Expectancy: {life_expectancy}')
                
                
                

                     

#results
print()
print(f'Highest Life: {highest_life} Year: {highest_year} country: {highest_country}')
print(f'Lowest Life: {lowest_life} Year: {lowest_year} country: {lowest_country}')
print()

print(f'For year: {year_select}')
print(f'The average life span was {average:.2f}')
print(f'The highest life expentancy was {year_life_high} in {country_high}')
print(f'The lowest life expentancy was {year_life_low} in {country_low}')


