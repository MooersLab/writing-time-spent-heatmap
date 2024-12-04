![Version](https://img.shields.io/static/v1?label=writing-time-spent-heatmap&message=0.1&color=brightcolor)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

# Heatmap of hours spent writing journal articles

## Problem addressed

I wanted an automated way of summing up the effort that I had expended on various writing projects in the form of a heatmap.
I find the heat map of commits to GitHub to be motivating in terms of trying to make frequent commits.
I think I can pick up a similar motivational driving force by generating a heat map of hours spent working on journal articles per day.

![hmj.png](./images/hmj.png)

## Why this is useful?

The heat map reveals periods of time when I have great difficulty getting my daily writing done.
For me this happens, this happens when I am collecting X-ray diffraction data around the clock for several days and preparing multiple presentations concurrently.
This identifies an area where I need to develop better self-regulation mechanisms, like not committing to two talks in the same two-week period.
I can generally persist with my writing schedule through teaching, traveling to attend scientific conferences, attending said conferences, and serving on Grant review panels.

According to [research by Robert Boice in the 1980s](https://www.sciencedirect.com/science/article/abs/pii/0005796789901447), academics who record their writing effort are four times more productive than those who do not.
Those academics who share their writing progress with their colleagues are nine times more productive.

I started my database 2022 May 1. 
I wrote and deployed `hmj.py` in November 2023.
It made a difference in terms of expended effort in 2024 compared to 2023.


## How it works

1. I track time spent on various projects by project number and project directory name in a sqlite database, mytime.db. I view and edit this database with DB Browser for Sqlite.
2. `hmj.py` reads the database file and searches for journal article entries by project number. Mine are in the range of 1 to 999. It sums the hours spent per day and generates the heatmap via matplotlib.
3. A cron job to run `./hmj.py` every morning at 4:00 a.m. I stare at the displayed image and then get back to writing.

## Installation

1. Assign project numbers to projects in a separate database or spreadsheet. I also use these numbers to start the name of project folders on my home directory to ease navigation on the command line. Your home folder can hold over 10,000 files. There is no need to use `Documents`.
2. Edit the file paths in hmj.py to fit your workflow.
3. Install the required Python packages. Take care that matplotlib is not yet being built in Python 3.13. I use Python 3.11. Calmap and calplot will probably have to be installed with pip. It may be best to use a conda or pyenv environment to avoid the Python dependency nightmare.
4. If you wish, set up a cron job to run hmj.py every morning and display the heatmap.

The cron job calls the following zsh alias. I am using a pyenv environment.

```
alias hmj='cd ~/6003TimeTracking/cb && source python311-env/bin/activate && ./python311-env/bin/python3.11 hmj.py && deactivate && echo "Run hmj.py and show total effort as a heatmap."'


## Update history

|Version      | Changes                                                                                                                                  | Date                 |
|:------------|:---------------------------------------------------------------------------------------------------------------------------------------- |:---------------------|
| Version 0.1 |   Added badges, funding, and update table.  Initial commit.                                                                              | 2024 December 4      |

## Sources of funding

- NIH: R01 CA242845
- NIH: R01 AI088011
- NIH: P30 CA225520 (PI: R. Mannel)
- NIH: P20 GM103640 and P30 GM145423 (PI: A. West)

