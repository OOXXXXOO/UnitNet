# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    config.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Tom Winshare <tanwenxuan@live.com>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/08/12 19:46:50 by winshare          #+#    #+#              #
#    Updated: 2020/10/02 02:08:34 by Tom Winshar      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Copyright 2020 winshare
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from reference import ref,framework_title
import json,os
import torch
class cfg(ref):
    """ Description	"""
    def __init__(self,file=None):
        """ 
        Description
        :type file: string
        :param file: the path of config json file 
        :raises:
        :rtype:
        """
        print(framework_title)
        ref.__init__(self)
        self.infolength=74
        
        print("# ---------------------------------------------------------------------------- #")
        print("#                           config decoder init start                          #")
        print("# ---------------------------------------------------------------------------- #")
        if file!=None:
            self.config=file
        if len(file)>self.infolength-22:
            print("# ===== Decode Config :\33[1;32m\n%s\33[0m"%self.config)
        else:
            print("# ===== Decode Config \33[1;32m%s\33[0m"%self.config) # Init on class model
        self.__configfile=self.config
        self.__json=json.load(open(self.__configfile,'r'))


        # -------------------------------- First Level ------------------------------- #
        self.experiment=self.__json["experiment"]

        self.MissionType=self.__json['MissionType']
        assert self.MissionType in self.mission_supported,"\033[1;31m invalid mission type: "+self.MissionType+" & supported mission is "+str(self.mission_supported)
        
        self.InstanceID=self.__json['instance_id']
        
        
        self.Content=self.__json['content']


        # ------------------------------- Second Level ------------------------------- #
        self.Net=self.Content['Net']
        self.DataSetConfig=self.Content['Dataset']
        self.Config=self.Content['Config']
        self.debug=self.Config["debug"]
        
        print('# ---------------------------------- config ---------------------------------- #')
       
        print("# ------------------------------ NETWORK CONFIG ------------------------------ #")
        self.print_dict(self.Net)
        print("# ------------------------------ NETWORK CONFIG ------------------------------ #")

        print("# ------------------------------ DATASET CONFIG ------------------------------ #")
        self.print_dict(self.DataSetConfig)
        print("# ------------------------------ DATASET CONFIG ------------------------------ #")

        print("# ------------------------------ GENERAL CONFIG ------------------------------ #")
        self.print_dict(self.Config)
        print("# ------------------------------ GENERAL CONFIG ------------------------------ #")

        print('# ---------------------------------- config ---------------------------------- #')
        self.DefaultNetwork=self.Net["DefaultNetwork"]
        self.BatchSize=self.Net['BatchSize']
        if self.Net['BackBone']=='None':
            self.BackBoneName=None
        else:
            self.BackBoneName=self.Net['BackBone']
        self.NetType=self.Net["NetType"]

      # --------------------------------- Optimizer -------------------------------- #

        self.optimizer=self.OptimDict[self.Net['Optimizer']]
        self.learning_rate=self.Net['learning_rate']
        self.momentum=self.Net['momentum']
        self.weight_decay=self.Net['weight_decay']

        # ------------------------------- lr_scheduler ------------------------------- #

        self.lr_scheduler=self.Net['lr_scheduler']
        self.lr_steps=self.Net['lr_steps']
        self.lr_gamma=self.Net['lr_gamma']
        self.lr_scheduler=self.Lr_Dict[self.lr_scheduler]
        self.class_num=self.Net['class_num']
        
        # ------------------------------- Loss Function ------------------------------ #

        self.Loss_Function=self.Loss_Function_Dict[self.Net['Loss_Function']]()
        


        # ---------------------------------------------------------------------------- #
        #                                    Dataset                                   #
        # ---------------------------------------------------------------------------- #

        
        self.DataSetType=self.DataSetConfig['Type']
        self.DataSet_Root=self.DataSetConfig['root']
    

        self.Dataset_Train_file=os.path.join(self.DataSet_Root,self.DataSetConfig['train_index_file'])
        self.Dataset_Val_file=os.path.join(self.DataSet_Root,self.DataSetConfig['val_index_file'])
        self.DefaultDataset=self.DataSetConfig['DefaultDataset']
        # self.NPY=self.DataSetConfig["NPY"]
        # if os.path.exists(self.NPY):
        #     self.NPY_Data=np.load(self.NPY,allow_pickle=True)




        # ---------------------------------------------------------------------------- #
        #                                    Config                                    #
        # ---------------------------------------------------------------------------- #
                
        self.DistributedDataParallel=self.Config['DistributedDataParallel']
        self.resume=self.Config['Resume']
        self.checkpoint=self.Config['checkpoint_path']
        self.multiScale_training=self.Config['multiscale_training']
        self.logdir=self.Config['logdir']
        self.devices=self.Config['devices']
        self.pre_estimation=self.Config['pre_estimation']
        self.workspace=self.Config["workspace"]
        try:
            if not os.path.exists(self.workspace):
                os.makedirs(self.workspace)
            exp=os.path.join(self.workspace,self.experiment)
            if not os.path.exists(exp):
                os.makedirs(exp)
            log=os.path.join(exp,self.logdir)
            if not os.path.exists(log):
                os.makedirs(log)
            checkpoint=os.path.join(exp,self.logdir)
            if not os.path.exists(checkpoint):
                os.makedirs(checkpoint)
        except Exception as e:
            print(e)


        
        if self.devices=='GPU':
            self.usegpu=True
            self.gpu_id=self.Config['gpu_id']
            # os.environ['CUDA_VISIBLE_DEVICES']=str(self.gpu_id)

            self.device = torch.device("cuda:"+str(self.gpu_id) if torch.cuda.is_available() else "cpu")
            print('# ===== \033[35mAvaliable Device : \033[36m%s\033[0m'%self.device)
        
        if self.devices=='CPU':
            self.device=torch.device("cpu")


        self.download_pretrain_model=self.Config['down_pretrain_model']
        self.visualization=self.Config['visualization']
        self.worker_num=self.Config['worker_num']
        self.epochs=self.Config['epochs']
        self.aspect_ratio_factor=self.Config['group_factor']





        print("# ---------------------------------------------------------------------------- #")
        print("#                           config decoder init done                           #")
        print("# ---------------------------------------------------------------------------- #")



    def print_dict(self,d,n=0):
        
        for k,v in d.items():
            # print ('\t'*n)
            if type(v)==type({}):
                print("%s : {" % k)
                self.print_dict(v,n+1)
            else:
                strl=len(str(k))+len(str(v))
                space=self.infolength-strl
                print("# %s : \33[1;32m%s\33[0m" % (k,v)+" "*space+"#")
        if n!=0:
            print('\t'*(n-1)+ '}')


def main():
    CFG=cfg(file="/Users/winshare/workspace/UnitNet/Src/Config/Classification/classification_std.json")

if __name__ == '__main__':
    main()
    