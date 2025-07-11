# The  lines starting with #'s are not part of the code they are comments
# Import the cw_api package
import cw_api

# Assign clubcode and the corresponding token you were given
clubcode = ''
api_token = ''

# Setup the data request you can find information for formating in the POSTGREST document provided
# This request just accesses the memvisit table and counts total visits per member_no
# cw_api can only return a maximum of 1000 entries to limit the volume of data sent
data_request = (
    f"memvisit"
    f"?select=member_no,member_no.count()"
    f"&mt_club_code=eq.8633"
)

# the fetch 
df = cw_api.fetch(clubcode, api_token, data_request)
# print the dataframe to terminal
print(df)