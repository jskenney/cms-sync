# Cascade CMS Sync config file example.

# If the site supports the use of an API Key, use that and skip
# the USERNAME / PASSWORD section, otherwise leave commented out.
# You will need either APIKEY or USERNAME configured.

# APIKEY = '*'

# If you are not using the APIKEY, you must set USERNAME below
# PASSWORD can also be set but is not recommended

USERNAME = 'myusername'
# PASSWORD = 'mypassword'

# You must specify the CASCADE CMS Site name, you can see this
# within the Cascade web interface

SITE = "User Sites CompSci - Public"

# Define the directory that the files will be added to as the ROOT,
# and the directory you wsh to publish after syncs, these will most likely
# be the same.

ROOT = "kenney/MyWebSite"
PUBLISH = "kenney/MyWebSite"

# Would you like to publish each file as it syncs, or upload all then publish,
# setting this to false should make things faster.
PUBLISH_AS_YOU_GO = False

# The system ignores all files starting with a . by default, provide the
# file names to ignore below.  Note that the system will block both files
# named in this list and any file that whose name matches any item at the
# Beginning.  Example, if you add 'x' to the list, any file starting with x
# would be blocked from syncing
IGNORE = ['cmssync.py']

# Enter the location of the API endpoint for your local castade server.
API = 'https://domain.com/api/v1/'
