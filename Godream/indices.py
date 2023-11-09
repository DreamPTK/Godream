import numpy as np
import rasterio
from rasterio.transform import from_origin
from rasterio import crs
from Godream.convertool import xarray_ds


# function to calculate index from bands
def cal_indinces(tiff_path, index=None, output_path=None):
    
    ds = xarray_ds(tiff_path)
    
    index_dict = {
    
    # Normalised Difference Vegation Index 
    'NDVI': lambda ds: (ds.band_4 - ds.band_1)/
                       (ds.band_4 + ds.band_1),
                        
    # Normalised Difference Vegation Index
    'GNDVI': lambda ds: (ds.band_4 - ds.band_2) /
                        (ds.band_4 + ds.band_2), 
                        
    # Difference vegetation index  
    'DVI': lambda ds: (ds.band_4 - ds.band_1),  
                        
    # Leaf Area Index
    'LAI': lambda ds: (3.618 * ((2.5 * (ds.band_4 - ds.band_1)) /
                       (ds.band_4 + 6 * ds.band_1 -
                       7.5 * ds.band_3 + 1)) - 0.118),  
    
    # Ratio vegetation Index
    'RVI': lambda ds: (ds.band_4) /
                      (ds.band_1), 
                      
    # Soil Adjusted Vegetation Index
    'SAVI': lambda ds: ((1.5 * (ds.band_4 - ds.band_1)) /
                       (ds.band_4 + ds.band_1 + 0.5)), 
    
    # Modified Soil Adjusted Vegetation Index
    'MSAVI': lambda ds: ((2 * ds.band_4 + 1 - 
                        ((2 * ds.band_4 + 1)**2 - 
                         8 * (ds.band_4 - ds.band_1))**0.5) / 2), 
    
    # Normalised Difference Water Index
    'NDWI': lambda ds: (ds.band_2 - ds.band_4) /
                       (ds.band_2 + ds.band_4), 
                       
    # Enhanced Vegetation Index
    'EVI': lambda ds: ((2.5 * (ds.band_4 - ds.band_1)) /
                        (ds.band_4 + 6 * ds.band_1 -7.5 * ds.band_3 + 1)),
    
    # Burn Area Index
    'BAI': lambda ds: (1.0 / ((0.10 - ds.band_1) ** 2 +
                       (0.06 - ds.band_4) ** 2)) 
        
}   

    # Check if the specified index is in the dictionary
    if index is not None and index in index_dict:
        # Calculate the specified band index
        calculated_index = index_dict[index](ds)
        
        # Export the result as a GeoTIFF
        if output_path:
            export_as_geotiff(calculated_index, tiff_path, output_path)
        
        # convert xarray to numpy array
        return calculated_index.values
    else:
        # If no index is specified or the specified index is not found, return None
        return None
    
# func tion to export band index data as a GeoTIFF file.   
def export_as_geotiff(data, input_tiff_path, output_geotiff_path):

    with rasterio.open(input_tiff_path) as src:
        # Get the metadata from the input TIFF file
        profile = src.profile
        transform = from_origin(src.bounds.left, src.bounds.top, src.res[0], src.res[1])
        
        # Update the profile with the data type, count, and compression
        profile.update(
            dtype=rasterio.float32,  # Change the data type as needed
            count=1,                # Number of bands
            compress='lzw'          # Compression method (you can change this)
        )

        # Write the data to the output GeoTIFF file
        with rasterio.open(output_geotiff_path, 'w', **profile) as dst:
            dst.write(data, 1)  # Write the data to the first band