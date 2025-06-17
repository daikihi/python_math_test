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

## Testing
```bash
# testing
$ python3 -m unittest discover -s test
```
