try:

    import argparse
    import tomllib
    from termcolor import colored
    import os
    import subprocess
    import requests

except ImportError as errorID:

    print('\n Failed Python3 Import Operation! Module: libasadt3\mainprog.py Failed to Import!')
    print(f' Reported Error Information: "{errorID}" \n ')

    raise SystemExit(9)

except KeyboardInterrupt as errorID:

    print('\n User Keyboard Interrupt Detected! Exiting Upon User Request!')

    raise SystemExit(9)


class config_handler():

    def import_hostcnf():

        config_fileid = os.getcwd() + "/config/scriptinfo.toml"

        with open(config_fileid, 'rb') as host_configuration_file:

            global hostscript_name, hostscript_version, hostscript_description, hostscript_readmefile, hostscript_authors, version_output

            host_config = tomllib.load(host_configuration_file)

            hostscript_name = host_config['script_data']['script_name']
            hostscript_version = host_config['script_data']['script_version']
            hostscript_description = host_config['script_data']['script_desc']
            hostscript_readmefile = host_config['script_data']['script_readme']
            hostscript_authors = host_config['script_data']['script_authors']
            version_output = f'{hostscript_name} | v{hostscript_version} [GPG SIG: {hostscript_authors}]'

            return hostscript_name, hostscript_version, hostscript_description, hostscript_readmefile, hostscript_authors, version_output



class toolkit():

    def toolkit_list(current_version):

        toolavail =  "  Available Tools (As of v" + current_version + ")\n"

        print(colored(toolavail, color='red', attrs=["bold"]), end='\n')
        print(colored('  Scantool Module (--scantool)', color='red', attrs=["bold"]))
        print(colored('  ┣ nmap', color='red', attrs=["bold"]))
        print(colored('  ┃ ╰ config/scantool/nmap.toml', color='red', attrs=["bold"]))
        print(colored('  ┣ nikto', color='red', attrs=["bold"]))
        print(colored('    ╰ config/scantool/nikto.toml', color='red', attrs=["bold"]), end='\n\n\n')

        print(colored('  Package Install Commands:', color='red', attrs=["bold"]), end='\n\n')
        print(colored('  Scantool Module (--scantool)', color='red', attrs=["bold"]))
        print(colored('  ┣ nmap', color='red', attrs=["bold"]))
        print(colored('  ┃ ╰ sudo apt install nmap -y', color='red', attrs=["bold"]))
        print(colored('  ┣ nikto', color='red', attrs=["bold"]))
        print(colored('    ╰ sudo apt install nikto -y', color='red', attrs=["bold"]))
        
        raise SystemExit(0)



class progbanner():

    def showbanner_normal(current_version):

        print('\n')
        print(colored('             (                ( ', color='red', attrs=["bold"]))
        print(colored('     (       )\ )     (       )\ )     *   ) ', color='red', attrs=["bold"]))
        print(colored('     )\     (()/(     )\     (()/(     )  /( ', color='red', attrs=["bold"]))
        print(colored('  ((((_)(    /(_)) ((((_)(    /(_))   ( )(_))  ⌠A⌡ssistive M', color='red', attrs=["bold"]))
        print(colored('   )\ _ )\  (_))    )\ _ )\  (_))_   (_(_())   ⌠S⌡earch    A', color='red', attrs=["bold"]))
        print(colored('   (_)_\(_) / __|   (_)_\(_)  |   \  |_   _|   ⌠A⌡nd       R', color='red', attrs=["bold"]))
        print(colored('    / _ \   \__ \    / _ \    | |) |   | |     ⌠D⌡iscovery K', color='red', attrs=["bold"]))
        print(colored('   /_/ \_\  |___/   /_/ \_\   |___/    |_|     ⌠T⌡ool      3', color='red', attrs=["bold"]))
        print(colored(' ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━', color='red', attrs=["bold"]))
        print(colored(' ⌠PROTECT THE INNOCENT⌡ ⌠PROTECT THE INTERNET⌡', color='red', attrs=["bold"]))
        print(colored('            ⌠PROTECT THE FUTURE⌡', color='red', attrs=["bold"]), end='\n\n')
        print(colored('  ╔════════════════════════════════════════╗', color='red', attrs=["bold"]))
        print(colored('  ║       Script Developed By ODFSEC       ║', color='red', attrs=["bold"]))
        print(colored(f'  ║        [v{current_version}] [MARK III BETA]        ║', color='red', attrs=["bold"]))
        print(colored('  ║                                        ║', color='red', attrs=["bold"]))
        print(colored('  ║                                        ║', color='red', attrs=["bold"]))
        print(colored('  ║             W3 4R3 0DFS3C              ║', color='red', attrs=["bold"]))
        print(colored('  ╚════════════════════════════════════════╝', color='red', attrs=["bold"]), end='\n')

    def showbanner_short(current_version):

        print("")
        print(colored('   █████╗  ███████╗  █████╗  ██████╗  ████████╗', color='red', attrs=["bold"]))
        print(colored('  ██╔══██╗ ██╔════╝ ██╔══██╗ ██╔══██╗ ╚══██╔══╝', color='red', attrs=["bold"]))
        print(colored('  ███████║ ███████╗ ███████║ ██║  ██║    ██║', color='red', attrs=["bold"]))
        print(colored('  ██╔══██║ ╚════██║ ██╔══██║ ██║  ██║    ██║', color='red', attrs=["bold"]))
        print(colored('  ██║  ██║ ███████║ ██║  ██║ ██████╔╝    ██║', color='red', attrs=["bold"]))
        print(colored('  ╚═╝  ╚═╝ ╚══════╝ ╚═╝  ╚═╝ ╚═════╝     ╚═╝', color='red', attrs=["bold"]))
        print(colored(f'  Assistive Search And Discovery Tool v{current_version}', color='red', attrs=["bold"]))
        print("")



class permscheck():

    def check_uid0_status():

        if os.getuid() == 0:

            global admin_bool
            
            admin_bool = "True"

            return admin_bool

        else:

            progbanner.showbanner_short(hostscript_version)
            
            print(colored('\n  Warning: It Is Suggested To Use SUID When Executing This Script', color='red', attrs=["bold", ]))
            print(colored('           Failure To Do So May Result In Unsuccessful Tool Execution\n', color='red', attrs=["bold", ]))
            print(colored('  Suggested Fix: Execute With "sudo" Flag', color="blue", attrs=["bold", ]))
            print(colored('                 Ex: sudo ./asadt.py --help', color="blue", attrs=["bold", ]))
            print(colored('                 Or Comment Out Line 42 In "asadt.py" ', color="blue", attrs=["bold", ]))
            print(colored('                 To Disengange Sudo Mode (Not Suggested)', color="blue", attrs=["bold", ]))
            
            editmodemsg = colored('\nPress Enter To Exit Script OR Type "edit" To Disengage Sudo Mode > ', color='red', attrs=["bold"])
            editmode_input = input(editmodemsg)

            if editmode_input == "edit":

                localscript = os.getcwd() + "/asadt.py"

                command_to_execute = "nano  --linenumbers --nonewlines --softwrap +92 " + str(f'"{localscript}"')
                subprocess.call(command_to_execute, shell=True)

                os.chmod(localscript, 0o751)

                raise SystemExit(0)

            else:

                raise SystemExit(2)



class updatecheck():

    def download_update(url):

        local_filename = ".newversion_" + url.split('/')[-1]
        r = requests.get(url)
        f = open(local_filename, 'wb')

        for chunk in r.iter_content(chunk_size=512 * 1024): 

            if chunk:

                f.write(chunk)

        f.close()
        
        return

    def check_update(current_version):

        global newchkfile; newchkfile= os.getcwd() + "/.newversion_scriptinfo.toml"
        
        try:

            checkfile_configurations = open(newchkfile, "r")

        except:

            print(colored('\n  URL Capture Error: Failed To Capture Script Main Configuration @ {newchkfile}', color='red', attrs=["bold"]))            

            raise SystemExit(2)

        else:

            global scriptversion_new

            with open(newchkfile, 'rb') as newchkfile_update:

                try:

                    scriptinfo_new = tomllib.load(newchkfile_update)

                    scriptversion_new = scriptinfo_new["script_data"]["script_version"]
                
                except:

                    print(colored('\n  Update Check: Unable To Parse New Configuration... Not ".toml" Syntax???', color='red', attrs=["bold"]))

                    os.remove(newchkfile)

                    raise SystemExit(2)

            if scriptversion_new == current_version:
            
                print(colored('  \nUpdate Check: No Updates Were Reported From Github!\n', color="green", attrs=["bold"]))

                os.remove(newchkfile)

                raise SystemExit(0)
            
            else:

                versionupdate = "  Update Check: An Update For ASADT MK III Is Available! " + "v" + current_version + " => " + "v" + scriptversion_new
                downloadid = "  Download Here: " + "https://github.com/odf-community/ASADT3/archive/refs/tags/v" + scriptversion_new + ".zip"
                infolink = "  Read More: " + "https://github.com/odf-community/ASADT3/releases/tag/v" + scriptversion_new
                repolink = "  Clone Me!: git clone https://github.com/odf-community/ASADT3.git"
                
                print('\n')
                print(colored(versionupdate, color="yellow", attrs=["bold"]))
                print(colored(downloadid, color="green", attrs=["bold"]))
                print(colored(repolink, color="green", attrs=["bold"]))
                print(colored(infolink, color="blue", attrs=["bold"]))

                os.remove(newchkfile)

                raise SystemExit(0)



class argument_handler():

    def argerror_invalidtoolname(localfailedtoolname):

        print(colored('  [!] Invalid Tool Name >', color='red', attrs=["bold"]), end=" ")
        print(colored(f'"{localfailedtoolname}" ', color='yellow', attrs=["bold"]))

        raise SystemExit(2)
    
    def argerror_invalidexitclause(localfailedexitclause):

        print(colored('  [!] Invalid Entry Command >', color='red', attrs=["bold"]), end=" ")
        print(colored(f'"{localfailedexitclause}" ', color='yellow', attrs=["bold"]))

        raise SystemExit(2)

    def parsearg(version_output):

        global argument_parser

        argument_parser = argparse.ArgumentParser(
                                                description='Assistive Search And Discovery Tool Mark 3',
                                                epilog='Thank You For Using the ASADT MK III Beta Python Script'
                                                )


        argument_parser.add_argument(

            "--scantool",
            action="store_true",
            help="Selects (tool_name) In The 'scantool' Module For Execution"

        )

        argument_parser.add_argument(

            "--tools",
            action="store_true",
            help="List Available Tools By Module Name"

        )

        argument_parser.add_argument(

            "--updatechk",
            action="store_true",
            help="Checks For Updates By Downloading The Newest ScriptInfo Configuration From GitHub"

        )

        argument_parser.add_argument(

            "tool_name",
            nargs="*",
            help="Utility/Script To be Executed (Used In Conjunction With --module_name)"

        )

        argument_parser.add_argument(

            "-v",
            action="store_true",
            help="Shows Program Version With Our Cool Banner :)"

        )

        argument_parser.add_argument(

            "--version",
            action="version",
            version=version_output,
            help="Show Program's Name, Version & Authors"

        )

        args = argument_parser.parse_args()

        return args