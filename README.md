## build
```
make init # destroy and build
make build # build fresh dependencies

# when DAY and YEAR are not set it should default to today
make day DAY=1 YEAR=2022 # create a workdir from template for DAY and YEAR
make run DAY=1 YEAR=2022 # run code for the DAY and YEAR
make in DAY=1 YEAR=2022 # get input for DAY and YEAR
make what # show the DAY and YEAR environment variable values
```
