# ~*~ coding: utf-8 ~*~

from .callback import *
from .inventory import *
from .runner import *
from .exceptions import *

d = {
    'changed': True,
    'instance': {
        'module_hw': True,
        'hw_name': 'maliao-web2',
        'hw_power_status': 'poweredOn',
        'hw_guest_full_name': 'CentOS 4/5/6/7 (64-bit)',
        'hw_guest_id': 'centos64Guest',
        'hw_product_uuid': '423ff446-8a7f-dfee-db48-2ae59ee65648',
        'hw_processor_count': 1,
        'hw_cores_per_socket': 1,
        'hw_memtotal_mb': 1024,
        'hw_interfaces': ['eth0'],
        'hw_datastores': ['datastore1'],
        'hw_files': ['[datastore1] maliao-web2/maliao-web2.vmx',
                     '[datastore1] maliao-web2/maliao-web2.nvram',
                     '[datastore1] maliao-web2/maliao-web2.vmsd',
                     '[datastore1] maliao-web2/maliao-web2.vmdk'],
        'hw_esxi_host': '172.16.10.16',
        'hw_guest_ha_state': None,
        'hw_is_template': False,
        'hw_folder': '/BF/vm',
        'hw_version': 'vmx-11',
        'instance_uuid': '503fd48c-2b7d-3e3d-236a-c6c550fb4f3c',
        'guest_tools_status': 'guestToolsRunning',
        'guest_tools_version': '9536',
        'guest_question': None,
        'guest_consolidation_needed': False,
        'ipv4': '172.16.10.66',
        'ipv6': None,
        'annotation': '',
        'customvalues': {},
        'snapshots': [],
        'current_snapshot': None,
        'vnc': {},
        'hw_cluster': None,
        'hw_eth0': {
            'addresstype': 'assigned',
            'label': 'Network adapter 1',
            'macaddress': '00:50:56:bf:3a:dd',
            'ipaddresses': [
                '172.16.10.66',
                'fe80::9955:4b88:f1a:70c5',
                'fe80::7808:a051:215d:9646'
            ],
            'macaddress_dash': '00-50-56-bf-3a-dd',
            'summary': 'VM Network',
            'portgroup_portkey': None,
            'portgroup_key': None
        }
    },
    'invocation': {
        'module_args': {
            'hostname': '172.16.10.6',
            'username': 'administrator@baifu.com',
            'password': 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER',
            'validate_certs': False,
            'state': 'present',
            'datacenter': 'BF',
            'folder': '',
            'name': 'maliao-web2',
            'disk': [
                {
                    'datastore': 'datastore1',
                    'size_gb': 20,
                    'type': 'eagerzeroedthick'
                }
            ],
            'hardware': {
                'memory_mb': 1024,
                'num_cpu_cores_per_socket': 2,
                'scsi': 'paravirtual',
                'hotadd_cpu': True,
                'hotremove_cpu': True,
                'hotadd_memory': True
            },
            'template': 'centos7',
            'wait_for_ip_address': True,
            'port': 443,
            'is_template': False,
            'customvalues': [],
            'name_match': 'first',
            'use_instance_uuid': False,
            'cdrom': {},
            'force': False,
            'state_change_timeout': 0,
            'linked_clone': False,
            'networks': [],
            'customization': {},
            'wait_for_customization': False,
            'vapp_properties': [],
            'annotation': None,
            'uuid': None,
            'guest_id': None,
            'esxi_hostname': None,
            'cluster': None,
            'snapshot_src': None,
            'resource_pool': None,
            'customization_spec': None,
            'datastore': None,
            'convert': None}
    },
    '_ansible_no_log': False
}
