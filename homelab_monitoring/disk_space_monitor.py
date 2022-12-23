from monitor_module import MonitorModule

import configuration
import shutil

class DiskSpaceMonitor(MonitorModule):

    def execute(self, cn, hostname : str, iteration_count : int) -> None:
        self._process_requested_mount_point_list(cn, hostname, iteration_count)

    def _process_requested_mount_point_list(self, cn, hostname : str, iteration_count : int) -> None:
        stored_mount_point_list = self._load_mount_point_list(cn, hostname)
        stored_mount_point_dict = {}
        for stored_mount_point in stored_mount_point_list:
            current_mount_point = stored_mount_point[2]
            stored_mount_point_dict[current_mount_point] = stored_mount_point
        for mp in self._get_mount_point_list():
            self._process_mount_point(cn, hostname, mp, stored_mount_point_dict)

    def _get_mount_point_list(self):
        mount_points = configuration.config("MOUNT_POINTS")
        mount_point_list = mount_points.split(",")
        mp_list = []
        for mp in mount_point_list:
            mp_list.append(mp)
        return mp_list

    def _load_mount_point_list(self, cn, hostname):
        disk_space_query = "SELECT id, host_id, mount_point FROM monitoring.disk_space WHERE host_id = '{}'".format(hostname)
        cursor = cn.cursor()
        cursor.execute(disk_space_query)
        existing_mount_points = cursor.fetchall()
        cursor.close()
        return existing_mount_points

    def _load_mount_point_list(self, cn, hostname):
        disk_space_query = "SELECT id, host_id, mount_point FROM monitoring.disk_space WHERE host_id = '{}'".format(hostname)
        cursor = cn.cursor()
        cursor.execute(disk_space_query)
        existing_mount_points = cursor.fetchall()
        cursor.close()
        return existing_mount_points

    def _process_mount_point(self, cn, hostname, current_mount_point, stored_mount_point_dict):
        current_du = shutil.disk_usage(current_mount_point)
        if current_mount_point in stored_mount_point_dict:
            disk_space_id = stored_mount_point_dict[current_mount_point][0]
            print("updating: MountPoint [{}], disk_space.id [{}]".format(current_mount_point, disk_space_id))
            self._update_disk_space(cn, disk_space_id, current_du)
        else:
            print("Insert for MountPoint [{}]".format(current_mount_point))
            self._insert_disk_space(cn, hostname, current_mount_point, current_du)

    def _insert_disk_space(
            self,
            cn,
            hostname, 
            mount_point, 
            stat):
        disk_space = {
            'host_id': hostname,
            'mount_point': mount_point,
            'total_bytes': stat.total,
            'used_bytes': stat.used,
            'free_bytes': stat.free
        }
        sql = "INSERT INTO monitoring.disk_space (host_id, mount_point, total_bytes, used_bytes, free_bytes) VALUES (%(host_id)s, %(mount_point)s, %(total_bytes)s, %(used_bytes)s, %(free_bytes)s)"
        cursor = cn.cursor()
        cursor.execute(sql, disk_space)
        cursor.close()

    def _update_disk_space(
            self,
            cn,
            id, 
            stat):
        disk_space = {
            'id': id,
            'total_bytes': stat.total,
            'used_bytes': stat.used,
            'free_bytes': stat.free
        }
        sql = "UPDATE monitoring.disk_space SET total_bytes = %(total_bytes)s, used_bytes = %(used_bytes)s, free_bytes = %(free_bytes)s, update_timestamp = CURRENT_TIMESTAMP WHERE id = %(id)s"
        cursor = cn.cursor()
        cursor.execute(sql, disk_space)
        cursor.close()


