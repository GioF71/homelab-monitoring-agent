# HomeLab Monitoring Agent

## Caveat

This is a work in progress. The documentation is still incomplete.  

## DataStore

This agent uses MySQL/MariaDB as its datastore. It currently requires two tables, `host` and `disk_space`. Disk space is currently the only implemented metric.

## Why 

Doesn't NetData and InfluxDB, or Prometheus, do everything an more? Yes, they do, but it's a lot more than what I need and those stack require much more computing power. So I am building something a lot simpler for my specific needs.

## Tools

