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
   - Without the codebook, it is unknown what this variable is referring to, whether it means birth year or when the data was taken from the income group. There are also future years with data, again we do not know what these data points mean. 
   - Affected Column: year
   - Example: any year after 2024 with population, age, and gender data 
   - Impact: the years in the future need to cleaned
     
2. **Population Column**
   - Again, without the codebook it is unclear what the population is exactly counting, we are not given an area or location.  
   - Affected Column: population 
   - Impact: due to its ambiguity, it may not provide useful data analysis  

## 2. Data Cleaning Process

### Issue 1: [Issue Name]
- **Cleaning Method**: [Describe your approach]
- **Implementation**:
  ```python
  # Include relevant code snippet
  ```
- **Justification**: [Explain why you chose this method]
- **Impact**: 
  - Rows affected: [Number]
  - Data distribution change: [Describe any significant changes]

### Issue 2: [Next Issue]
- ...


## 3. Final State Analysis

### Dataset Overview
- **Name**: cleaned_population_data.csv (or whatever you named it)
- **Rows**: [Your answer]
- **Columns**: [Your answer]

### Column Details
| Column Name | Data Type | Non-Null Count | #Unique Values |  Mean  |
|-------------|-----------|----------------|----------------|--------|
| [Column 1]  | [Type]    | [Count]        | [#Unique]      | [Mean] |
| ...         | ...       | ...            | ...            | ...    |

### Summary of Changes
- [List major changes made to the dataset]
- [Discuss any significant changes in data distribution]
