import sys
import subprocess
import pathlib

base_path = pathlib.Path(__file__).parent.absolute()

CMDS = {
  'MediaInfo': [R"D:\Programs\Utils\Media Info\MediaInfo.exe"],
  'HashCalc': [R"D:\Programs\Utils\HashCalc\HashCalc.exe"],
}

ERROR_CMD = [R'C:\Windows\py.exe', base_path / 'error.py']

def error(out):
  process = subprocess.Popen(ERROR_CMD + out, creationflags = subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP)

if __name__ == '__main__':
  try:
    
    if len(sys.argv) < 2:
      error(['execute.py - no command supplied'] + sys.argv)
      exit(1)

    cmd = sys.argv[1]
    files = sys.argv[2:]
    
    if (loc:=cmd.find(' - ')) >= 0:
      cmd = cmd[loc+3:]
    
    print(cmd, files)
    
    if cmd in CMDS:
      process = subprocess.Popen(CMDS[cmd] + files, creationflags = subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP)
      print(f'process cmd: {CMDS[cmd]}')
    else:
      error([f'execute.py - unknown cmd: {cmd}'] + [cmd] + files)
    
  except:
    import traceback
    error(['execute.py - error', traceback.format_exc()])
