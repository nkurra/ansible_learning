def generate_rscfl_subsystems_header(json_fname, header_file):
    """Using the JSON list of subsystems, generate a header file that creates
    a enum of subsystems.

    Save this header file to $header_file

    Args:
        json_file: File object with a JSON list of subsystems.
        header_file: File to write a C header file containing an enum of
            possible subsystems.
    """
    json_file = open(json_fname, 'r')
    subsys_json = json.load(json_file)
    subsystems = sorted(subsys_json.items(), key=lambda x: x[1]['id'])
    template = jinja2.Template(RSCFL_SUBSYS_HEADER_TEMPLATE)
    args = {}
    args['subsystems'] = subsystems
    args['ADDR_INVALID'] = ADDR_INVALID
    args['ADDR_CALLQ'] = ADDR_CALLQ
    args['ADDR_USER_SYSCALL'] = ADDR_USER_SYSCALL
    args['ADDR_KERNEL_SYSCALL'] = ADDR_KERNEL_SYSCALL
    header_file.write(template.render(args))

    json_file.close() 
