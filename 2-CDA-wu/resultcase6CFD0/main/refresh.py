# get e script to refresh the call_componnets in shishimujoco.

import os
import time 
import shutil #this is for operating the folder 

class refresh():
    script_folder = 'C:/Users/106/Desktop/EnglishMulu/testCDA1/main'
    target_folder = 'C:/Users/106/.conda/envs/shishimujoco/Lib'
    def go_file(self):
        # os.remove(self.target_folder+'/call_components.py')
        shutil.copyfile(self.script_folder+'/call_components.py' , self.target_folder+'/call_components.py')
        shutil.copyfile(self.script_folder+'/time_out.py' , self.target_folder+'/time_out.py')
    def go_env(self):
        # try to install env here.
        print('MXairfoil: it looks not easy to install env here. zhao bao')

if __name__=="__main__":
    zou = refresh()
    zou.go_file()



