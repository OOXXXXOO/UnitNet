# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    config.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: winshare <winshare@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/08/12 19:46:50 by winshare          #+#    #+#              #
#    Updated: 2020/08/14 14:21:26 by winshare         ###   ########.fr        #
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
from reference import *

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



def main():
    CFG=cfg()

if __name__ == '__main__':
    main()
    