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

framework_title="""
\033[1;30m# ============================================================================ #\033[0m
# ---------\033[5;31m██╗   ██╗███╗   ██╗██╗████████╗███╗   ██╗███████╗████████╗ \033[0m-------- #
# ---------\033[5;32m██║   ██║████╗  ██║██║╚══██╔══╝████╗  ██║██╔════╝╚══██╔══╝ \033[0m-------- #
# ---------\033[5;33m██║   ██║██╔██╗ ██║██║   ██║   ██╔██╗ ██║█████╗     ██║ \033[0m----------- #
# ---------\033[5;34m██║   ██║██║╚██╗██║██║   ██║   ██║╚██╗██║██╔══╝     ██║ \033[0m----------- #
# ---------\033[5;35m╚██████╔╝██║ ╚████║██║   ██║   ██║ ╚████║███████╗   ██║ \033[0m----------- #
# ----------\033[5;35m╚═════╝ ╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═══╝╚══════╝   ╚═╝ \033[0m----------- #
\033[1;30m# ============================================================================ #\033[0m
"""

# --------------------------- Pytorch API Reference -------------------------- #

import torchvision.models as models
import torchvision.datasets as dataset
import torch.optim as optim
import torch.nn as nn
import torch.nn.functional as F

# ---------------------------- Keras API Reference --------------------------- #

# ---------------------------- MXNet API Reference --------------------------- #

# ------------------------------ Local Reference ----------------------------- #


class ref():
    """ Description	"""
    def __init__(self):
        """ Description
        :type self:
        :param self:
    
        :raises:
    
        :rtype:
        """


        self.mission_supported={
            "InstenceSegmentation":[
                dataset.CocoDetection
            ],
            "Detection":[
                dataset.CocoDetection
            ],
            "Classification":{
                "ImageNet":dataset.ImageNet,
                "MINST":dataset.MNIST,
                "CIFAR100":dataset.CIFAR100,
                "Cityscapes":dataset.Cityscapes,
            },
            "Segmentation":[
                

            ]
        }




      
        # ---------------------------------------------------------------------------- #
        #                              Optimizer Function                              #
        # ---------------------------------------------------------------------------- #

        self.OptimDict={
           "SGD":optim.SGD,                                                                                                                                              
           "ASGD":optim.ASGD,
           "Adam":optim.Adam,
           "Adadelta":optim.Adadelta,
           "Adagrad":optim.Adagrad,
           "AdamW":optim.AdamW, 
           "LBFGS":optim.LBFGS,
           "RMSprop":optim.RMSprop,
           "SparseAdam":optim.SparseAdam,
           "Adamax":optim.Adamax
        }

        # ---------------------------------------------------------------------------- #
        #                                 Loss Function                                #
        # ---------------------------------------------------------------------------- #

        self.Loss_Function_Dict={
            "AdaptiveLogSoftmaxWithLoss":nn.AdaptiveLogSoftmaxWithLoss
            ,"BCELoss":nn.BCELoss 
            ,"BCEWithLogitsLoss":nn.BCEWithLogitsLoss 
            ,"CosineEmbeddingLoss":nn.CosineEmbeddingLoss 
            ,"CrossEntropyLoss":nn.CrossEntropyLoss 
            ,"CTCLoss":nn.CTCLoss 
            ,"cosine_embedding_loss":F.cosine_embedding_loss 
            ,"ctc_loss":F.ctc_loss
            ,"hinge_embedding_loss":F.hinge_embedding_loss 
            ,"l1_loss":F.l1_loss 
            ,"margin_ranking_loss":F.margin_ranking_loss 
            ,"mse_loss":F.mse_loss 
            ,"multi_margin_loss":F.mse_loss 
            ,"multilabel_margin_loss":F.multilabel_margin_loss 
            ,"multilabel_soft_margin_loss":F.multilabel_margin_loss 
            ,"nll_loss":F.nll_loss 
            ,"poisson_nll_loss":F.poisson_nll_loss 
            ,"smooth_l1_loss":F.smooth_l1_loss 
            ,"soft_margin_loss":F.soft_margin_loss 
            ,"triplet_margin_loss":F.triplet_margin_loss 
            ,"HingeEmbeddingLoss":nn.HingeEmbeddingLoss 
            ,"KLDivLoss":nn.KLDivLoss 
            ,"L1Loss":nn.L1Loss 
            ,"MarginRankingLoss":nn.MarginRankingLoss 
            ,"MSELoss":nn.MSELoss 
            ,"MultiLabelMarginLoss":nn.MultiLabelMarginLoss 
            ,"MultiLabelSoftMarginLoss":nn.MultiLabelSoftMarginLoss 
            ,"MultiMarginLoss":nn.MultiMarginLoss 
            ,"NLLLoss":nn.MultiMarginLoss 
            ,"PoissonNLLLoss":nn.PoissonNLLLoss 
            ,"SmoothL1Loss":nn.SmoothL1Loss 
            ,"SoftMarginLoss":nn.SoftMarginLoss 
            ,"TripletMarginLoss":nn.TripletMarginLoss
        }


        # ---------------------------------------------------------------------------- #
        #                            Learning Rate Scheduler                           #
        # ---------------------------------------------------------------------------- #

        self.Lr_Dict={
            "StepLR":optim.lr_scheduler.StepLR,
            "MultiStepLR":optim.lr_scheduler.MultiStepLR,
            "ExponentialLR":optim.lr_scheduler.ExponentialLR,
            "CosineAnnealingLR":optim.lr_scheduler.CosineAnnealingLR,
            "ReduceLROnPlateau":optim.lr_scheduler.ReduceLROnPlateau,
            "CyclicLR":optim.lr_scheduler.CyclicLR,
            "OneCycleLR":optim.lr_scheduler.OneCycleLR,
            "CosineAnnealingWarmRestarts":optim.lr_scheduler.CosineAnnealingWarmRestarts
        }

        # ---------------------------------------------------------------------------- #
        #                                    Network                                   #
        # ---------------------------------------------------------------------------- #

        # --------------------------------- BackBone --------------------------------- #

        self.BackBoneDict={




        }

        # --------------------------- InstanceSegmentation --------------------------- #

        self.InstanceSegmentationDict={



        }

        # --------------------------------- Detection -------------------------------- #

        self.DetectionDict={




        }

        # ------------------------------- Segmentation ------------------------------- #

        self.SegmentationDict={



        }

        # ------------------------------------ MOT ----------------------------------- #
        self.MotDict={



        }

        # --------------------------------- Keypoint --------------------------------- #
        self.KeyPointDict={




        }

        # ------------------------------ Network Library ----------------------------- #

        self.network_zoo={
            "Detection":self.DetectionDict,
            "Segmentation":self.SegmentationDict,
            "InstenceSegmentation":self.InstanceSegmentationDict,
            "Classification":self.BackBoneDict,
            "Keypoint":self.KeyPointDict
        }
