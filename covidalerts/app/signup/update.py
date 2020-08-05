import csv
import urllib.request as request

#updated live file
r = request.urlopen("https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us-counties.csv").read().decode('utf8').split("\n")
reader = csv.reader(r)

with open("live-us-counties.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for line in reader:
        writer.writerow(line)


#update the past file
r2 = request.urlopen("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv").read().decode('utf8').split("\n")
reader2 = csv.reader(r2)

with open("ago-us-counties.csv", "w", newline="") as csvfile2:
    writer2 = csv.writer(csvfile2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for line in reader2:
        writer2.writerow(line)
