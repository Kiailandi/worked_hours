# :computer: worked_hours :hourglass:
A simple script to calculate the total number of hours worked (and money earned) based on a timetable.

## Configuration file :wrench:

The configuration can be passed to the script via a configuration file called `config.json`. An example can be found in this repo.

### Options:

- `input_file` is the name of the timetable file
- `time_format` is the time format you use in the input file [HH:MM]
- `time_separator` is the separator between the starting time and the ending time for the time frame [HH:MM-HH:MM]
- `date_separator` is the separator you want to use to separate day date from time frame
- `stage` is an object you can use if you are doing an unpaid stage for University
  - `active` is used if your are working for a curricular stage for you uni which is worth credits instead of money
  - `CFU_needed` is the number of CFU you need to complete the stage
  - `CFU_hours` is the number of hours each credit is worth [an EU credit is 25h]
- `currency_symbol` is the symbol you want to use as currency
- `hour_pay` is how much you earn in an hour
- `hours_day_fulltime` is the number of hours you consider a fulltime day of work

### Example:

```
{
  "input_file": "input.txt",
  "time_format": "%H:%M",
  "time_separator": "-",
  "date_separator": " ",
  "stage": {
    "active": true,
    "CFU_needed": 9,
    "CFU_hours": 25
  },
  "currency_symbol": "€",
  "hour_pay": 10,
  "hours_day_fulltime": 8
}
```

## Input file :watch:

Each line represents a frame of time, if you have multiple frames in a single day each one should be on a different line. An example can be found in this repo as `input.txt`.

### Example:

```
14/02 09:00-18:00
15/02 10:00-13:00
15/02 14:00-18:00
```

NB: ' ', ':', '-' are the date / time separators and are declared in the config file.

## TODO (wip) :construction:

- [ ] Use better terms in config file
- [ ] Add a check to avoid the same separator for different thing
- [ ] Add error handling
- [ ] Publish on PyPI
