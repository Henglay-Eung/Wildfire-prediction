TP data:

- Download:
    - 2015.csv: TP Data from https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc:C00861
    - ghcnd-stations.csv: Station data
    - cb_2022_us_county_500k: For finding FIPS by Latitude and Longitude
- Run: 
    - Run preprocess/tp/filter_us_tp.py to filter for US tp data
    - Run datasets/tp/filter_us_stations to filter for US stations
    - Run preprocess/tp/add_lat_long_to_tp.py to add latitude and longitude to TP data
    - Run preprocess/tp/add_fips_to_tp.py to add FIPS to TP data

Wind data:

- Download:
    - uwnd.sig995.2015.nc and vwnd.sig995.2015.nc: Wind data from https://downloads.psl.noaa.gov/Datasets/ncep.reanalysis/Dailies/surface/

- Run: 
    - Run preprocess/wind/extract_u_v_and_calculate_wind_speed.py to extract u and v wind and calculate wind speed 
    - Run preprocess/wind/add_fips_to_wind.py to add fips to Wind data
    - Run preprocess/wind/filter_data_without_fips.py to filter data that does not contain fips

Fuel data:

- Download:
    - field_sample.csv: Fuel data from https://fems.fs2c.usda.gov/download
    - site_metadata.csv: Fuel data from https://fems.fs2c.usda.gov/download for adding site latitude and longitude
- Run: 
    - Run preprocess/fuel/filter_fuel.py to filter unneccessary data
    - Run preprocess/fuel/add_lat_long_fuel.py to add lat and long to fuel data
    - Run preprocess/fuel/add_fips_fuel.py to add fips to fuel data