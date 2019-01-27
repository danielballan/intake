import pandas
import numpy

TEST_CATALOG = """
sources:
  stuff:
    driver: csv
    args: # passed to the open() method
      urlpath: '/tmp/data_file.csv'
      csv_kwargs:
        blocksize: 1000000
"""

N = 1000000
data_file = '/tmp/data_file.csv'
pandas.DataFrame({k: numpy.ones(N) for k in 'abcde'}).to_csv(data_file)
cat_file = '/tmp/benchmark_cat.yml'
with open(cat_file, 'w') as f:
    f.write(TEST_CATALOG)
TEST_CATALOG_PATH = cat_file
