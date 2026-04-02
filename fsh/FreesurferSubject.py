#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Fraser M Callaghan

Use of hurahura to setup and manage freesurfer runs

"""

## Local imports
import os
import shutil
import zipfile
from hurahura.mi_config import MIResearch_config
from hurahura import miresearch_main, mi_subject
from spydcmtk import spydcm




# ====================================================================================================
#      HELPER FUNCTIONS
# ====================================================================================================




# ====================================================================================================
class FreesurferSubject(mi_subject.AbstractSubject):
    """
    A class for managing FreeSurfer subjects.
    """
    def __init__(self, subjectNumber, dataRoot, subjectPrefix):
        super().__init__(subjectNumber=subjectNumber, dataRoot=dataRoot, subjectPrefix=subjectPrefix)



    def runPostLoadPipeLine(self):
        pass 
        # Should launch a freesurfer recon-all pipeline - need to control subject name to match this. ? 



class FreesurferSubjectList(mi_subject.SubjectList):
    """
    A class for managing a list of FreeSurfer subjects.
    """
    def __init__(self, subjectList):
        super().__init__(subjectList=subjectList)








### ====================================================================================================================
#      THIS IS FREESURFER-HURAHURA SPECIFIC COMMAND LINE ACTIONS
### ====================================================================================================================
def freesurfer_specific_actions(args):
    pass


def getArgGroup():
    groupFreesurfer = miresearch_main.ParentAP.add_argument_group('Freesurfer Actions')
    return groupFreesurfer
    ##

def main():
    getArgGroup()
    ##
    miresearch_main.main(extra_runActions=[freesurfer_specific_actions], class_obj=FreesurferSubject)


# S T A R T
if __name__ == '__main__':
    main()
