# ------------------------------------------------------------------------------
#
#   pylapse.py
#   By: Fred Stakem
#   Date: 5.19.2013
#
# ------------------------------------------------------------------------------

# Libraries
import os
import time
import copy
from subprocess import Popen, PIPE

# Setup
script_name = os.path.basename(__file__)
print '   ----------------< Starting %s >----------------   ' % (script_name)

# Globals
image_width = 1000
image_height = 1000
base_filename = 'image_'
output_path = './output/'
number_of_images = 10
time_between_images = 0.1

# Debug info
print 'Parameters'
print '----------'
local_vars = copy.deepcopy( dir() )
for var in local_vars:
    if not var.startswith('__'):
        value = str(locals()[var])
        if not value.startswith('<'):
            print '%s: %s' % (var, value)
print

# Main
print 'Starting main...'
capture_cmd = 'raspistill -t 1 -w %s -h %s -o %s' % ( str(image_width), str(image_height), output_path + base_filename)
for i in range(number_of_images):
    print 'Capturing image: %d' % (i+1)
    cmd = capture_cmd + str(i+1) + '.jpg'
    print 'Running command: %s' % (cmd)
    os.system(cmd)
    time.sleep(time_between_images)

print 'Finished main.'

print '   ----------------< Finishing %s >----------------   ' % (script_name)


