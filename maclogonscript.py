# $language = "python"
# $interface = "1.0"

import SecureCRT

def Main():

    # turn on synchronous mode so we don't miss any data
    crt.Screen.Synchronous = True

    crt.Screen.WaitForString("Last login: ")

    crt.Screen.Send("export LANG=zh_CN.UTF-8\r")
    crt.Screen.Send("clear\r")

    # turn off synchronous mode to restore normal input processing
    crt.Screen.Synchronous = False

Main()
