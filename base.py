import socket
import win32serviceutil
import servicemanager
import win32event
import win32service

class SMWinservice(win32serviceutil.ServiceFramework):
  _svc_name = 'pythonService'
  _svc_display_name_ = 'Python Service'
  _svc_description_ = 'Python Service Description'