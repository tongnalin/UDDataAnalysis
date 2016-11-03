#!/usr/bin/env python2
"""
This is Docstring
"""

# Analyze data in pure python first
from datetime import datetime as dt
import unicodecsv


def read_csv(filename):
    """
    read csv data from filename
    """
    with open(filename, 'rb') as csv_file:
        reader = unicodecsv.DictReader(csv_file)
        return list(reader)

ENROLLMENTS = read_csv('enrollments.csv')
DAILY_ENGAGEMENT = read_csv('daily_engagement.csv')
PROJECT_SUBMISSIONS = read_csv('project_submissions.csv')


def parse_date(date):
    """
    Takes a date as a string, and returns a Python datetime object.
    If there is no date given, returns None
    """
    if date == '':
        return None
    else:
        return dt.strptime(date, '%Y-%m-%d')


def parse_maybe_int(i):
    """
    Takes a string which is either an empty string or represents an integer,
    and returns an int or None.
    """
    if i == '':
        return None
    else:
        return int(i)

# Clean up the data types in the enrollments table
for enrollment in ENROLLMENTS:
    enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
    enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
    enrollment['is_canceled'] = enrollment['is_canceled'] == 'True'
    enrollment['is_udacity'] = enrollment['is_udacity'] == 'True'
    enrollment['join_date'] = parse_date(enrollment['join_date'])

for engagement_record in DAILY_ENGAGEMENT:
    engagement_record['lessons_completed'] = int(float(engagement_record['lessons_completed']))
    engagement_record['num_courses_visited'] = int(float(engagement_record['num_courses_visited']))
    engagement_record['projects_completed'] = int(float(engagement_record['projects_completed']))
    engagement_record['total_minutes_visited'] = float(engagement_record['total_minutes_visited'])
    engagement_record['utc_date'] = parse_date(engagement_record['utc_date'])

for submission in PROJECT_SUBMISSIONS:
    submission['completion_date'] = parse_date(submission['completion_date'])
    submission['creation_date'] = parse_date(submission['creation_date'])

for de in DAILY_ENGAGEMENT:
    de['account_key'] = de.pop('acct')

ENROLLMENT_NUM_ROWS = len(ENROLLMENTS)
UNIQUE_ENROLLMENTS = set([x["account_key"] for x in ENROLLMENTS])
ENROLLMENT_NUM_UNIQUE_STUDENTS = len(UNIQUE_ENROLLMENTS)
print ENROLLMENT_NUM_ROWS, ENROLLMENT_NUM_UNIQUE_STUDENTS

ENGAGEMENT_NUM_ROWS = len(DAILY_ENGAGEMENT)
UNIQUE_DAILY_ENGAGEMENT = set([x["account_key"] for x in DAILY_ENGAGEMENT])
ENGAGEMENT_NUM_UNIQUE_STUDENTS = len(UNIQUE_DAILY_ENGAGEMENT)
print ENGAGEMENT_NUM_ROWS, ENGAGEMENT_NUM_UNIQUE_STUDENTS

SUBMISSION_NUM_ROWS = len(PROJECT_SUBMISSIONS)
UNIQUE_PROJECT_SUBMISSIONS = set([x["account_key"] for x in PROJECT_SUBMISSIONS])
SUBMISSION_NUM_UNIQUE_STUDENTS = len(UNIQUE_PROJECT_SUBMISSIONS)
print SUBMISSION_NUM_ROWS, SUBMISSION_NUM_UNIQUE_STUDENTS

SURPRISING_RECORDS = []
for item in ENROLLMENTS:
    if item['account_key'] not in UNIQUE_DAILY_ENGAGEMENT:
        SURPRISING_RECORDS.append(item)
        if not item['cancel_date'] == item['join_date']:
            print item
