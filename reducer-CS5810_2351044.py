import sys

current_country = None
total_aqi = {'CO': 0, 'O3': 0, 'NO2': 0, 'PM2.5': 0}
count = 0


for line in sys.stdin:
    # Resolving the mapper output
    country, pollutant_aqi = line.strip().split('\t')
    pollutant, aqi_value = pollutant_aqi.split(',')
    
    # Converting AQI value to a floating point number
    aqi_value = float(aqi_value)
    
    # Initializing for country
    if current_country is None:
        current_country = country
    
    # Calculating average AQI for each pollutant when the country changes
    if current_country != country:
        
        avg_aqi = {pollutant: total_aqi[pollutant] / count for pollutant in total_aqi}
        
        # Determining the predominant pollutant
        predominant_pollutant = max(avg_aqi, key=avg_aqi.get)
        
        # Printing the country name and its predominant pollutant
        print(f"{current_country} {predominant_pollutant}")
        
        # Resetting the variables for the next country
        current_country = country
        total_aqi = {'CO': 0, 'O3': 0, 'NO2': 0, 'PM2.5': 0}
        count = 0
    
    # Accumulating the AQI value for each pollutant
    total_aqi[pollutant] += aqi_value
    count += 1

# Processing the last country
if current_country is not None:
    # Calculating the average AQI for each pollutant for the last one
    avg_aqi = {pollutant: total_aqi[pollutant] / count for pollutant in total_aqi}
    
    # Determining the predominant pollutant for the last one
    predominant_pollutant = max(avg_aqi, key=avg_aqi.get)
    
    # Print the country name along with the predominant pollutant
    print(f"{current_country} {predominant_pollutant}")
