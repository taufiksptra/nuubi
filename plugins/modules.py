#!/usr/bin/python

import sys
import os
import json
import webtech
import requests as res
from requests import get
from os import system

# Nuubi Modules
def certspotter(url):
	target = res.get('https://api.certspotter.com/v1/issuances?domain='+url+'&expand=dns_names&expand=issuer&expand=cert | jq ".[].dns_names[]" | sed "s/\"//g" | sed "s/\*\.//g" | sort -u | grep '+url).text
	data = json.loads(target)
	dump = json.dumps(data,sort_keys=True, indent=4)
	print(dump)
def urlscan(url):
	response = res.get('https://urlscan.io/api/v1/search/?q=domain:'+url).text
	data = json.loads(response)
	dump = json.dumps(data,sort_keys=True, indent=4)
	print(dump)
def whois(url):
	response = get('http://api.hackertarget.com/whois/?q=' + url).text
	sys.stdout.write(response)
def techno(url):
	obj = webtech.WebTech()
	results = obj.start_from_url(url, timeout=1)
	system('tput setaf 9')
	sys.stdout.write(results)
def subnetlookup(cidr):
	response = get('https://api.hackertarget.com/subnetcalc/?q='+ cidr).text
	print(response)
def sub(domain):
	response = get('https://api.hackertarget.com/hostsearch/?q=' + domain).text
	print(response,"\n")
def extract(url):
	response = get('https://api.hackertarget.com/pagelinks/?q=' + url).text
	sys.stdout.write(response)
def httpheader(url):
	response = get('https://api.hackertarget.com/httpheaders/?q=' + url).text
	sys.stdout.write(response)
def gitusers(username):
	response = res.get("https://api.github.com/users/" + username).text
	data = json.loads(response)
	print("[+] Dumping Sensitive information from github")
	os.system('tput setaf 9')
	print("[+] Name : ", str(data['name']))
	print("[+] Location : ", str(data['location']))
	print("[+] ID : ", str(data['id']))
	print("[+] Website : ", str(data['blog']))
	print("[+] Number of public github Repository : " ,str(data['public_repos']))
	print("[+] Number of public gist Repository : ",str(data['public_gists']))
def gitemails(username):
	try:
		response = res.get("https://api.github.com/users/%s/events/public" %(username))
		jsn = response.json()
		data = jsn[0]
		dump = data["payload"]["commits"][0]["author"]["email"]
		print("[+] Email data : ", dump)	
	except KeyError:
		os.system('tput setaf 12')
		print("[+] Aww Snap Unable to find out the email address!")
def geo(ip):
	response = get('https://api.hackertarget.com/geoip/?q=' + ip).text
	print(response,"\n")
def dnslookup(url):
	response = get('https://api.hackertarget.com/dnslookup/?q=' + url).text
	sys.stdout.write(response)
def nmap(domain):
	os.system("nmap -Pn -p- " +domain)
#def respondir(target):
#    os.system("tput setaf 6")
#    os.system("echo "+target+ "| hakrawler -plain | hakcheckurl | grep -v 404")
def banner(ip):
	response = get('https://api.hackertarget.com/bannerlookup/?q='+ip).text
	sys.stdout.write(response)
def traceroute(url):
	response = get('https://api.hackertarget.com/mtr/?q='+url).text
	sys.stdout.write(response)