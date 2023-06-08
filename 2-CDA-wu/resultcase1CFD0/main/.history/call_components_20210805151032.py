# trying to call IGG with scripts.
# in fact no need for another .py file.
# 20210407 further modification for parallel.

import os
import time 
import shutil #this is for operating the folder 
import eventlet #this is for time out
import time_out # this is after all for time out.
import numpy as np 
import subprocess

class call_components:
    # these location will change according to different object of this class
    script_folder = 'C:/Users/106/Desktop/EnglishMulu/testCDA1'
    matlab_location = 'C:/Users/106/Desktop/EnglishMulu/MXairfoilCDA'
    IGG_script_name = script_folder+'/testCDA1.py'
    Turbo_script_name = script_folder+'/testCDA1_Turbo.py'
    Turbo_case_name = script_folder+'/testCDA1/testCDA1_computation_1/testCDA1_computation_1.run'
    CFView_script_name = script_folder+'/testCDA1_post.py'

    log_location = script_folder+'/main/log'
    result_folder = script_folder+'/testCDA1/jieguo'
    #these will change when switch te computer.
    IGG_location = 'C:/NUMECA_SOFTWARE/fineturbo/fine141/bin64'
    Turbo_location = IGG_location
    CFView_location = IGG_location

    def __init__(self,raw_script_folder,raw_matlab_folder):
        #initialize. copy folder.
        # first, get a name.
        self.raw_script_folder = raw_script_folder
        self.raw_matlab_folder = raw_matlab_folder
        i=1 
        # while ((i<1000)&(os.path.exists(self.script_folder)|os.path.exists(self.matlab_location))):
        while ((i<1000)&(os.path.exists(self.matlab_location))):
            # self.script_folder =  raw_script_folder + str(i)
            self.matlab_location = raw_matlab_folder + str(i)            
            try:
                shutil.copytree(raw_matlab_folder,self.matlab_location)
                # shutil.copytree(raw_script_folder,self.script_folder)
                i=1001
            except:
                i=i+1     
        i=1
        while ((i<1000)&(os.path.exists(self.script_folder))):
            self.script_folder =  raw_script_folder + str(i)
            try:
                shutil.copytree(raw_script_folder,self.script_folder)
                i=1001
            except:
                i=i+1

            #if there is MXairfoilCDA1, then use MXairfoilCDA2        
        # shutil.copytree(raw_matlab_folder,self.matlab_location)
        # shutil.copytree(raw_script_folder,self.script_folder)

        self.IGG_script_name = self.script_folder+'/testCDA1.py'
        self.Turbo_script_name = self.script_folder+'/testCDA1_Turbo.py'
        self.Turbo_case_name = self.script_folder+'/testCDA1/testCDA1_computation_1/testCDA1_computation_1.run'
        self.CFView_script_name = self.script_folder+'/testCDA1_post.py'
    
        self.log_location = self.raw_script_folder+'/main/log'
        self.result_folder = self.script_folder+'/testCDA1/jieguo'

        #get something to know done. if it is true, no need to continue.
        self.done = 0

        #caonima! cao ! 
        self.set_scripts('testCDA1.py')
        self.set_scripts('testCDA1_Turbo.py')
        self.set_scripts('testCDA1_Post.py')


    
    def __del__(self):
        # #move the ptr out of the temp dir. Or the temp dir can not be deleted.
        # os.chdir(self.raw_matlab_folder)
        # #delet temp files here.
        # shutil.rmtree(self.matlab_location)
        # shutil.rmtree(self.script_folder)
        # print('MXairfoil: successfully remove the temp file')
        # time.sleep(3)
        try:
            #move the ptr out of the temp dir. Or the temp dir can not be deleted.
            os.chdir(self.raw_matlab_folder)
            #delet temp files here.
            shutil.rmtree(self.matlab_location)
            shutil.rmtree(self.script_folder)
            print('MXairfoil: successfully remove the temp file using __del__ in call_components')
        except OSError as e:
            print('MXairfoil: fail to remove the temp file in __del__ in call_components')
            print(e)

    def del_gai(self):
        try:
            #move the ptr out of the temp dir. Or the temp dir can not be deleted.
            os.chdir(self.raw_matlab_folder)
            #delet temp files here.
            shutil.rmtree(self.matlab_location)
            shutil.rmtree(self.script_folder)
            print('MXairfoil: successfully remove the temp file using del_gai in call_components')
        except OSError as e:
            print('MXairfoil: fail to remove the temp file in del_gai in call_components')
            print(e)

    def clear(self):
        # #move the ptr out of the temp dir. Or the temp dir can not be deleted.
        # os.chdir(self.raw_matlab_folder)
        # #delet temp files here.
        # shutil.rmtree(self.matlab_location)
        # shutil.rmtree(self.script_folder)
        # print('MXairfoil: successfully remove the temp file')
        time.sleep(3)
        try:
            #move the ptr out of the temp dir. Or the temp dir can not be deleted.
            os.chdir(self.raw_matlab_folder)
            #delet temp files here.
            shutil.rmtree(self.matlab_location)
            shutil.rmtree(self.script_folder)
            print('MXairfoil: successfully remove the temp file using clear')
        except:
            print('MXairfoil: fail to remove the temp file in clear')

    def clear_all(self,raw_script_folder,raw_matlab_folder):
        i=1
        while (i<100):
            clear_script_folder =  raw_script_folder + str(i)
            clear_matlab_location = raw_matlab_folder + str(i)
            if (clear_script_folder != self.script_folder)&(clear_matlab_location != self.matlab_location):
                try:
                    shutil.rmtree(clear_matlab_location)
                    print('MXairfoil: clear_matlab_location successfully')
                except:
                    print('MXairfoil: clear_matlab_location fail, i='+str(i))
                try:
                    shutil.rmtree(clear_script_folder)
                    print('MXairfoil: clear_script_folder successfully')
                except:
                    print('MXairfoil: clear_script_folder fail, i='+str(i))
            # elif clear_script_folder == self.script_folder:

            i=i+1
            #if there is MXairfoilCDA1, then use MXairfoilCDA2
    
    def reset(self):
        # this is to reset the class. Just copy from raw folder again.
        os.chdir(self.raw_matlab_folder) # run out before delet.
        try:
            shutil.rmtree(self.matlab_location)
            shutil.rmtree(self.script_folder)
            shutil.copytree(self.raw_matlab_folder,self.matlab_location)
            shutil.copytree(self.raw_script_folder,self.script_folder)
        except:
            strbuffer = 'MXairfoil: cannot reset. fail to remove the temp file. \n' + self.matlab_location + '\n'+self.script_folder
            self.jilu(strbuffer)
            # shutil.copytree(self.raw_matlab_folder,self.matlab_location)
            # shutil.copytree(self.raw_script_folder,self.script_folder)
            # avoid deleting part of file 

    # @time_out.time_out(60, time_out.callback_func)
    def execute_go(self,command):
        #universal command execute, with time out.
        # os.system(command)

        # a newer way to call command using subporcess model.
        if self.done !=0:
            print('MXairfoil: wan nima, zhaoba in execute_go')
            # os.system('pause')
        try:
            jieguo = subprocess.run(command, stdin=None, input=None, stdout=subprocess.DEVNULL, stderr=None, shell=False, timeout=100, check=True)
            #stdout=subprocess.DEVNULL for no output from NUMECA
            #stdout = None for all of the output. using it when debugging.
        except  subprocess.CalledProcessError :
            print('MXairfoil: something really wrong when calling outside process')
            jieguo = 'MXairfoil: running a lonliness'
            # os.system('pause')

        return jieguo.returncode # cannot return subprocess.CompletedProcess, I don't know why. So, returning a returncode.

    # @time_out.time_out(60, time_out.callback_func)
    def call_matlab(self):
        # this is for calling matlab, to get a new airfoil from parameters.
        # exe_location = 'C:/Users/y/Desktop/自动生成几何二维CDA/code'
        self.done = 0 
        matlab_location = self.matlab_location
        matlab_name = matlab_location + '/code/shishi_main4.exe' 
        print('MXairfoil: exe name is: ')
        print(matlab_name)
        os.chdir(matlab_location+'/code')
        flag = os.path.exists(matlab_name)
        if flag == 0:
            print('MXairfoil: did not exist.')
            return 
        mingling = matlab_name + ' '+ matlab_location
        sec_timeout = 100 
        t = eventlet.Timeout(sec_timeout,False)
        time_start = time.time()
        try:
            # os.system(matlab_name)
            jieguo = self.execute_go(mingling)

            if jieguo !=  0:
                # which means matlab exits with exception
                self.done = 1
                strbuffer = 'MXairfoil : matlab running a loneliness'+ self.matlab_location
                self.jilu(strbuffer)
        except eventlet.timeout.Timeout as e:
            strbuffer = 'MXairfoil : matlab time out. last step are used for continue. sec_timeout = '+str(sec_timeout)
            self.jilu(strbuffer)
            self.done=1
        finally:
            t.cancel()
        time_end = time.time()

        if((time_end-time_start)>sec_timeout):
            #even if I can't do exit, at least I can remember
            self.done = 1
            strbuffer = 'MXairfoil : matlab time out. last step are used for continue. sec_timeout = '+str(sec_timeout)
            self.jilu(strbuffer)


        # move the data from matlab to NUMECA
        try:
            os.remove(self.script_folder+'/pressure.dat')
            os.remove(self.script_folder+'/pressure2.dat')
            os.remove(self.script_folder+'/pressure3.dat')
            os.remove(self.script_folder+'/suction.dat')
            os.remove(self.script_folder+'/suction2.dat')
            os.remove(self.script_folder+'/suction3.dat')
        except:
            rizhi ='MXairfoil: unkonwn error when cleanning old airfoil'
            self.jilu(rizhi)
            self.done = 1
            # os.system('pause')
        
        try:
            shutil.move(self.matlab_location+'/output/CDA1/pressure.dat',self.script_folder)
            shutil.move(self.matlab_location+'/output/CDA1/pressure2.dat',self.script_folder)
            shutil.move(self.matlab_location+'/output/CDA1/pressure3.dat',self.script_folder)
            shutil.move(self.matlab_location+'/output/CDA1/suction.dat',self.script_folder)
            shutil.move(self.matlab_location+'/output/CDA1/suction2.dat',self.script_folder)
            shutil.move(self.matlab_location+'/output/CDA1/suction3.dat',self.script_folder)
        except:
            rizhi ='MXairfoil: unkonwn error when generate airfoil'
            self.jilu(rizhi)
            self.done = 1
            # os.system('pause')


        print('MXairfoil: finish generate the airfoil. En Taro XXH!')
        print('(time cost:',time_end-time_start,'s)')

    # @time_out.time_out(60, time_out.callback_func)
    def call_IGG(self):
        if self.done == 1:
            rizhi = 'MXairfoil: no need to continue calling IGG for something wrong before.'
            self.jilu(rizhi)
            return
        exe_location = self.IGG_location
        exe_name = exe_location + '/iggx86_64.exe' 
        print('MXairfoil: exe name is: ')
        print(exe_name)
        script_name = self.IGG_script_name
        print('MXairfoil: script name is: ')
        print(script_name)
        mingling = exe_name + ' '+'-batch -script' + ' ' + script_name
        flag = 1
        flag = flag & os.path.exists(exe_name)& os.path.exists(script_name)
        if flag == 0:
            print('MXairfoil: something did not exist.')
            self.done = 1
            return
        
        os.chdir(self.script_folder)
        sec_timeout = 59 
        t = eventlet.Timeout(sec_timeout,False)
        time_start = time.time()
        try:
            # os.system(mingling)
            jieguo = self.execute_go(mingling)

            if jieguo != 0:
                # which means matlab exits with exception
                self.done = 1
                strbuffer = 'MXairfoil : IGG running a loneliness'+ self.IGG_location
                self.jilu(strbuffer)
                return 
        except eventlet.timeout.Timeout as e:
            strbuffer = 'MXairfoil : IGG time out. last step are used for continue. sec_timeout = '+str(sec_timeout)
            self.jilu(strbuffer)
            self.done=1
        finally:
            t.cancel()
        time_end = time.time()

        if((time_end-time_start)>sec_timeout):
            #even if I can't do exit, at least I can remember
            self.done = 1
            strbuffer = 'MXairfoil : matlab time out. last step are used for continue. sec_timeout = '+str(sec_timeout)
            self.jilu(strbuffer)

        print('MXairfoil: finish generate the mesh. En Taro XXH!')
        print('(time cost:',time_end-time_start,'s)')

    # @time_out.time_out(300, time_out.callback_func)
    def call_Turbo(self):
        if self.done == 1:
            rizhi = 'MXairfoil: no need to continue calling Turbo for something wrong before.'
            self.jilu(rizhi)
            return
        exe_location = self.Turbo_location
        exe_name = exe_location + '/finex86_64.exe' 
        print('MXairfoil: exe name is: ')
        print(exe_name)
        script_name = self.Turbo_script_name
        print('MXairfoil: script name is: ')
        print(script_name)
        mingling = exe_name + ' '+'-script' + ' ' + script_name+' -batch'
        # mingling = exe_name + ' '+'-script' + ' ' + script_name
        print('MXairfoil: mingling is: ')
        print(mingling)
        os.chdir(self.script_folder)
        sec_timeout = 59 
        t = eventlet.Timeout(sec_timeout,False)
        time_start = time.time()
        try:
            # os.system(mingling)
            jieguo = self.execute_go(mingling)
            if jieguo!= 0:
                # which means matlab exits with exception
                self.done = 1
                strbuffer = 'MXairfoil : Turbo running a loneliness'
                self.jilu(strbuffer)
                return 
        except eventlet.timeout.Timeout as e:
            strbuffer = 'MXairfoil : Turbo time out. last step are used for continue. sec_timeout = '+str(sec_timeout)
            self.jilu(strbuffer)
            self.done=1
        finally:
            t.cancel()
        time_end = time.time()

        if((time_end-time_start)>sec_timeout):
            #even if I can't do exit, at least I can remember
            self.done = 1
            strbuffer = 'MXairfoil : Turbo time out. last step are used for continue. sec_timeout = '+str(sec_timeout)
            self.jilu(strbuffer)
            mingling = 'taskkill /F /IM finex86_64.exe'
            os.system(mingling)

        print('MXairfoil: finish generate the case. En Taro XXH!')
        print('(time cost:',time_end-time_start,'s)')   

        #then call euranus to calculate.
        # exe_location = self.Turbo_location
        exe_name = exe_location + '/euranusx86_64.exe' 
        print('MXairfoil: exe name is: ')
        print(exe_name)
        case_name = self.Turbo_case_name
        print('MXairfoil: case_name name is: ')
        print(case_name)
        mingling = exe_name + ' ' + case_name+' -seq'
        print('MXairfoil: mingling is: ')
        print(mingling)
        flag = 1
        flag = flag & os.path.exists(exe_name)& os.path.exists(case_name)
        if flag == 0:
            print('MXairfoil: something did not exist.')
            return
        
        sec_timeout = 59 
        t = eventlet.Timeout(sec_timeout,False)
        time_start = time.time()
        try:
            # os.system(mingling)
            self.execute_go(mingling)
            if jieguo!= 0:
                # which means turbo exits with exception
                self.done = 1
                strbuffer = 'MXairfoil : euranus running a loneliness'
                self.jilu(strbuffer)
                return 
        except eventlet.timeout.Timeout as e:
            strbuffer = 'MXairfoil : euranus time out. last step are used for continue. sec_timeout = '+str(sec_timeout)
            self.jilu(strbuffer)
            self.done=1
        finally:
            t.cancel()
        time_end = time.time()
        if((time_end-time_start)>sec_timeout):
            #even if I can't do exit, at least I can remember
            self.done = 1
            strbuffer = 'MXairfoil : matlab time out. last step are used for continue. sec_timeout = '+str(sec_timeout)
            self.jilu(strbuffer)
        
        print('MXairfoil: finish calculate. En Taro XXH!')
        print('(time cost:',time_end-time_start,'s)')

    # @time_out.time_out(60, time_out.callback_func)
    def call_CFView(self):
        if self.done == 1:
            rizhi = 'MXairfoil: no need to continue calling CFView for something wrong before.'
            self.jilu(rizhi)
            return
        exe_location = self.CFView_location
        exe_name = exe_location + '/cfviewx86_64.exe' 
        print('MXairfoil: exe name is: ')
        print(exe_name)
        script_name = self.CFView_script_name
        print('MXairfoil: script name is: ')
        print(script_name)
        mingling = exe_name + ' '+'-macro' + ' ' + script_name 
        print(mingling)
        flag = 1
        flag = flag & os.path.exists(exe_name)& os.path.exists(script_name)
        if flag == 0:
            print('MXairfoil: something did not exist.')
            return
        os.chdir(self.script_folder)

        sec_timeout = 59
        time_start = time.time()
        # os.system(mingling)
        jieguo = self.execute_go(mingling)
        if jieguo!= 0:
                # which means matlab exits with exception
                self.done = 1
                strbuffer = 'MXairfoil : IGG running a loneliness'+ self.IGG_location
                self.jilu(strbuffer)
                return 
        time_end = time.time()

        if((time_end-time_start)>sec_timeout):
            #even if I can't do exit, at least I can remember
            self.done = 1
            strbuffer = 'MXairfoil : matlab time out. last step are used for continue. sec_timeout = '+str(sec_timeout)
            self.jilu(strbuffer)
            mingling = 'taskkill /F /IM cfviewx86_64.exe'
            os.system(mingling)

        
        print('MXairfoil: finish post process. En Taro XXH!')
        print('(time cost:',time_end-time_start,'s)')
       
    def jilu(self,strBuffer):
        shijian = time.strftime("%Y-%m-%d", time.localtime()) 
        wenjianming = self.log_location+shijian+'.txt'
        rizhi = open(wenjianming,'a')
        rizhi.write(strBuffer+'\n')
        rizhi.write(time.ctime())
        rizhi.write('\n')
        rizhi.close()
        print(strBuffer)
        return

    def jilu_data(self,data):
        #store some data.
        shijian = time.strftime("%Y-%m-%d", time.localtime()) 
        wenjianming = self.log_location+shijian+'data.txt'
        wenjian = open(wenjianming,'a')
        wenjian.write(data + '\n')
        wenjian.close()
        return

    def get_value(self):
        if self.done == 1:
            rizhi = 'MXairfoil: no need to continue calling get_value for something wrong before. pause'
            self.jilu(rizhi)
            os.system('pause')
            return 0,0
        result_folder = self.result_folder
        omega_name = result_folder+'/omega.dat'
        rise_name = result_folder+'/rise.dat'
        omega_file = open(omega_name,'r')
        omega= float(omega_file.read())
        omega_file.close()
        rise_file = open(rise_name,'r')
        rise=float(rise_file.read())
        print('MXairfoil: in this turn, omega = ',omega,'  rise =', rise)
        return omega,rise

    def set_value(self,value,value_name):
        # value_name=self.matlab_location + '/input/CDA1/'+value_name+'.txt'
        # value_file = open(value_name,'w')
        # value_file.write(str(value))
        # value_file.close()
        try:
            value_name=self.matlab_location + '/input/CDA1/'+value_name+'.txt'
            value_file = open(value_name,'w')
            value_file.write(str(value))
            value_file.close()
            shuofa = 'MXairfoil: in this turn, value = '+ str(value)+'  location ='+ value_name
        except:
            shuofa = 'MXairfoil: fail to set the value, location ='+ value_name
        # self.jilu(shuofa)

    def get_value2(self,value_name):
        # value_file = open(value_name,'r')
        # value= float(value_file.read())
        # value_file.close()
        # print('MXairfoil: get the value, value = ',value,'  location =', value_name)
        try:
            value_file = open(value_name,'r')
            value= float(value_file.read())
            value_file.close()
            print('MXairfoil: get the value, value = ',value,'  location =', value_name)
        except:
            value = 0 
            print('MXairfoil: fail to get_value2 ',value,'  location =', value_name)
        return value 

    def set_scripts(self,name):
        #caonima, gang xiehao ceshihao,jieguo ziji buzaile ,xianzia haiyao chongxin xieyibian, wo tama zhende shi rilegoule cao. caocaocaocaocoacao.
        wenjian = open(self.script_folder+'/'+name,'r')
        neirong = wenjian.read()
        wenjian.close()
        index = neirong.find('\n')
        bianliang_add = 'mulu = \'' + self.script_folder+'\''
        if name.count('Post')>0:
            index = neirong.find('\n',index+1)
            bianliang_add = 'CFViewBackward(1210,) \n'+bianliang_add 

        neirong2 = bianliang_add + neirong[index:]
        wenjian = open(self.script_folder+'/'+name,'w')
        wenjian.write(neirong2)
        wenjian.close()

        print('MXairfoil: caonima!')


    def test_existing_case(self,i):
        #just test existing case.
        self.matlab_location = self.raw_matlab_folder + str(i)
        self.script_folder =  self.raw_script_folder + str(i)
        self.IGG_script_name = self.script_folder+'/testCDA1.py'
        self.Turbo_script_name = self.script_folder+'/testCDA1_Turbo.py'
        self.Turbo_case_name = self.script_folder+'/testCDA1/testCDA1_computation_1/testCDA1_computation_1.run'
        self.CFView_script_name = self.script_folder+'/testCDA1_post.py'
    
        self.log_location = self.raw_script_folder+'/main/log'
        self.result_folder = self.script_folder+'/testCDA1/jieguo'

if __name__=="__main__":
    # this is for test the temp file.
    script_folder = 'C:/Users/106/Desktop/EnglishMulu/testCDA1'
    matlab_location = 'C:/Users/106/Desktop/EnglishMulu/MXairfoilCDA'
    shishi = call_components(script_folder,matlab_location)
    flag = 0
    if flag == 0 :
        #do one loop of CFD
        # shishi.set_value(0.4,'tethk')
        # shishi.call_matlab()
        # shishi.call_IGG()
        while 1 :
            shishi.call_matlab()
            # shishi.call_Turbo()
        # shishi.call_CFView()        
        omega,rise = shishi.get_value()
        r = (rise-1)*10 - omega*5
        rizhi = 'MXairfoil: test done, with omega ='+str(omega)+' and rise = '+str(rise)+'\n reward is ' + str(r)
        shishi.jilu(rizhi)
    elif flag == 1 :
        x_rand = np.array([ 0.21333502, -0.3116936 ,  0.52255278,  5.59440807])
        # shishi = call_components(script_folder,matlab_location)
        shishi.set_value(x_rand[0],'chi_in')
        shishi.set_value(x_rand[1],'chi_out')
        shishi.set_value(x_rand[2],'mxthk')
        shishi.set_value(x_rand[3],'umxthk')
        shishi.call_matlab()
        shishi.call_IGG()
        shishi.call_Turbo()
        shishi.call_CFView()        
        omega,rise = shishi.get_value()
    elif flag == 2 :
        shishi.test_existing_case(1)
        # shishi.call_matlab()
        # shishi.call_IGG()
        # shishi.call_Turbo()
        shishi.call_CFView()        
        omega,rise = shishi.get_value()
        rizhi = 'MXairfoil: struggle to find out bug..'+'\n '+shishi.result_folder + '\n  ' + str(omega)+'    ' + str(rise)  
        shishi.jilu(rizhi)
    elif flag == -999 :
        #clear all.
        shishi.clear_all(script_folder,matlab_location)

    # del shishi
    print('MXairfoil: end a call_components test process')

