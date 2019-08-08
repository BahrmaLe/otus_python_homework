def args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-p', action='store', dest='package_version', default="docker",
                        help='Get version of the package')
    parser.add_argument('-d', action='store', dest='directory', default=".",
                        help='Get file list in the directory')
    parser.add_argument('--port', action='store', dest='port_activity', default=":21",
                        help='Get port activity')
    parser.add_argument('--program', action='store', dest='program_proccess', default="docker",
                        help='Get program info')
    parser.add_argument('--ifconfig', action='store_const', dest='ip_config', const="test_ifconfig",
                        default="test_ifconfig",
                        help='Get ifconfig info')
    parser.add_argument('--route', action='store_const', dest='route_config', const="test_check_default_route",
                        default="test_check_default_route",
                        help='Get route')
    parser.add_argument('--cpu', action='store_const', dest='cpu_info', const="test_processor_info",
                        default="test_processor_info",
                        help='Get CPU info')
    parser.add_argument('--net', action='store_const', dest='net_info', const="test_network_bytes",
                        default="test_network_bytes",
                        help='Get Net stats')
    parser.add_argument('--service', action='store_const', dest='service_status', const="apache2",
                        default="test_service_stat",
                        help='Get Service stats')
    parser.add_argument('--curdir', action='store_const', dest='current_directory', const="test_current_dir",
                        default="test_current_dir",
                        help='Get Current path')
    parser.add_argument('--kernel', action='store_const', dest='kernel_version', const="test_kernel_version",
                        default="test_kernel_version",
                        help='Get Kernel version')
    parser.add_argument('--os', action='store_const', dest='os_verison', const="test_os_version",
                        default="test_os_version",
                        help='Get OS Version')
    return parser.parse_args()