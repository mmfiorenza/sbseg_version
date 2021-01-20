import netmiko
import paramiko
import os
from nameko.rpc import rpc, RpcProxy


class SSH:
    """
        Cisco SSH Connector Service
        Function that performs the application via ssh of the rules generated by the translation modules
        Receive parameters:
          - host: management ip of the device that will receive the rules
          - port: device ssh port
          - username: device username for ssh access
          - password: device password for ssh access
          - device_type: indicates the device's OS 'cisco_ios' or 'linux', other devices_type are available
          in the netmiko documentation
          - command: set of commands generated by the translator module
        Return:
          - String 'ERROR': if an error is identified in the application of the rules
          - String 'OK': successful application of the rules
    """

    name = "cisco_connector"
    zipcode_rpc = RpcProxy('cisco_service_connector')

    @rpc
    def apply_config(self, host, port, username, password, device_type, commands):
        with open('.command.txt', 'w+b') as archive:
            archive.write(commands.encode())
        archive = open('.command.txt', 'r')
        try:
            ssh_session = netmiko.ConnectHandler(device_type=device_type, ip=host, port=port, username=username, password=password)
            ssh_session.send_command_expect("enable" + '\n', expect_string="Password: ")
            ssh_session.send_command_expect(password + '\n', expect_string="# ")
            for line in archive:
                print(line)
                output = ssh_session.send_command(line + '\n', expect_string="#", cmd_verify=False)
                print(output)
            ssh_session.disconnect()
            #return 'OK'
        except(netmiko.ssh_exception.NetMikoAuthenticationException,
               netmiko.ssh_exception.NetMikoTimeoutException,
               paramiko.ssh_exception.SSHException) as s_error:
            print(s_error)
        archive.close()
        os.remove('.command.txt')
        return 'OK'


