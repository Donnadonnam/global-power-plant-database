#  """
#  A library to support open-source power sector data.
#  
#  import argparse
#  import urllib				# necessary because requests doesn't handle FTP
#  import csv
#  import os
#  import re

#  Folder directories
#  RAW_DIR = os.path.join(ROOT_DIR, "raw_source_files")
#  SOURCE_DB_BIN_DIR = os.path.join(ROOT_DIR, "source_databases")
#  OUTPUT_DIR = os.path.join(ROOT_DIR, "output_database")
#  		"src_csv": SOURCE_DB_CSV_DIR, "root": ROOT_DIR, "output": OUTPUT_DIR}

# Resource files
#  HEADER_NAMES_THESAURUS_FILE		= os.path.join(RESOURCES_DIR, "header_names_thesaurus.csv")
#  COUNTRY_INFORMATION_FILE		= os.path.join(RESOURCES_DIR, "country_information.csv")
#  WEPP_CONCORDANCE_FILE 			= os.path.join(RESOURCES_DIR, "master_wepp_concordance.csv")
#  GENERATION_FILE      			= os.path.join(RESOURCES_DIR, "generation_by_country_by_fuel_2014.csv")

#  Encoding
#  NO_DATA_UNICODE = u""	# used to indicate no data for a Unicode-type attribute in the PowerPlant class
#  NO_DATA_OTHER = None	# used to indicate no data for object- or list-type attribute in the PowerPlant class
#  
#  
#  	"""Class representing a power plant."""
#  		plant_owner=NO_DATA_UNICODE,
#  		plant_capacity=NO_DATA_NUMERIC,
#  		plant_source=NO_DATA_OTHER,
#  		plant_location=NO_DATA_OTHER,
#  		plant_primary_fuel=NO_DATA_UNICODE,
#  		plant_generation=NO_DATA_OTHER,
#  