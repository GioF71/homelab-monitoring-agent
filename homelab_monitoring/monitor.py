import os
import time
import socket

import traceback
import logging

import shutil
import mysql.connector

import configuration
import db

import available_modules
import monitor_module

def get_current_host_name():
    return socket.gethostname()

def get_host_by_name(cursor, hostname):
    host_query = "SELECT id, friendly_name FROM monitoring.host WHERE id = '{}' ORDER BY friendly_name".format(hostname)
    cursor.execute(host_query)
    return cursor.fetchall()
    
def create_host(cursor, hostname, friendly_name):
    sql = "INSERT INTO monitoring.host (id, friendly_name) VALUES (%(id)s, %(friendly_name)s)"
    new_host = {
        'id': hostname,
        'friendly_name': friendly_name
    }
    cursor.execute(sql, new_host)

def get_or_create_host(cn, hostname, friendly_name):
    cursor = cn.cursor()
    select_host = get_host_by_name(cursor, hostname)
    if not select_host or len(select_host) == 0:
        create_host(cursor, hostname, friendly_name)
        cn.commit()
        select_host = get_host_by_name(cursor, hostname)
    cursor.close()
    return select_host

def iteration(cn, hostname, iteration_count):
    select_host = get_or_create_host(cn, hostname, configuration.config("HOST_FRIENDLY_NAME", hostname))
    if select_host and len(select_host) == 1:
        print(select_host)
        # process_requested_mount_point_list(cn, hostname, iteration_count)
        # commit once for each iteration

        modules = available_modules.get_module_list()
        for current_module_name in modules:
            current_module : monitor_module.MonitorModule = available_modules.get_module(current_module_name)
            current_module.execute(cn, hostname, iteration_count)

        cn.commit()
    elif select_host and len(select_host) > 1:
        # Should not happen!
        print("Multiple hosts found for id [{}]".format(hostname))
    else:
        # Should not happen!
        print("Host [{}] not found".format(hostname))

if __name__ == "__main__":
    hostname = configuration.config("HOSTNAME", get_current_host_name())
    use_loop = configuration.config("LOOP", True)
    delay = int(configuration.config("DELAY_SEC", "5"))
    delay_on_fail = int(configuration.config("DELAY_ON_FAIL_SEC", "1"))
    cn = None
    iteration_count = 0
    while (True):
        success = False
        iteration_start = time.time()
        try:
            if cn == None:
                cn = db.connect()
            iteration(cn, hostname, iteration_count)
            success = True
        except mysql.connector.errors.OperationalError as mySqlError:
            cn = None
            if mySqlError.errno == -1:
                print("MySQL server not available, skipping iteration")
            else:
                logging.error(traceback.format_exc())
        except Exception as e:
            print("Iteration failed due to exception: [{}]".format(type(e)))
            #logging.error(traceback.format_exc())
            logging.critical(e, exc_info = True)
        iteration_elapsed = time.time() - iteration_start
        print("Iteration elapsed time: [{}]".format(iteration_elapsed))
        if use_loop:
            if success:
                time.sleep(delay)
                iteration_count += 1
            else:
                time.sleep(delay_on_fail)
        else:
            break
    if cn:
        cn.close()


