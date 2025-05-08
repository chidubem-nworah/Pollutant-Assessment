import sys


header_skipped = False


for line in sys.stdin:
    # Skipping the header row
    if not header_skipped:
        header_skipped = True
        continue
    
    # Splitting the line into columns
    columns = line.strip().split(',')
    
    # Extracting relevant columns
    country = columns[0]
    co_aqi_value = columns[4]
    ozone_aqi_value = columns[6]
    no2_aqi_value = columns[8]
    pm25_aqi_value = columns[10]

    # Emitting key-value pairs for each pollutant
    print(f"{country}\tCO,{co_aqi_value}")
    print(f"{country}\tO3,{ozone_aqi_value}")
    print(f"{country}\tNO2,{no2_aqi_value}")
    print(f"{country}\tPM2.5,{pm25_aqi_value}")


