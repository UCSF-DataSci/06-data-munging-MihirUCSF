# Data Cleaning Project: Population Dataset

## 1. Initial State Analysis

### Dataset Overview
- **Name**: messy_population_data.csv
- **Rows**: each row is an individual
- **Columns**: there are 5 columns: income_group, age, gender, year, and population 

### Column Details
#### Data Info
Data columns (total 5 columns):
    Column         Non-Null Count   Dtype 
---  ------         --------------   ----- 
 0   income_groups  122008 non-null  object
 1   age            122008 non-null  int64 
 2   gender         122008 non-null  int64 
 3   year           122008 non-null  int64 
 4   population     122008 non-null  int64 
dtypes: int64(4), object(1)

#### Data Statistics
       income_groups            age         gender           year    population
count         122008  122008.000000  122008.000000  122008.000000  1.220080e+05
unique             4            NaN            NaN            NaN           NaN
top      high_income            NaN            NaN            NaN           NaN
freq           30502            NaN            NaN            NaN           NaN
mean             NaN      50.000000       1.500000    2025.000000  9.235068e+06
std              NaN      29.154879       0.500002      43.589168  8.492751e+06
min              NaN       0.000000       1.000000    1950.000000  2.100000e+01
25%              NaN      25.000000       1.000000    1987.000000  2.221932e+06
50%              NaN      50.000000       1.500000    2025.000000  7.042608e+06
75%              NaN      75.000000       2.000000    2063.000000  1.392130e+07
max              NaN     100.000000       2.000000    2100.000000  3.432180e+07
Series([], dtype: int64)
Duplicate rows: 0

#### Value Counts
income_groups
high_income            30502
low_income             30502
lower_middle_income    30502
upper_middle_income    30502
Name: count, dtype: int64
age
0      1208
1      1208
10     1208
100    1208
11     1208
       ...
95     1208
96     1208
97     1208
98     1208
99     1208
Name: count, Length: 101, dtype: int64
gender
1    61004
2    61004
Name: count, dtype: int64
year
1950    808
1951    808
1952    808
1953    808
1954    808
       ...
2096    808
2097    808
2098    808
2099    808
2100    808
Name: count, Length: 151, dtype: int64
population
189        5
105        5
546        5
186        5
66         5
          ..
1468082    1
1570130    1
1609130    1
1631977    1
7816237    1
Name: count, Length: 120781, dtype: int64

#### Unique Values
     Column Name  Unique Count
0  income_groups             4
1            age           101
2         gender             2
3           year           151
4     population        120781

### Identified Issues

1. **Error in Age Column**
   - Description: there are data points with age '0' which don't make sense and are invalid. We do not know whether some of these values are supposed to be categorical labels. 
   - Affected Column(s): age
   - Example: the first 300 rows in the data set have '0' as the age value 
   - Potential Impact: will skew the data and can create an eror in analysis/graphs

2. **Gender Column**
   - Without the codebook, we have to assume the '1' indicates male and '2' indicates female
   - Affected Column: gender
   - Impact: this variable must be categorized as a categorical variable not numerical
     
3. **Year Column**
   - Without the codebook, it is unknown what this variable is referring to, whether it means birth year or when the data was taken from the income group. There are also future years with data (it's impossible to have gender and age data for future years), again we do not know what these data points mean. 
   - Affected Column: year
   - Example: any year after 2024 with population, age, and gender data 
   - Impact: the years in the future need to cleaned
     
4. **Population Column**
   - Again, without the codebook it is unclear what the population is exactly counting, we are not given an area or location.  
   - Affected Column: population 
   - Impact: due to its ambiguity, it may not provide useful data analysis
    
2. **General Observations**
   - Using descriptive statistics on categorical variables don't make sense due to the results being invalid, these only work for numerical variables.
   - There are 0 duplicated rows


## 2. Data Cleaning Process

### Issue 1: Age Column
- **Cleaning Method**: remove all ages with '0' as the data
- **Implementation**:
  ```python
  clean_df = df[df['age'] != 0]
  ```
- **Justification**: having an age of '0' does not make sense
- **Impact**: 
  - Rows affected: 1,208 rows removed  
  - Data distribution change: reduces the data from removing the rows with age '0'

### Issue 2: Gender Column
- **Cleaning Method**: convert the values '1' to 'male' and '2' to 'female'
- **Implementation**:
  ```python
  clean_df = df['gender'] = df['gender'].replace({1: 'male', 2: 'female'})
  ```
- **Justification**: 1 and 2 in gender column is ambiguous so add labels to better define the variable  
  
### Issue 3: Year Column
- **Cleaning Method**: remove all years after 2024 
- **Implementation**:
  ```python
  clean_df = df[df['year'] <= 2024]
  ```
- **Justification**: we are assuming it is impossible to have future data with the information we are given (since we are not given a codebook, we do not know what the variable 'year' is referring to)
- **Impact**: 
  - Rows affected:  61,408 rows removed  
  - Data distribution change: reduces the data from removing the rows with a year greater than '2024'

## 3. Final State Analysis

### Dataset Overview
- **Name**: "C:/Users/mihir/OneDrive/Desktop/clean_population_data.csv"
- **Rows**: same as original with the **removal** of all ages equal to 0, conversion of 1 and 2 to 'male' and 'female' respectively, and years after 2024 
- **Columns**: income_groups, age, gender, year, population

### Column Details
#### Data columns (total 5 columns):
    Column         Non-Null Count  Dtype
---  ------         --------------  -----
 0   income_groups  60000 non-null  object
 1   age            60000 non-null  int64
 2   gender         60000 non-null  object
 3   year           60000 non-null  int64
 4   population     60000 non-null  int64
dtypes: int64(3), object(2)

      income_groups           age gender          year    population
count          60000  60000.000000  60000  60000.000000  6.000000e+04
unique             4           NaN      2           NaN           NaN
top      high_income           NaN   male           NaN           NaN
freq           15000           NaN  30000           NaN           NaN
mean             NaN     50.500000    NaN   1987.000000  6.277242e+06
std              NaN     28.866311    NaN     21.648891  7.000100e+06
min              NaN      1.000000    NaN   1950.000000  2.100000e+01
25%              NaN     25.750000    NaN   1968.000000  8.064298e+05
50%              NaN     50.500000    NaN   1987.000000  4.200848e+06
75%              NaN     75.250000    NaN   2006.000000  8.135359e+06
max              NaN    100.000000    NaN   2024.000000  3.383587e+07

Value Counts for Categorical Columns:
Value counts for 'income_groups':
income_groups
high_income            15000
low_income             15000
lower_middle_income    15000
upper_middle_income    15000
Name: count, dtype: int64

Value counts for 'gender':
gender
male      30000
female    30000

     Column Name  Unique Count
0  income_groups             4
1            age           100
2         gender             2
3           year            75
4     population         59176


### Summary of Changes
- All age values equal to '0' have been removed
- Gender column has been renamed from '1' and '2' to 'male' and 'female' respectively
- All years after 2024 have been removed (future years)
- Removal of rows results in reduced unique value counts, the year statistics have changed, and the mean population changed as well.
- As stated in the beginning, more info is needed from the codebook as to what the variables are exactly referring to, as a result we have to assume the meaning. 
