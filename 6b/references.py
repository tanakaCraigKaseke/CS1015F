# Student Name: Craig Kaseke
# Student Id: KSKTAN003
# Date: 08-04-2025
# Last Updated: 08-04-2025
# Description: Script to reformat references as follows:
#             • The author names are in title case.
#             • The title has only the first letter capitalised and,
#             • The rest remains the same.
#             Assume that the input reference format is: a list of authors, space, (year), space, title, comma, other
#             information.

# Reference input
input_references = "poulo, lebeko bernard (2013) fine-grained scalability Of digital library services In The cloud, SAICSIT Conference 2014, ACM, pp23-34, 2014"

# Find positions of key delimiters
start_of_year_index = input_references.find("(")
end_of_year_index = input_references.find(")")
first_comma_after_year = input_references.find(",", end_of_year_index)

# Extract parts of the reference
author_names = input_references[0:start_of_year_index].title()
year = input_references[start_of_year_index:end_of_year_index + 1]

# Extract the title (from after year to first comma)
title = input_references[end_of_year_index + 2:first_comma_after_year]
formatted_title = title[0].upper() + title[1:].lower()

# Extract everything after the title's comma
rest = input_references[first_comma_after_year:]

# Construct and print reformatted reference
reformatted_reference = author_names + year + " " + formatted_title + rest
print("Reformatted reference:")
print(reformatted_reference)