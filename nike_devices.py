from scrapli.driver.core import IOSXEDriver
from pprint import pprint
import requests
import json
import urllib3
import os
import pathlib
from os.path import join
from dotenv import load_dotenv

dotenv_path = join(pathlib.Path().resolve(), '/home/mteke1/oop/devnet_edge/.env')
load_dotenv(dotenv_path)


# Disable HTTPS Certificate warning
urllib3.disable_warnings()

class NikeDevice:
    """
    This class is a parent class for Nike infrastructure devices.
    """
    def __init__(self, hostname, username, password):
        self.hostname = hostname
        self.username = username
        self.password = password



class NikeCiscoDevice(NikeDevice):
    """
    This class is used for creating Cisco(IOSXE and IOS) device instances. 
    It is developed by using "SCRAPLI" library. You can have more info about this library via 'https://github.com/carlmontanari/scrapli'
    Addition to 'scrapli' also 'textFSM' and 'genie' parsers are optionally used.  

    Usage:
    device = NikeCiscoDevice( 'ip address/hostname', 'username', 'password' )

    Attributes:
        hostname(Str): Specify ip address or hostname if DNS resolution is done.
        username(Str): Specify your tacacs Corparate Short login(CSL) username.
        password(Str): Specify your tacacs Corparate Short login(CSL) password.
    """
    
    def __init__(self, hostname, username, password):
        """Init method of the class"""
        NikeDevice.__init__(self, hostname, username, password)
        self.device = {
            "host": self.hostname,
            "auth_username": self.username,
            "auth_password": self.password,
            "auth_secondary": self.password,
            "auth_strict_key": False,
        }
    
    def get_configuration(self):
        """This method is collecting running-configration from IOSXE/IOS devices.
        Usage:
            device.get_configuration()
        """
        conn = IOSXEDriver(**self.device)
        conn.open()
        response = conn.send_command("show running-config")
        conn.close()
        return response.result

    def get_interface_status(self, parsing_module='no_parse'):
        """This method is collecting 'show interface status' output from IOSXE/IOS devices.

        Attributes:
            parsing_module:
                - no_parse  : Collects the data without parsing it
                - genie     : Collects the output and parse it with genie parser.
                - textfsm   : Collects the output and parse it with textfsm parser.
        Usage:
            device.get_interface_status(parsing_module)
        """
        conn = IOSXEDriver(**self.device)
        conn.open()
        response = conn.send_command("show interfaces status")
        conn.close()
        if parsing_module == 'genie':
            return response.genie_parse_output()
        elif parsing_module == 'textfsm':
            return response.textfsm_parse_output()
        else:
            return response.result

    def get_interface_brief(self, parsing_module='no_parse'):
        conn = IOSXEDriver(**self.device)
        conn.open()
        response = conn.send_command("show ip interface brief")
        conn.close()
        if parsing_module == 'genie':
            return response.genie_parse_output()
        elif parsing_module == 'textfsm':
            return response.textfsm_parse_output()
        else:
            return response.result

    def get_interface_description(self, parsing_module='no_parse'):
        conn = IOSXEDriver(**self.device)
        conn.open()
        response = conn.send_command("show interface description")
        conn.close()
        if parsing_module == 'genie':
            return response.genie_parse_output()
        elif parsing_module == 'textfsm':
            return response.textfsm_parse_output()
        else:
            return response.result

    def get_trunk_interfaces(self, parsing_module='no_parse'):
        conn = IOSXEDriver(**self.device)
        conn.open()
        response = conn.send_command("show interfaces trunk")
        conn.close()
        if parsing_module == 'genie':
            return response.genie_parse_output()
        elif parsing_module == 'textfsm':
            return response.textfsm_parse_output()
        else:
            return response.result    

    def get_snmp_user(self, parsing_module='no_parse'):
        conn = IOSXEDriver(**self.device)
        conn.open()
        response = conn.send_command("show snmp user")
        conn.close()
        if parsing_module == 'genie':
            return response.genie_parse_output()
        elif parsing_module == 'textfsm':
            return response.textfsm_parse_output()
        else:
            return response.result

    def get_eigrp_neighbor(self, parsing_module='no_parse'):
        conn = IOSXEDriver(**self.device)
        conn.open()
        response = conn.send_command("show ip eigrp neighbors")
        conn.close()
        if parsing_module == 'genie':
            return response.genie_parse_output()
        elif parsing_module == 'textfsm':
            return response.textfsm_parse_output()
        else:
            return response.result

    def get_eigrp_topology(self, parsing_module='no_parse'):
        conn = IOSXEDriver(**self.device)
        conn.open()
        response = conn.send_command("show ip eigrp topology")
        conn.close()
        if parsing_module == 'genie':
            return response.genie_parse_output()
        elif parsing_module == 'textfsm':
            return response.textfsm_parse_output()
        else:
            return response.result

    def get_eigrp_interfaces(self, parsing_module='no_parse'):
        conn = IOSXEDriver(**self.device)
        conn.open()
        response = conn.send_command("show ip eigrp interfaces")
        conn.close()
        if parsing_module == 'genie':
            return response.genie_parse_output()
        elif parsing_module == 'textfsm':
            return response.textfsm_parse_output()
        else:
            return response.result

    def get_cdp_neighbors(self, parsing_module='no_parse'):
        conn = IOSXEDriver(**self.device)
        conn.open()
        response = conn.send_command("show cdp neighbors")
        conn.close()
        if parsing_module == 'genie':
            return response.genie_parse_output()
        elif parsing_module == 'textfsm':
            return response.textfsm_parse_output()
        else:
            return response.result

    def get_cdp_neighbors_details(self, parsing_module='no_parse'):
        conn = IOSXEDriver(**self.device)
        conn.open()
        response = conn.send_command("show cdp neighbors detail")
        conn.close()
        if parsing_module == 'genie':
            return response.genie_parse_output()
        elif parsing_module == 'textfsm':
            return response.textfsm_parse_output()
        else:
            return response.result

    def get_routing_table(self, parsing_module='no_parse'):
        conn = IOSXEDriver(**self.device)
        conn.open()
        response = conn.send_command("show ip route")
        conn.close()
        if parsing_module == 'genie':
            return response.genie_parse_output()
        elif parsing_module == 'textfsm':
            return response.textfsm_parse_output()
        else:
            return response.result

    def get_routing_table_summary(self, parsing_module='no_parse'):
        conn = IOSXEDriver(**self.device)
        conn.open()
        response = conn.send_command("show ip route summary")
        conn.close()
        if parsing_module == 'genie':
            return response.genie_parse_output()
        elif parsing_module == 'textfsm':
            return response.textfsm_parse_output()
        else:
            return response.result

    def get_os_version(self, parsing_module='no_parse'):
        conn = IOSXEDriver(**self.device)
        conn.open()
        response = conn.send_command("show version")
        conn.close()
        if parsing_module == 'genie':
            return response.genie_parse_output()
        elif parsing_module == 'textfsm':
            return response.textfsm_parse_output()
        else:
            return response.result

    def get_clock_info(self, parsing_module='no_parse'):
        conn = IOSXEDriver(**self.device)
        conn.open()
        response = conn.send_command("show clock")
        conn.close()
        if parsing_module == 'genie':
            return response.genie_parse_output()
        elif parsing_module == 'textfsm':
            return response.textfsm_parse_output()
        else:
            return response.result

    def get_environment_power_info(self, parsing_module='no_parse'):
        conn = IOSXEDriver(**self.device)
        conn.open()
        response = conn.send_command("show environment power all")
        conn.close()
        if parsing_module == 'genie':
            return response.genie_parse_output()
        elif parsing_module == 'textfsm':
            return response.textfsm_parse_output()
        else:
            return response.result

    def get_environment_temperature(self, parsing_module='no_parse'):
        conn = IOSXEDriver(**self.device)
        conn.open()
        response = conn.send_command("show environment temperature")
        conn.close()
        if parsing_module == 'genie':
            return response.genie_parse_output()
        elif parsing_module == 'textfsm':
            return response.textfsm_parse_output()
        else:
            return response.result

    def get_arp_info(self, parsing_module='no_parse'):
        conn = IOSXEDriver(**self.device)
        conn.open()
        response = conn.send_command("show ip arp")
        conn.close()
        if parsing_module == 'genie':
            return response.genie_parse_output()
        elif parsing_module == 'textfsm':
            return response.textfsm_parse_output()
        else:
            return response.result


    def get_ip_nat_translations(self, parsing_module='no_parse'):
        conn = IOSXEDriver(**self.device)
        conn.open()
        response = conn.send_command("show ip nat translations")
        conn.close()
        if parsing_module == 'genie':
            return response.genie_parse_output()
        elif parsing_module == 'textfsm':
            return response.textfsm_parse_output()
        else:
            return response.result

    def get_mac_address_table(self, parsing_module='no_parse'):
        conn = IOSXEDriver(**self.device)
        conn.open()
        response = conn.send_command("show mac address-table")
        conn.close()
        if parsing_module == 'genie':
            return response.genie_parse_output()
        elif parsing_module == 'textfsm':
            return response.textfsm_parse_output()
        else:
            return response.result

    def get_module_info(self, parsing_module='no_parse'):
        conn = IOSXEDriver(**self.device)
        conn.open()
        response = conn.send_command("show module")
        conn.close()
        if parsing_module == 'genie':
            return response.genie_parse_output()
        elif parsing_module == 'textfsm':
            return response.textfsm_parse_output()
        else:
            return response.result

    def get_switch_info(self, parsing_module='no_parse'):
        conn = IOSXEDriver(**self.device)
        conn.open()
        response = conn.send_command("show switch")
        conn.close()
        if parsing_module == 'genie':
            return response.genie_parse_output()
        elif parsing_module == 'textfsm':
            return response.textfsm_parse_output()
        else:
            return response.result


    def get_switch_detail_info(self, parsing_module='no_parse'):
        conn = IOSXEDriver(**self.device)
        conn.open()
        response = conn.send_command("show switch detail")
        conn.close()
        if parsing_module == 'genie':
            return response.genie_parse_output()
        elif parsing_module == 'textfsm':
            return response.textfsm_parse_output()
        else:
            return response.result

    def get_vlan_info(self, parsing_module='no_parse'):
        conn = IOSXEDriver(**self.device)
        conn.open()
        response = conn.send_command("show vlan")
        conn.close()
        if parsing_module == 'genie':
            return response.genie_parse_output()
        elif parsing_module == 'textfsm':
            return response.textfsm_parse_output()
        else:
            return response.result

    def get_tacacs_info(self, parsing_module='no_parse'):
        conn = IOSXEDriver(**self.device)
        conn.open()
        response = conn.send_command("show tacacs")
        conn.close()
        if parsing_module == 'genie':
            return response.genie_parse_output()
        elif parsing_module == 'textfsm':
            return response.textfsm_parse_output()
        else:
            return response.result

    def get_errdisable_recovery_info(self, parsing_module='no_parse'):
        conn = IOSXEDriver(**self.device)
        conn.open()
        response = conn.send_command("show errdisable recovery")
        conn.close()
        if parsing_module == 'genie':
            return response.genie_parse_output()
        elif parsing_module == 'textfsm':
            return response.textfsm_parse_output()
        else:
            return response.result

    def get_access_list_info(self, parsing_module='no_parse'):
        conn = IOSXEDriver(**self.device)
        conn.open()
        response = conn.send_command("show access-lists")
        conn.close()
        if parsing_module == 'genie':
            return response.genie_parse_output()
        elif parsing_module == 'textfsm':
            return response.textfsm_parse_output()
        else:
            return response.result

    def get_ip_protocols_info(self, parsing_module='no_parse'):
        conn = IOSXEDriver(**self.device)
        conn.open()
        response = conn.send_command("show ip protocols")
        conn.close()
        if parsing_module == 'genie':
            return response.genie_parse_output()
        elif parsing_module == 'textfsm':
            return response.textfsm_parse_output()
        else:
            return response.result

    def get_licence_status(self, parsing_module='no_parse'):
        conn = IOSXEDriver(**self.device)
        conn.open()
        response = conn.send_command("show license status")
        conn.close()
        if parsing_module == 'genie':
            return response.genie_parse_output()
        elif parsing_module == 'textfsm':
            return response.textfsm_parse_output()
        else:
            return response.result

    def get_platform_info(self, parsing_module='no_parse'):
        conn = IOSXEDriver(**self.device)
        conn.open()
        response = conn.send_command("show platform")
        conn.close()
        if parsing_module == 'genie':
            return response.genie_parse_output()
        elif parsing_module == 'textfsm':
            return response.textfsm_parse_output()
        else:
            return response.result

    def get_power_inline_info(self, parsing_module='no_parse'):
        conn = IOSXEDriver(**self.device)
        conn.open()
        response = conn.send_command("show power inline")
        conn.close()
        if parsing_module == 'genie':
            return response.genie_parse_output()
        elif parsing_module == 'textfsm':
            return response.textfsm_parse_output()
        else:
            return response.result

    def get_redundancy_info(self, parsing_module='no_parse'):
        conn = IOSXEDriver(**self.device)
        conn.open()
        response = conn.send_command("show redundancy")
        conn.close()
        if parsing_module == 'genie':
            return response.genie_parse_output()
        elif parsing_module == 'textfsm':
            return response.textfsm_parse_output()
        else:
            return response.result


    def get_etherchannel_summary_info(self, parsing_module='no_parse'):
        conn = IOSXEDriver(**self.device)
        conn.open()
        response = conn.send_command("show etherchannel summary")
        conn.close()
        if parsing_module == 'genie':
            return response.genie_parse_output()
        elif parsing_module == 'textfsm':
            return response.textfsm_parse_output()
        else:
            return response.result

    def get_chassis_info(self, parsing_module='genie'):
        return self.get_os_version ('genie')['version']['chassis']

    def get_image_id_info(self, parsing_module='genie'):
        return self.get_os_version ('genie')['version']['image_id']
    
    def get_system_image_info(self, parsing_module='genie'):
        return self.get_os_version ('genie')['version']['system_image']

    def get_os_info(self, parsing_module='genie'):
        return self.get_os_version ('genie')['version']['os']

    def get_number_of_switch_info(self, parsing_module='genie'):
        return len(self.get_os_version ('genie')['version']['switch_num'].keys())

    def get_platform_info(self, parsing_module='genie'):
        return self.get_os_version ('genie')['version']['platform']

    def get_chassis_sn_info(self, parsing_module='genie'):
        return self.get_os_version ('genie')['version']['chassis_sn']

class NikeVcoDevice:
    VCO_URL = "https://nike.velocloud.net/portal/rest"
    PROD_ENTERPRISE_ID = 1
    VELO_TOKEN = os.environ.get("VELO_TOKEN")
    
    def __init__(self):
        self._token = NikeVcoDevice.VELO_TOKEN

    def post_vco_request(self, method, data=None):

        self.headers = {'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Authorization': 'Token ' + self._token}

        response = requests.post(NikeVcoDevice.VCO_URL + method,
                                 headers=self.headers,
                                 verify=False,
                                 data=json.dumps(data)
                                 )
        return json.loads(response.text)

    def getEdgesByName(self, name='') -> list:
        """
        This returns a list of Edges from VeloCloud Orchestrator
        :param name: (optional) Edge Name
        :return: The Edge with the specified name or id, if provided, otherwise a list of all Edges
        """
        response = self.post_vco_request('/enterprise/getEnterpriseEdges',
                            data={
                                "enterpriseId": NikeVcoDevice.PROD_ENTERPRISE_ID
                            })
        if name:
            for edge in response:
                if edge['name'] == name:
                    return edge

        return response

    def getEdgeIdByName(self, name='') -> list:
        """
        This returns a list of Edges from VeloCloud Orchestrator
        :param name: (optional) Edge Name
        :param edge_id: (optional) Edge ID
        :return: The Edge with the specified name or id, if provided, otherwise a list of all Edges
        """
        response = self.post_vco_request('/enterprise/getEnterpriseEdges',
                            data={
                                "enterpriseId": NikeVcoDevice.PROD_ENTERPRISE_ID
                            })
        if name:
            for edge in response:
                if edge['name'] == name:
                    return edge['id']

        return response

    def getEdgesById(self, id='') -> list:
        """
        This returns a list of Edges from VeloCloud Orchestrator
        :param name: (optional) Edge Name
        :param edge_id: (optional) Edge ID
        :return: The Edge with the specified name or id, if provided, otherwise a list of all Edges
        """
        response = self.post_vco_request('/enterprise/getEnterpriseEdges',
                            data={
                                "enterpriseId": NikeVcoDevice.PROD_ENTERPRISE_ID
                            })
        if id:
            for edge in response:
                if edge['id'] == int(id):
                    return edge

        return response

    def getEdgeConfiguration(self, edgeId: int) -> list:
        """
        This returns a list of Edges from VeloCloud Orchestrator
        :param name: (optional) Edge Name
        :param edge_id: (optional) Edge ID
        :return: The Edge with the specified name or id, if provided, otherwise a list of all Edges
        """
        response = self.post_vco_request('/edge/getEdgeConfigurationStack',
                            data={
                                "enterpriseId": NikeVcoDevice.PROD_ENTERPRISE_ID,
                                "edgeId": edgeId
                            })
        print(type(response))
        return response



    def getEdgeManagementIp(self, edgeId: int) -> list:
        """
        This returns a list of Edges from VeloCloud Orchestrator
        :param name: (optional) Edge Name
        :param edge_id: (optional) Edge ID
        :return: The Edge with the specified name or id, if provided, otherwise a list of all Edges
        """
        response = self.post_vco_request('/edge/getEdgeConfigurationStack',
                            data={
                                "enterpriseId": NikeVcoDevice.PROD_ENTERPRISE_ID,
                                "edgeId": edgeId
                            })
        return response[0]["modules"][1]["data"]["lan"]["management"]["cidrIp"]


    def getEdgeLanSviInfo(self, edgeId: int) -> list:
        response = self.post_vco_request('/edge/getEdgeConfigurationStack',
                            data={
                                "enterpriseId": NikeVcoDevice.PROD_ENTERPRISE_ID,
                                "edgeId": edgeId
                            })
        lan_interfaces = {}

        for i in range(0,len(response[0]["modules"][1]["data"]["lan"]["networks"])):
            lan_interfaces[response[0]["modules"][1]["data"]["lan"]["networks"][i]["vlanId"]] = {
                        "svi_name" : response[0]["modules"][1]["data"]["lan"]["networks"][i]["name"],
                        "ip_address" : response[0]["modules"][1]["data"]["lan"]["networks"][i]["cidrIp"],
                         "subnet_mask" : response[0]["modules"][1]["data"]["lan"]["networks"][i]["netmask"],
                         "dhcp_enabled" : response[0]["modules"][1]["data"]["lan"]["networks"][i]["dhcp"]["enabled"],
                         "dhcp_pool_base_number": response[0]["modules"][1]["data"]["lan"]["networks"][i]["baseDhcpAddr"],
                         "dhcp_pool_size" : response[0]["modules"][1]["data"]["lan"]["networks"][i]["numDhcpAddr"],
                         "advertised" : response[0]["modules"][1]["data"]["lan"]["networks"][i]["advertise"],
                         "physical_interface" : response[0]["modules"][1]["data"]["lan"]["networks"][i]["interfaces"]
                        }

        return lan_interfaces


    def getEdgeWanInterfaceInfo(self, edgeId: int) -> list:
        response = self.post_vco_request('/edge/getEdgeConfigurationStack',
                            data={
                                "enterpriseId": NikeVcoDevice.PROD_ENTERPRISE_ID,
                                "edgeId": edgeId
                            })
        wan_interfaces = {}

        for i in range(0,len(response[0]["modules"][1]["data"]["routedInterfaces"])):
            wan_interfaces[response[0]["modules"][1]["data"]["routedInterfaces"][i]["name"]] = {
                        "ipv4_address" : response[0]["modules"][1]["data"]["routedInterfaces"][i]["addressing"]["cidrIp"],
                        "subnet_mask"  : response[0]["modules"][1]["data"]["routedInterfaces"][i]["addressing"]["netmask"],
                        "type" : response[0]["modules"][1]["data"]["routedInterfaces"][i]["addressing"]["type"],
                        "cidr_prefix" : response[0]["modules"][1]["data"]["routedInterfaces"][i]["addressing"]["cidrPrefix"],
                        "duplex" : response[0]["modules"][1]["data"]["routedInterfaces"][i]["l2"]["duplex"],
                        "speed" : response[0]["modules"][1]["data"]["routedInterfaces"][i]["l2"]["speed"],
                        "overlay": response[0]["modules"][1]["data"]["routedInterfaces"][i]["wanOverlay"]
                             }

        return wan_interfaces

    def getEdgeStatus(self, name: str):
        """
        Retrieves aggregate healthStats metric summaries for a specified enterpriseId(and list of edges) 
        over a specified time intervaland list of metrics. On success, this method returns an array of healthsStats
        objects for all requested edges and metrics
        """
        vce_status_by_name = []

        response = self.post_vco_request('/monitoring/getEnterpriseEdgeLinkStatus',
                            data={
                                "enterpriseId": NikeVcoDevice.PROD_ENTERPRISE_ID})
 
        for i in range(len(response)):
            if name == response[i]["edgeName"]:
                vce_status_by_name.append(response[i])
            elif not name:
                return response
        return vce_status_by_name

    def getEdgeSerialNumber(self, name:str):
        """
        Retrieves aggregate healthStats metric summaries for a specified enterpriseId(and list of edges) 
        over a specified time intervaland list of metrics. On success, this method returns an array of healthsStats
        objects for all requested edges and metrics
        """

        vce_status_response = self.getEdgeStatus(name)

        vce_serial_number = {'edgeName': vce_status_response[0]['edgeName'],
                             'Active_VCE_SN': vce_status_response[0]['edgeSerialNumber'],
                             "Standby_VCE_SN": vce_status_response[0]['edgeHASerialNumber']
                            }
        return vce_serial_number

    def getWanInterfaceStatus(self, name: str):
        """
        Retrieves aggregate healthStats metric summaries for a specified enterpriseId(and list of edges) 
        over a specified time intervaland list of metrics. On success, this method returns an array of healthsStats
        objects for all requested edges and metrics
        """
        vce_wan_interface_status_by_name = []

        response = self.post_vco_request('/monitoring/getEnterpriseEdgeLinkStatus',
                            data={
                                "enterpriseId": NikeVcoDevice.PROD_ENTERPRISE_ID})
 
        for i in range(len(response)):
            if name == response[i]["edgeName"]:
                vce_wan_interface_status_by_name.append(response[i])
            elif not name:
                return response
        wan_link = {}
        
        for i in range(len(vce_wan_interface_status_by_name)):
            wan_link[vce_wan_interface_status_by_name[i]["interface"]] = {"ip_address":vce_wan_interface_status_by_name[i]["linkIpAddress"],
                                                                          "isp_info": vce_wan_interface_status_by_name[i]["isp"],
                                                                          "link_state": vce_wan_interface_status_by_name[i]["linkState"],
                                                                          "linkVpnState": vce_wan_interface_status_by_name[i]["linkState"],
                                                                          "edgeState": vce_wan_interface_status_by_name[i]["edgeState"]}
        return wan_link


#my_vco = NikeVcoDevice()
#print(f"VELO_PASSWORD: *****{NikeVcoDevice.VELO_TOKEN[-3:]}")
#pprint(my_vco.getEdgeSerialNumber("NER0502D01"))

"""
def get_os_info(self, parsing_module='genie'):
        return self.get_os_version ('genie')['version']['os']

"""
    