try:

    import PySimpleGUI as guihandler
    from termcolor import colored
    import subprocess
    import os
    import math
    import time
    import tomllib

except ImportError as errorID:

    print('\n Failed Python3 Import Operation! Module: libasadt3\scantool.py Failed to Import!')
    print(f' Reported Error Information: "{errorID}" \n ')

    raise SystemExit(9)

except KeyboardInterrupt as errorID:

    print('\n User Keyboard Interrupt Detected! Exiting Upon User Request!')

    raise SystemExit(9)

module_name = "scantool"
module_version = "v1.0.4"



class config_handler():

    def get_tool_config(tool_name):

        config_file_id = os.getcwd() + "/config/" + module_name + "/" + tool_name + ".toml"

        global script_name
        global script_version

        with open(config_file_id, 'rb') as cnf_currenttool:

            global current_script_configuration
            
            current_script_configuration = tomllib.load(cnf_currenttool)

            script_name = current_script_configuration["ScriptInfo"]["script_id"]
            script_version = current_script_configuration["ScriptInfo"]["script_version"]

            print(colored(f'\n  Initializing TOML Configuration For: {script_name}-v{script_version} ({module_name}-{module_version})...', color="blue", attrs=["bold"]), end=" ")
            
            time.sleep(2.5)

            print(colored(f'"{tool_name}_{script_version}" Complete!\n', color="green", attrs=["bold"]))

            print(colored(f'  [MOD EXEC] Now Executing Module: "{module_name}-{tool_name}_{script_version}"', color="red", attrs=["bold"]))
            print(colored('\n  Happy Hacking! :P\n', color='red', attrs=["bold"]))

        if tool_name == "nmap":
            
            global scriptenabler_nmap_host
            global scriptenabler_nmap_updatedb
            global scriptenabler_nmap_nsescriptscan
            global scriptenabler_nmap_nsedebug
            global scriptenabler_nmap_permuser
            global scriptoutput_nmap_fullscan

            scriptenabler_nmap_host = current_script_configuration["ScriptEnablers"]["nmap_enable"]
            scriptenabler_nmap_updatedb = current_script_configuration["ScriptEnablers"]["nmap_updatedb"]
            scriptenabler_nmap_nsescriptscan = current_script_configuration["ScriptEnablers"]["nmap_nsescriptscan_enable"]
            scriptenabler_nmap_nsedebug = current_script_configuration["ScriptEnablers"]["nmap_nsedebug_enable"]
            scriptenabler_nmap_permuser = current_script_configuration["ScriptEnablers"]["nmap_assumesudoperms_enable"]
            scriptoutput_nmap_fullscan = current_script_configuration["ScriptOutput"]["nmap_fullscan_output_filename"]

        elif tool_name == "nikto":
              
            global scriptenabler_nikto_host
            global scriptenabler_nikto_displaytype
            global scriptenabler_nikto_nointeractive
            global scriptoutput_nikto_default
            global scriptoutput_nikto_format

            scriptenabler_nikto_host = current_script_configuration["ScriptEnablers"]["nikto_enable"]
            scriptenabler_nikto_displaytype = current_script_configuration["ScriptEnablers"]["nikto_displaytype"]
            scriptenabler_nikto_nointeractive = current_script_configuration["ScriptEnablers"]["nikto_nointeractive"]
            scriptoutput_nikto_format = current_script_configuration["ScriptOutput"]["nikto_output_format"]
            scriptoutput_nikto_default = current_script_configuration["ScriptOutput"]["nikto_default_output_filename"]

        else:
              
            print(colored('\n  [MOD EXEC] Module Execution Failed! Invalid Tool Name Specified!', color='red', attrs=["bold"]))

            raise SystemExit(9)

    def edit_tool_configuration(tool_name):

        config_file_id = os.getcwd() + "/config/" + module_name + "/" + tool_name + ".toml"

        print(colored(f"\n  Editing TOML Configuration For: {script_name}-v{script_version} ({module_name}-{module_version})", color="blue", attrs=["bold"]))

        host_command = "nano --nonewlines --linenumbers +6"
        command_to_execute = host_command + " " + str(f'"{config_file_id}"')
        subprocess.call(command_to_execute, shell=True)

        os.chmod(config_file_id, 0o751)
        
        print(colored(f"\n\n  TOML Configuration File Changes For: {script_name}-v{script_version} ({module_name}-{module_version}) Has Been Sucessfully Saved!", color="yellow", attrs=["bold"]))
        print(colored(f"\n  File Name: {config_file_id} \n  File RW Permissions: 0o751", color="blue", attrs=["bold"]))

        raise SystemExit(0)



class gui_handler():

    def nmapui():

        nmap_scantype_dropdown_layout = ["TCP Syn Scan","Connect() Scan","ACK Scan","Window Scan","Maimon Scan", "UDP Scan", "TCP Null Scan", "FIN Scan", "Xmas Scan"]

        nmap_scrn1_layout = [

            [

                guihandler.Text(
                    
                    text='TARGET SPECIFICATION',
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="center",
                    
                )

            ],
            [

                guihandler.Text(
                    
                    text='Enter Target Address*:',
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="left",
                    tooltip='(Required) Accepted Parameters: \n\nIP Address: Ex. 10.0.0.1 \nIP Range: Ex. 10.0.0-255.1-254 \nHostname: Ex. scanme.nmap.org / odfsec.org \nNetBlock: Ex. 10.0.0.1/24'
                    
                ),

                guihandler.Input(
            
                    text_color='red',
                    background_color='black',
                    border_width=2,
                    justification="left"
                    
                )

            ],
            [

                guihandler.Text(
                    
                    text='Enter Target Port or Port Range*:',
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="left",
                    tooltip='(Required) Accepted Parameters: \n\nSingular Port Number: Ex. 443 \nPort Selection: Ex. 80,443,53,22,21 \nPort Range: Ex. 1-65535 \n\nYou Can Also Specify Port Type:  \n"U:" for UDP \n"T:" for TCP \n"S:" for SCTP \nEx. U:22 or T:443. \nEx.T:443,80,22,8080,9090 etc.'
                    
                ),

                guihandler.Input(
            
                    text_color='red',
                    background_color='black',
                    border_width=2,
                    
                )

            ],
            [
                guihandler.Text(
                
                text="\n ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n SCAN TUNING OPTIONS",
                text_color='red',
                background_color='black',
                expand_x=True,
                justification="center",

                )

            ],
            [

                guihandler.Text(
            
                    text='NSE Script Scan Method(s):',
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="left",
                    tooltip='Accepted Parameters: \n\nSingular Catagory:        By Script Type:        By Script Type Exclusion: \nauth                               intrusive                   not intrusive\nbroadcast                      safe                          not safe \nbrute                             default                       not default \ndiscovery \ndos \nexploit \nexternal \nfuzzer \nmalware \nversion \nvuln \n\nNote: Multi Catagory Execution Is Possible; Ex. vuln,dos,fuzzer \n(Must Include Comma "," Seperator)'

                ),

                guihandler.Input(
            
                    text_color='red',
                    background_color='black',
                    border_width=2,
                    justification="left"
                    
                )

            ],
            [

                guihandler.Text(
            
                    text='NSE Script Arguments (filename):',
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="left",
                    tooltip='Accepted Parameters: \n\n Filename of arguments file for NSE Script Scan Methods. \nEx. /home/user/Documents/argfile.txt'

                ),

                guihandler.Input(
            
                    text_color='red',
                    background_color='black',
                    border_width=2,
                    justification="left"
                    
                )

            ],
            [

                guihandler.Checkbox(
            
                    text=' Enable Traceroute Scan',
                    checkbox_color='black',
                    background_color='black',
                    tooltip='alias nmap --traceroute {targetip} (On Screen Only - No Output)',
                    text_color='red'

                ),

                guihandler.Checkbox(
            
                    text=' Enable IPV6 Scanning',
                    checkbox_color='black',
                    background_color='black',
                    tooltip='alias -6',
                    text_color='red'

                ),

                guihandler.Checkbox(
            
                    text=' Enable OS Detection Guessing',
                    checkbox_color='black',
                    background_color='black',
                    tooltip='alias -O Switch',
                    text_color='red'

                )

            ],
            [

                guihandler.Text(
            
                    text='Service Version Scan Intesity:',
                    text_color='red',
                    background_color='black',
                    expand_x=False,
                    justification="left",
                    tooltip='Accepted Parameters: \n\nNumerical Option: \n-1   = DISABLED \n0-9 = Light Scan - Intense Scan \n\nDefault Value: 5'

                ),

                guihandler.Slider(
            
                    range=(-1,9),
                    text_color='red',
                    background_color='black',
                    trough_color='red',
                    orientation='horizontal',
                    default_value=5,
                    size=(40,20)

                )

            ],
            [

                guihandler.Text(
            
                    text='Scan Timing Preset:',
                    text_color='red',
                    background_color='black',
                    expand_x=False,
                    justification="left",
                    tooltip='Accepted Parameters: \n\nNumerical Option: \n0   = Slow Packet Send Speed \n5 = Send Packets As Fast As Possible \n\nDefault Value: 3'

                ),

                guihandler.Slider(
            
                    range=(0,5),
                    text_color='red',
                    background_color='black',
                    trough_color='red',
                    orientation='horizontal',
                    default_value=3,
                    size=(48,20)

                )

            ],
            [

                guihandler.Text(
                
                    text="\n ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n SPOOFING AND EVASION OPTIONS",
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="center",

                )

            ],
            [

                guihandler.Text(
            
                    text='Spoof Source Address (ipaddr):',
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="left",
                    tooltip='Accepted Parameters: \n\nIP Address: Ex. 192.342.84.109'

                ),

                guihandler.Input(
            
                    text_color='red',
                    background_color='black',
                    border_width=2,
                    justification="left"
                    
                ),

            ],
            [

                guihandler.Text(
            
                    text='Use Specified Source Port (port):',
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="left",
                    tooltip='Accepted Parameters: \n\nPort Number: Ex. 443 \n\nAccepts: Any Port 1-65535'

                ),

                guihandler.Input(
            
                    text_color='red',
                    background_color='black',
                    border_width=2,
                    justification="left"
                    
                )

            ],
            [

                guihandler.Text(
            
                    text='Use A Proxy URL (url):',
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="left",
                    tooltip='Accepted Parameters: \n\nURL/Domain: Ex. https://nmap.org'

                ),

                guihandler.Input(
            
                    text_color='red',
                    background_color='black',
                    border_width=2,
                    justification="left"
                    
                )

            ],
            [

                guihandler.Text(
            
                    text='Spoof MAC Address (macaddr):',
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="left",
                    tooltip='Accepted Parameters: \n\nMAC Address: Ex. 00:B0:D0:63:C2:26'

                ),

                guihandler.Input(
            
                    text_color='red',
                    background_color='black',
                    border_width=2,
                    justification="left"
                    
                )

            ],
            [

                guihandler.Text(
            
                    text='Use A Specified Interface',
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="left",
                    tooltip='Accepted Parameters: \n\nNetwork Interface ID: \nEx. eth0 \nEx. wlan0'

                ),

                guihandler.Input(
            
                    text_color='red',
                    background_color='black',
                    border_width=2,
                    justification="left"
                    
                )

            ],
            [

                guihandler.Checkbox(
            
                    text='Enable Bad CheckSums',
                    checkbox_color='black',
                    background_color='black',
                    tooltip='alias --badsum \n\nSend Packets With Bogus TCP/UDP/SCTP CheckSums',
                    text_color='red'

                )

            ],
            [

                guihandler.Text(
                
                text="\n\n",
                text_color='red',
                background_color='black',
                expand_x=True,
                justification="center",

                )

            ],
            [

                guihandler.Text(
            
                    text='Output Directory',
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="left",
                    tooltip='Accepted Parameters: \n\nDirectory Name: Ex. /home/user/output/scantool/nmap \n\nDo NOT use end slash. \n\nTo Change Output Filename, Press {Edit Configuration}'

                ),

                guihandler.Input(
            
                    text_color='red',
                    background_color='black',
                    border_width=2,
                    justification="left"
                    
                )

            ],
            [

                guihandler.Text(
                
                    text="\n ━━━━━━━━━━━━━━━━━━━━━━",
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="left",

                )

            ],
            [

                guihandler.Button(
            
                    button_text='Execute "NMAP"',
                    border_width=0,
                    button_color=["red","black"],
                    mouseover_colors=["black","red"]

                ),

                guihandler.Button(
            
                    button_text='Edit Configuration',
                    border_width=0,
                    button_color=["red","black"],
                    mouseover_colors=["black","red"]

                ),

                guihandler.Button(
            
                    button_text='Quit Program',
                    border_width=0,
                    button_color=["red","black"],
                    mouseover_colors=["black","red"]

                ),

                guihandler.Listbox(
                    
                    values=nmap_scantype_dropdown_layout,
                    select_mode='LISTBOX_SELECT_MODE_SINGLE',
                    default_values="TCP Syn Scan",
                    sbar_trough_color="black",
                    sbar_arrow_color="red",
                    sbar_frame_color="black",
                    sbar_background_color="black",
                    expand_x=True,
                    size=(2,2),
                    text_color="red",
                    background_color="black",
                    
                )


            ]
            
        ]

        nmap_scrn1 = guihandler.Window(
            
                                      'Enter Nmap Scan Variables',
                                      nmap_scrn1_layout,
                                      background_color='black',
                                      titlebar_text_color='red',
                                      resizable=True
                                      
                                      )

        while True:
            
            event, values = nmap_scrn1.read()
            
            if event == "Quit Program" or event == guihandler.WIN_CLOSED:

                print(colored('\n  Exiting Upon User Request :(\n', color='red', attrs=["bold"]))

                raise SystemExit(1)

            elif event == "Edit Configuration":

                nmap_scrn1.close()

                return "editcnf"
            
            elif event == 'Execute "NMAP"':

                nmap_scrn1.close()

                return values


    def niktoui():

        nikto_scrn1_layout = [

            [

                guihandler.Text(
                    
                    text='TARGET SPECIFICATION',
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="center",
                    
                )

            ],
            [

                guihandler.Text(
                    
                    text='Enter Target Address*:',
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="left",
                    tooltip='(Required) Accepted Parameters: \n\nIP Address: Ex. 10.0.0.1 \nHost/Domain Name: Ex. scanme.nmap.org / odfsec.org'
                    
                ),

                guihandler.Input(
            
                    text_color='red',
                    background_color='black',
                    border_width=2,
                    justification="left"
                    
                )

            ],
            [

                guihandler.Text(
            
                    text='Enter Target Port:',
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="left",
                    tooltip='Accepted Parameters: \n\nSingular Port Number: Ex. 8080 \nDEFAULT = PORT 80 (empty field)'
                ),

                guihandler.Input(
            
                    text_color='red',
                    background_color='black',
                    border_width=2,
                    justification="left"
                    
                )

            ],
            [

                guihandler.Radio (
            
                    text='Use IPV4',
                    group_id="ip_type",
                    default=True,
                    disabled=False,
                    background_color='black',
                    text_color='red',
                    circle_color='black',
                    expand_x=True,
                    tooltip='Connect to target using IPV4'

                ),

                guihandler.Radio (
            
                    text='Use IPV6',
                    group_id="ip_type",
                    default=False,
                    disabled=False,
                    background_color='black',
                    text_color='red',
                    circle_color='black',
                    expand_x=True,
                    tooltip='Connect to target using IPV6'

                ),

                guihandler.Text (
            
                    text='|',
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="center"

                ),

                guihandler.Radio (
            
                    text='Force SSL',
                    group_id="ssl_type",
                    default=False,
                    disabled=False,
                    background_color='black',
                    text_color='red',
                    circle_color='black',
                    expand_x=True,
                    tooltip='Connect to target using IPV6'

                ),

                guihandler.Radio (
            
                    text='Disable SSL',
                    group_id="ssl_type",
                    default=True,
                    disabled=False,
                    background_color='black',
                    text_color='red',
                    circle_color='black',
                    expand_x=True,
                    tooltip='Connect to target using IPV6'

                )

            ],
            [

                guihandler.Text(
                
                    text="\n ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ \nSCAN OPTIONS",
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="center",

                )

            ],
            [

                guihandler.Checkbox (
            
                    text='Over-ride UserAgent',
                    background_color='black',
                    text_color='red',
                    checkbox_color='black',
                    tooltip='Alias to "-useragent" \nOver-rides the default useragent'
                ),

                guihandler.Checkbox (
            
                    text='Use Cookies',
                    background_color='black',
                    text_color='red',
                    checkbox_color='black',
                    tooltip='Alias to "-usecookies" \nUse cookies from responses in future requests'
                ),

                guihandler.Checkbox (
            
                    text='Follow 3XX Redirects',
                    background_color='black',
                    text_color='red',
                    checkbox_color='black',
                    tooltip='Alias to "-followredirects" \nFollow 3xx redirects to new location'
                ),

                guihandler.Checkbox (
            
                    text='No Slash URLs',
                    background_color='black',
                    text_color='red',
                    checkbox_color='black',
                    tooltip='Alias to "-noslash" \nStrip trailing slash from URLs (e.g., "/admin/" to "/admin")'
                )

            ],
            [

                guihandler.Text(
                
                    text="\n ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ \nSCAN TUNING",
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="center",

                )

            ],
            [

                guihandler.Text(
            
                    text='Scan Tuning Option(s):',
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="left",
                    tooltip=' Accepted Parameters: \n\n 1     Interesting File / Seen in logs \n 2     Misconfiguration / Default File \n 3     Information Disclosure \n 4     Injection (XSS/Script/HTML) \n 5     Remote File Retrieval - Inside Web Root \n 6     Denial of Service \n 7     Remote File Retrieval - Server Wide \n 8     Command Execution / Remote Shell \n 9     SQL Injection \n 0     File Upload \n a     Authentication Bypass \n b     Software Identification \n c     Remote Source Inclusion \n d     WebService \n e     Administrative Console \n x     Reverse Tuning Options (i.e., include all except specified) \n\n Accepts multiple parameters (ex. "123456ab")'
                ),

                guihandler.Input(
            
                    text_color='red',
                    background_color='black',
                    border_width=2,
                    justification="left"
                    
                )

            ],
            [

                guihandler.Text(
            
                    text='Scan Evasion Option(s):',
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="left",
                    tooltip=' Accepted Parameters: \n\n 1     Random URI encoding (non-UTF8) \n 2     Directory self-reference (/./) \n 3     Premature URL ending \n 4     Prepend long random string \n 5     Fake parameter \n 6     TAB as request spacer \n 7     Change the case of the URL \n 8     Use Windows directory separator (\) \n A     Use a carriage return (0x0d) as a request spacer \n B     Use binary value 0x0b as a request spacer \n\n Accepts multiple parameters (ex. "12345678AB")'
                ),

                guihandler.Input(
            
                    text_color='red',
                    background_color='black',
                    border_width=2,
                    justification="left"
                    
                )

            ],
            [

                guihandler.Text(
            
                    text='Custom CGI Scan:',
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="left",
                    tooltip=' Accepted Parameters: \n\n "none" "all", or values like "/cgi/ /cgi-a/") \n\n Don`t print "" during input \n Multiple directory spacer: " " (space)'
                ),

                guihandler.Input(
            
                    text_color='red',
                    background_color='black',
                    border_width=2,
                    justification="left"
                    
                )

            ],
            [

                guihandler.Text(
            
                    text='Request Timeout (Seconds):',
                    text_color='red',
                    background_color='black',
                    expand_x=False,
                    justification="left",
                    tooltip=' Accepted Parameters: \n\n Numerical Option: \n 1   = Fast Packet Timeout Speed \n 100 = Slow Packet Timeout Speed \n\n Default Value: 10'

                ),

                guihandler.Slider(
            
                    range=(1,100),
                    text_color='red',
                    background_color='black',
                    trough_color='red',
                    orientation='horizontal',
                    default_value=10,
                    size=(48,20)

                )

            ],
            [

                guihandler.Text(
            
                    text='Scan Pausing (Seconds):',
                    text_color='red',
                    background_color='black',
                    expand_x=False,
                    justification="left",
                    tooltip=' Accepted Parameters: \n\n Numerical Option: \n 0   = Disabled \n 1-100 = Pause For XXX Seconds Between Tests \n\n Default Value: 0'

                ),

                guihandler.Slider(
            
                    range=(0,100),
                    text_color='red',
                    background_color='black',
                    trough_color='red',
                    orientation='horizontal',
                    default_value=0,
                    size=(48,20)

                )

            ],
            [

                guihandler.Text(
                
                    text="\n ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ \nCONNECTION SETTINGS",
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="center",

                )

            ],
            [

                guihandler.Text(
            
                    text='Proxy Settings (http://server:port):',
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="left",
                    tooltip=' Accepted Parameters: \n\n http://server:port'
                ),

                guihandler.Input(
            
                    text_color='red',
                    background_color='black',
                    border_width=2,
                    justification="left"
                    
                )

            ],
            [

                guihandler.Text(
            
                    text='VHost Settings:',
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="left",
                    tooltip=' Accepted Parameters: \n\n Virtual Host'
                ),

                guihandler.Input(
            
                    text_color='red',
                    background_color='black',
                    border_width=2,
                    justification="left"
                    
                )

            ],
            [

                guihandler.Text(
            
                    text='Host Authentication:',
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="left",
                    tooltip=' Accepted Parameters: \n\n id:pass or id:pass:realm'
                ),

                guihandler.Input(
            
                    text_color='red',
                    background_color='black',
                    border_width=2,
                    justification="left"
                    
                )

            ],
            [

                guihandler.Text(
            
                    text='Host Certificate Key File:',
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="left",
                    tooltip=' Accepted Parameters: \n\n File Location For Key File'
                ),

                guihandler.Input(
            
                    text_color='red',
                    background_color='black',
                    border_width=2,
                    justification="left"
                    
                )

            ],
            [

                guihandler.Text(
                
                text="\n\n",
                text_color='red',
                background_color='black',
                expand_x=True,
                justification="center",

                )

            ],
            [

                guihandler.Text(
            
                    text='Output Directory:',
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="left",
                    tooltip=' Accepted Parameters: \n\n id:pass or id:pass:realm'
                ),

                guihandler.Input(
            
                    text_color='red',
                    background_color='black',
                    border_width=2,
                    justification="left"
                    
                )

            ],
            [

                guihandler.Text(
                
                    text="\n ━━━━━━━━━━━━━━━━━━━━━━",
                    text_color='red',
                    background_color='black',
                    expand_x=True,
                    justification="left",

                )

            ],
            [

                guihandler.Button(
                
                    button_text='Execute NIKTO',
                    border_width=0,
                    button_color=["red","black"],
                    mouseover_colors=["black","red"]

                ),

                    guihandler.Button(
                
                    button_text='Edit Configuration',
                    border_width=0,
                    button_color=["red","black"],
                    mouseover_colors=["black","red"]

                ),

                    guihandler.Button(
                
                    button_text='Quit Program',
                    border_width=0,
                    button_color=["red","black"],
                    mouseover_colors=["black","red"]

                )

            ]
            
        ]

        nikto_scrn1 = guihandler.Window(
            
                                      'Enter Nikto Scan Variables',
                                      nikto_scrn1_layout,
                                      background_color='black',
                                      titlebar_text_color='red',
                                      resizable=True
                                      
                                      )
        
        while True:
            
            event, values = nikto_scrn1.read()
            
            if event == "Quit Program" or event == guihandler.WIN_CLOSED:

                print(colored('\n  Exiting Upon User Request :(\n', color='red', attrs=["bold"]))

                raise SystemExit(1)

            elif event == "Edit Configuration":

                nikto_scrn1.close()

                return "editcnf"

            elif event == "Execute NIKTO":

                nikto_scrn1.close()

                return values
            


class stouterr_handl():

    def check_output(errorid):

        if errorid == "no_defined_output_stream_location":

            print(colored('\n  [!] Error: No Output Directory Was Defined Via The GUI!\n', color='red', attrs=["bold"]))
        
            raise SystemExit(2)
        
        elif errorid == "no_defined_target":

            print(colored('\n  [!] Error: No Target Address Was Defined Via The GUI!\n', color='red', attrs=["bold"]))

            raise SystemExit(2)
        
        elif errorid == "no_defined_port":

            print(colored('\n  [!] Error: No Target Port Was Defined Via The GUI!\n', color='red', attrs=["bold"]))

            raise SystemExit(2)
        
    def check_output_stream(output_location):

        if os.path.isdir(output_location):
                            
            print(colored(f'\n  [!] Output Stream @ {output_location} Is Usable!\n', color='green', attrs=["bold"]))

        else:

            makepath = f"mkdir -p {output_location}"

            print(colored(f'\n  [!] Warning: The Output Stream Location Defined ({output_location} Is Non Existent!\n)', color='yellow', attrs=["bold"]))
            print(colored('\n      Input "yes" To Create Missing Directory, Or "exit" To Quit. ', color='blue', attrs=["bold"]), end=" ")
            
            dirinput = input(colored('> ', color='blue', attrs=["bold"]))

            if dirinput == "yes":

                print(colored(f'\n  [!] Creating Directory ({makepath}) ', color='blue', attrs=["bold"]))

                subprocess.call(makepath, shell=True)

            elif dirinput == "exit":

                raise SystemExit(2)



class cmdgen():

    def cmdgen_nmap(values):

        print(colored('  Generating Command... Please Wait...', color='blue', attrs=["bold"]))

        global output_location
        global host_command
        global targetaddress
        global targetport
        global traceroute_cmd

        targetaddress = values[0]
        targetport = values[1]
        output_location = values[15]
        values[7] = math.trunc(values[7])
        values[8] = math.trunc(values[8])

        host_command = "nmap"
        host_command_root_apx = "nmap"

        if not values[0]:

            stouterr_handl.check_output(errorid='no_defined_target')

        if not values[1]:

            stouterr_handl.check_output(errorid='no_defined_port')

        if not values[15]:

            stouterr_handl.check_output(errorid='no_defined_output_stream_location')

        else:

            stouterr_handl.check_output_stream(values[15])

        if not values[2]:

            if scriptenabler_nmap_nsescriptscan == "True":

                values[2] = 'default'

                print(colored(f'  [!] Missing Values For NSE Method: Using Default Value: "{values[2]}"', color='yellow', attrs=["bold"]))
                        
            else:
 
                values[2] = ''

        if values[1]:

            host_command = host_command + ' -p "' + targetport + '" '

        if values[2]:

            if scriptenabler_nmap_nsescriptscan == "True":

                host_command = host_command + '--script="' + values[2] + '" '

            if scriptenabler_nmap_nsedebug == "True":

                host_command = host_command + "--script-trace "

        if values[3]:

            if scriptenabler_nmap_nsescriptscan == "True":

                host_command = host_command + "--script-args-file=" + '"' + values[3] + '" '

        if str(values[4]) == "True":

            traceroute_cmd = "True"

        else:
                    
            traceroute_cmd = "False"

        if values[5]:

            host_command = host_command + "-6 "

        if str(values[6]) == "True":

            host_command = host_command + "-O "

        if str(values[7]) == "-1":

            host_command = host_command

        else:

            host_command = host_command + "-sV " "--version-intensity " + str(values[7]) + " "

        if values[8]:

            host_command = host_command + "-T" + str(values[8]) + " "

        if values[9]:

            host_command = host_command + "-S " + values[9] + " "

        if values[10]:

            host_command = host_command + "--source-port " + values[10] + " "

        if values[11]:

            host_command = host_command + "--proxies " + values[11] + " "

        if values[12]:

            host_command = host_command + '--spoof-mac "' + values[12] + '" '

        if values[13]:

            host_command = host_command + "-e " + values[13] + " "

        if str(values[14]) == "True":

            host_command = host_command + "--badsum "

        if str(values[16]) == "['TCP Syn Scan']":

            host_command = host_command + "-sS "
                
        elif str(values[16]) == "['Connect() Scan']":

            host_command = host_command + "-sT "

        elif str(values[16]) == "['ACK Scan']":

            host_command = host_command + "-sA "

        elif str(values[16]) == "['Window Scan']":

            host_command = host_command + "-sW "
                
        elif str(values[16]) == "['Maimon Scan']":

            host_command = host_command + "-sM"

        elif str(values[16]) == "['UDP Scan']":

            host_command = host_command + "-sU "
                
        elif str(values[16]) == "['TCP Null Scan']":

            host_command = host_command + "-sN "

        elif str(values[16]) == "['FIN Scan']":

            host_command = host_command + "-sF "

        elif str(values[16]) == "['Xmas Scan']":

            host_command = host_command + "-sX "

        else:

            print(colored(f'\nError: Could Not Parse Selected Scan Type... Exiting (2)"{targetaddress}"', color='red', attrs=["bold"]))

            SystemExit(2)

        if scriptenabler_nmap_permuser == "True":

            host_command = host_command + "--privileged "

        elif scriptenabler_nmap_permuser == "False":

            host_command = host_command + "--unprivileged "

        else:

            host_command = host_command

        if values[15]:

            host_command = host_command + "-oN " + values[15] + "/" + scriptoutput_nmap_fullscan + " "

        if targetaddress:

            host_command = host_command + targetaddress

        print(colored('  [!] CMDGen Complete!', color='green', attrs=["bold"]))

        if scriptenabler_nmap_updatedb == "True":

            print(colored(f'\nChecking For NSE Script Database Updates', color='red', attrs=["bold"]))
            print(colored(f'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n', color='red', attrs=["bold"]))

            command_to_execute = host_command_root_apx + " --script-updatedb"
            subprocess.call(command_to_execute, shell=True)

        if traceroute_cmd == "True":

            print(colored(f'\nGathering Traceroute Data \nTarget: "{targetaddress}"', color='red', attrs=["bold"]))
            print(colored(f'━━━━━━━━━━━━━━━━━━━━━━━━━━━\n', color='red', attrs=["bold"]))

            command_to_execute = host_command_root_apx + " --traceroute " + targetaddress
            subprocess.call(command_to_execute, shell=True)

        if scriptenabler_nmap_host == "True":

            command_to_execute = host_command

            print(colored(f'\nExecuting Full Scan \nTarget: "{targetaddress}"', color='red', attrs=["bold"]))
            print(colored(f'━━━━━━━━━━━━━━━━━━━━━\n\n', color='red', attrs=["bold"]))
            print(colored(f'{command_to_execute}\n', color='red', attrs=["bold"]))
                    
            subprocess.call(command_to_execute, shell=True)

        raise SystemExit(0)
    


    def cmdgen_nikto(values):

        print(colored('  Generating Command... Please Wait...', color='blue', attrs=["bold"]))

        global output_location
        global host_command
        global targetaddress
        global targetport

        targetaddress = values[0]
        targetport = values[1]
        output_location = values[19]
        values[13] = math.trunc(values[13])
        values[14] = math.trunc(values[14])

        host_command = "nikto"

        if not values[0]:
              
            stouterr_handl.check_output(errorid='no_defined_target')

        if not values[19]:
              
            stouterr_handl.check_output(errorid='no_defined_output_stream_location')

        else:
              
            stouterr_handl.check_output_stream(values[19])

        if values[0]:

            host_command = host_command + ' -host "' + targetaddress +'" '

        if values[1] == "":

            host_command = host_command

        else:

            host_command = host_command + '-port "' + values[1] + '" '

        if values[2] == True:

            host_command = host_command + '-ipv4 '

        else:

            host_command = host_command + '-ipv6 '

        if values[4] == True:

            host_command = host_command + '-ssl '

        else:
                    
            host_command = host_command + '-nossl '

        if values[6] == True:

            host_command = host_command + '-useragent '

        else:

            host_command = host_command

        if values[7] == True:

            host_command = host_command + '-usecookies '

        else:
                    
            host_command = host_command

        if values[8] == True:

            host_command = host_command + '-followredirects '

        else:

            host_command = host_command

        if values[9] == True:

            host_command = host_command + '-noslash '

        else:

            host_command = host_command

        if values[10]:

            host_command = host_command + '-Tuning "' + values[10] + '" '

        else:

            host_command = host_command

        if values[11]:

            host_command = host_command + '-evasion "' + values[11] + '" '

        else:

            host_command = host_command

        if values[12]:

            host_command = host_command + '-Cgidirs "' + values[12] + '" '

        else:

            host_command = host_command

        if values[13]:

            host_command = host_command + '-timeout "' + str(values[13]) + '" '

        if values[14]:

            host_command = host_command + '-Pause "' + str(values[14]) + '" '

        if values[15]:
                
            host_command = host_command + '-useproxy "' + values[15] + '" '

        else:
                    
            host_command = host_command

        if values[16]:

            host_command = host_command + '-vhost "' + values[16] + '" '

        else:

            host_command = host_command

        if values[17]:

            host_command = host_command + '-id "' + values[17] + '" '

        else:

            host_command = host_command

        if values[18]:

            host_command = host_command + '-key "' + values[18] + '" '

        else:

            host_command = host_command

        if scriptenabler_nikto_nointeractive == "True":

            host_command = host_command + '-nointeractive '

        host_command = host_command + '-Display "' + scriptenabler_nikto_displaytype +'" ' + '-o "' + output_location + '/' + scriptoutput_nikto_default + '" ' + '-Format "' + scriptoutput_nikto_format +'"'

        print(colored('  [!] CMDGen Complete!', color='green', attrs=["bold"]))
        
        print(colored('\nRunning Nikto!', color='red', attrs=["bold"]))
        print(colored('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n', color='red', attrs=["bold"]))
                
        print(colored(host_command, color='red', attrs=["bold"]))
        print('\n')

        command_to_execute = host_command
        subprocess.call(command_to_execute, shell=True)

        raise SystemExit(0)