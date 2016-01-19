#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import webapp2
import MySQLdb
import os
import time
import csv

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
env = os.getenv('SERVER_SOFTWARE')
if (env and env.startswith('Google App Engine/')):
  # Connecting from App Engine
  db = MySQLdb.connect(
    unix_socket='/cloudsql/project2-972:tas91',
    user='root')
else:
  # Connecting from an external network.
  # Make sure your network is whitelisted
  db = MySQLdb.connect(
    host='173.194.225.76',
    port=3306,
    user='root')
cur = db.cursor()
file_name = open("all_month.csv","r")
data = csv.reader(file_name)
start_time = time.clock()

for row in data:
	cur.execute("INSERT INTO all_month(time,latitude,longitude,depth,mag,magType,nst,gap,dmin,rms,net,id,updated,place,type) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", row)

end_time = time.clock()
print "\n Time taken to load data : ", end_time - start_time

db.commit()

print 'Records inserted'

