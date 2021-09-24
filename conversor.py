import netCDF4
import pandas as pd
import xarray as xr
import os

from IPython.display import display, HTML

local_storage_directory = 'conversor/dados/'
netcdf_dir = local_storage_directory + 'netcdf/'
csv_dir = local_storage_directory + 'csv/'

netcdf_file_name = 'global-analysis-forecast-phy.nc'

netcdf_file_in = netcdf_dir + netcdf_file_name
csv_file_out = csv_dir + netcdf_file_name[:-3] + '.csv'

ds = xr.open_dataset(netcdf_file_in)
df = ds.to_dataframe()

df.to_csv(csv_file_out)
print(df)
files_to_convert = local_storage_directory + 'netcdf/'
print(files_to_convert)

for filename in os.listdir(files_to_convert):
  ds = xr.open_dataset(files_to_convert + filename)
  df = ds.to_dataframe()
  df.to_csv(csv_dir + filename[:-3] + '.csv')
  print (filename + ' has been processed to .csv')
print(df)

csv_uncleaned_in = netcdf_file_name[:-3] + '.csv'
csv_cleaned_out = csv_uncleaned_in[:-4] + '_cleaned.csv'

data = pd.read_csv(csv_dir + csv_uncleaned_in)

print(data.dropna())
data.dropna().to_csv(csv_dir + csv_cleaned_out, index = False)
