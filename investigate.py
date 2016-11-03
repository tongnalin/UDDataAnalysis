#!/usr/bin/python3

# Analyze data in pure python first

import unicodecsv

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

enrollments = read_csv('enrollments.csv')
daily_engagements = read_csv('daily_engagement.csv')
project_submissions = read_csv('project_submissions.csv')

from datetime import datetime as dt

# Takes a date as a string, and returns a Python datetime object. 
# If there is no date given, returns None
def parse_date(date):
    if date == '':
        return None
    else:
        return dt.strptime(date, '%Y-%m-%d')
    
# Takes a string which is either an empty string or represents an integer,
# and returns an int or None.
def parse_maybe_int(i):
    if i == '':
        return None
    else:
        return int(i)

# Clean up the data types in the enrollments table
for enrollment in enrollments:
    enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
    enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
    enrollment['is_canceled'] = enrollment['is_canceled'] == 'True'
    enrollment['is_udacity'] = enrollment['is_udacity'] == 'True'
    enrollment['join_date'] = parse_date(enrollment['join_date'])

for engagement_record in daily_engagements:
    engagement_record['lessons_completed'] = int(float(engagement_record['lessons_completed']))
    engagement_record['num_courses_visited'] = int(float(engagement_record['num_courses_visited']))
    engagement_record['projects_completed'] = int(float(engagement_record['projects_completed']))
    engagement_record['total_minutes_visited'] = float(engagement_record['total_minutes_visited'])
    engagement_record['utc_date'] = parse_date(engagement_record['utc_date'])

for submission in project_submissions:
    submission['completion_date'] = parse_date(submission['completion_date'])
    submission['creation_date'] = parse_date(submission['creation_date'])

for de in daily_engagements:
    de['account_key'] = de.pop('acct')

enrollment_num_rows = len(enrollments)
unique_enrollments = set([x["account_key"] for x in enrollments])
enrollment_num_unique_students = len(unique_enrollments)
print enrollment_num_rows, enrollment_num_unique_students

engagement_num_rows = len(daily_engagements)
unique_daily_engagements = set([x["account_key"] for x in daily_engagements])
engagement_num_unique_students = len(unique_daily_engagements) 
print engagement_num_rows, engagement_num_unique_students

submission_num_rows = len(project_submissions)
unique_project_submissions = set([x["account_key"] for x in project_submissions])
submission_num_unique_students =  len(unique_project_submissions) 
print submission_num_rows, submission_num_unique_students

surprising_records = []
for item in enrollments:
    if item['account_key'] not in unique_daily_engagements:
        surprising_records.append(item)
        if not item['cancel_date'] == item['join_date']:
            print item