# NLP_Project1

## Authors
Emily Qiao, Lexi Ryan, and Yuchao Wang

## Description
This program generates a list of presenters, hosts, nominees, awards, and winners from a dataset of tweets about the golden globes from a given year. Additionally, it provides information about the red carpet from that year.

The program outputs this information in two ways: a human-readable format and a json. The json does not use our self-generated awards, but the given awards. The awards we generated can be seen in the human-readable output.

## Usage
run `pip install -r requirements.txt`

To see human readable format, run `python gg_api.py <year>` with the year of your data. The results will be printed to standard output (including red carpet) and to a .txt file "HumanRead.txt" (excluding red carpet).

## Execution Time
On Lexi's laptop, the autograder runs in 1:30 for 2013 and 5:00 for 2015 without the red carpet information.
Note: red carpet is not fully optimized. For best results on gg_api, use a smaller dataset or comment out the red carpet section.
