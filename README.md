## Edgar 13F Data Parser

Script that extracts 13F data for a given company using their CIK id.

#### Requirements

You will need Selenium (configured for Chrome) to use this script.

#### Step 1 - Setup

Clone the repository: `$ git clone https://github.com/rodcoelho/edgar_parser.git`

#### Step 2 - Configure

1) In `selenium_parser/work.py`, configure line 13 to add CIKs for companies of interest.

2) In `selenium_parser/writeout.py`, configure line 5 so that the data payloads land in the `selenium_parser/output/` directory.

3) In `selenium_parser/work.py` change the `executable_path` to your chromedriver's path.

#### Step 3 - Run!

`$ ./run.sh`