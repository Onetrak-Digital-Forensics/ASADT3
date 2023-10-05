#!/usr/bin/env python3

###########################
## ASADT Mark III Python ##
###########################

#############################################################################
# This Repository Utilizes The GNU General Public License v3                #
#                                                                           #
# As a sole actor, you are authorized to redistribute the data              #
# of this repository as long as you follow the proper guidelines listed     #
# within the GNU GPLv3 License, and you do not redistribute for the purpose #
# of financial, commerciality, marketability, or otherwise profitable gain  #
#############################################################################

##################################################################################################
## Author: @odf-community                                                                       ##
##                                                                                              ##
## ODFSEC Developer ID's: 9990909 (secops@odfsec.org)                                           ##
## Signed GPG ID's: 685619EDCE460E26 (secops@odfsec.org)                                        ##
##################################################################################################


##################################################################################################
## Document Syntax Outline                                                                      ##
##                                                                                              ##
## Program Modules                                                                              ##
##                                                                                              ##
## ┣ asadt3 (mainprog.py)                                                                       ##
## ┃ ╰ Class\Function Layout                                                                    ##
## ┃   ┣ config_handler                                                                         ##
## ┃   ┃ ╰ import_hostcnf()                                                                     ##
## ┃   ┣ toolkit                                                                                ##
## ┃   ┃ ╰ toolkit_list()                                                                       ##
## ┃   ┣ progbanner                                                                             ##
## ┃   ┃ ├ showbanner_normal(current_version)                                                   ##
## ┃   ┃ ╰ showbanner_short(current_version)                                                    ##
## ┃   ┣ permscheck                                                                             ##
## ┃   ┃ ╰ check_uid0_status()                                                                  ##
## ┃   ┣ updatecheck                                                                            ##
## ┃   ┃ ├ download_update(url)                                                                 ##
## ┃   ┃ ╰ check_update(current_version)                                                        ##
## ┃   ┣ argument_handler                                                                       ##
## ┃   ┃ ├ argerror_invalidtoolname(localfailedtoolname)                                        ##
## ┃   ┃ ├ argerror_invalidexitclause(localfailedexitclause)                                    ##
## ┃   ┻ ╰ parsearg(version_output)                                                             ##
## ┃                                                                                            ##
## ┣ scantool (scantool.py)                                                                     ##
## ┃ ╰ Class\Function Layout                                                                    ##
## ┃   ┣ config_handler                                                                         ##
## ┃   ┃ ├  get_tool_config(toolname)                                                           ##
## ┃   ┃ ╰  edit_tool_configuration(toolname)                                                   ##
## ┃   ┣ gui_handler                                                                            ##
## ┃   ┃ ├  nmapui()                                                                            ##
## ┃   ┃ ╰  niktoui()                                                                           ##
## ┃   ┣ stouterr_handler                                                                       ##
## ┃   ┃ ├ check_output(errorid)                                                                ##
## ┃   ┃ ╰ check_output_stream(output_location)                                                 ##
## ┃   ┣ cmdgen                                                                                 ##
## ┃   ┃ ├  cmdgen_nmap(values)                                                                 ##
## ┃   ┃ ╰ cmdgen_nikto(values)                                                                 ##
## ┻   ┻                                                                                        ##
##################################################################################################


try:

    from libasadt3 import mainprog as asadt3
    from libasadt3 import scantool as scantool

except ImportError as errorID:

    print('\n Failed Python3 Import Operation! Module: Failed to Import MainProg Module(s)!')
    print(f' Reported Error Information: "{errorID}" \n ')

    raise SystemExit(9)

except KeyboardInterrupt as errorID:

    print('\n User Keyboard Interrupt Detected! Exiting Upon User Request!')

    raise SystemExit(9)



## Import Host Configuration
hostscript_name, hostscript_version, hostscript_description, hostscript_readmefile, hostscript_authors, version_output = asadt3.config_handler.import_hostcnf()



## Check User Permissions
asadt3.permscheck.check_uid0_status()



## Parse User Inputted Arguments
args = asadt3.argument_handler.parsearg(version_output)



## Define Argument Output
if args.v:

    asadt3.progbanner.showbanner_normal(hostscript_version)

    raise SystemExit(0)

elif args.updatechk:

    asadt3.progbanner.showbanner_short(hostscript_version)
    asadt3.updatecheck.download_update("https://raw.githubusercontent.com/odf-community/ASADT3/main/config/scriptinfo.toml")
    asadt3.updatecheck.check_update(hostscript_version)

elif args.scantool:

    if not args.tool_name:

        asadt3.progbanner.showbanner_short(hostscript_version)

        asadt3.argument_handler.argerror_invalidtoolname(localfailedtoolname='nullinput')

    elif args.tool_name[0] == "nmap":

        asadt3.progbanner.showbanner_short(hostscript_version)

        scantool.config_handler.get_tool_config(tool_name='nmap')

        execargs = scantool.gui_handler.nmapui()

        if execargs == str("editcnf"):
                
            scantool.config_handler.edit_tool_configuration(tool_name='nmap')

        else:

            scantool.cmdgen.cmdgen_nmap(execargs)

    elif args.tool_name[0] == "nikto":

        asadt3.progbanner.showbanner_short(hostscript_version)

        scantool.config_handler.get_tool_config(tool_name='nikto')

        execargs = scantool.gui_handler.niktoui()

        if execargs == str("editcnf"):

            scantool.config_handler.edit_tool_configuration(tool_name='nikto')

        else:

            scantool.cmdgen.cmdgen_nikto(execargs)

    else:

        asadt3.progbanner.showbanner_short(hostscript_version)

        asadt3.argument_handler.argerror_invalidtoolname(args.tool_name[0])

elif args.tools:

    asadt3.progbanner.showbanner_short(hostscript_version)

    asadt3.toolkit.toolkit_list(hostscript_version)

else:

    asadt3.argument_handler.argerror_invalidexitclause(args)