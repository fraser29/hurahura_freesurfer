#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Fraser M Callaghan

Organisation and management of KISPI CLINICAL PIPELINE work

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
    if args.addANON is not None: 
        if len(args.subjNList) != 1:
            raise ValueError(f"For addANON - need 1 and only 1 subject")
        for sn in args.subjNList:
            iSubj = args.MISubjClass(sn, args.dataRoot, args.subjPrefix)
            if iSubj.exists():
                iSubj.addAnonData(anonPath=args.addANON)
    if args.pseudoCT:
        for sn in args.subjNList:
            iSubj = args.MISubjClass(sn, args.dataRoot, args.subjPrefix)
            if iSubj.exists():
                iSubj.runPseudoCT_pipeline()


def getArgGroup():
    groupFreesurfer = miresearch_main.ParentAP.add_argument_group('Freesurfer Actions')
    groupFreesurfer.add_argument('-addANON', dest='addANON', help='Add anonymised data to subject and execute ZTE4D-DL pipeline', type=str, default=None)
    groupFreesurfer.add_argument('-pseudoCT', dest='pseudoCT', help='Run pipeline for pseudoCT', action='store_true')
    return groupFreesurfer
    ##

def main():
    getArgGroup()
    ##
    miresearch_main.main(extra_runActions=[freesurfer_specific_actions], class_obj=FreesurferSubject)


# S T A R T
if __name__ == '__main__':
    main()
