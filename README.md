#

## prepare to use

this example to execute this project is only for bash or zsh.

if you are using python on windows, then check for your envienment (maybe for power shell)

```bash
$ python3 -mvenv venv 
$ source venv/bin/activate  
# or 
$ source env/bin/acticate
```

## math functions

There are several packages in this project.

statistic package contains common statistic function but not use standard library. 

( Don't you your product! There are only my experience to use pyhthon. )

### statistic 統計系の関数

statistic package contains following functions.

#### mean : 平均値

get mean for input ata_array

#### median : 中央値

get median for input ata_array

#### variance : 分散
get variance for input data_array

### caoliculus 数値計算系の関数

#### integral 積分

current this package is implemented only simple integral function such y = ax + b

### statistic experimence using real open data 

Previous codes are for basic coding experiences.

Now, I try to analyze data using real public data.

## Testing
```bash
# testing
$ python3 -m unittest discover -s test
```

# experience using open data

For practical experience, I utilize open data from the following site and queries. Although navigating this site can be quite challenging, the real-world open data it offers is invaluable for studying.

Here’s an example of sample data on honey imports: https://www.e-stat.go.jp/stat-search?page=1&query=%E3%81%AF%E3%81%A1%E3%81%BF%E3%81%A4%E3%80%80%E8%BC%B8%E5%85%A5&layout=dataset&metadata=1&data=1
