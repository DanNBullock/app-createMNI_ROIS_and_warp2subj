#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 19 13:05:58 2022

@author: dan
"""

import json
import os
import nibabel as nib
import sys

# load inputs from config.json
with open('config.json') as config_json:
 	config = json.load(config_json)
 
#load the mni template
mniTemplate=nib.load('MNI152_T1_1mm_brain.nii.gz')

#create output directory
outDir='output'
if not os.path.exists(outDir):
    os.makedirs(outDir)
if not os.path.exists(os.path.join(outDir,'ROIS')):
    os.makedirs(os.path.join(outDir,'ROIS'))

#create MNI roi directory
MNI_Dir='MNI'
if not os.path.exists(MNI_Dir):
    os.makedirs(MNI_Dir)
if not os.path.exists(os.path.join(MNI_Dir,'ROIS')):
    os.makedirs(os.path.join(MNI_Dir,'ROIS'))

sys.path.append('wma_pyTools')

import wmaPyTools.roiTools
import wmaPyTools.analysisTools
import wmaPyTools.segmentationTools
import wmaPyTools.streamlineTools
import wmaPyTools.visTools

sphereRequests=config['spheres']
#split at the split char
sphereRequests=sphereRequests.split(';')
import re

#remove blank if it's in there
if '' in sphereRequests:
    sphereRequests.remove('')


for sphereIterator,iSphereRequests in enumerate(sphereRequests):
    currFullRequest=iSphereRequests
    #remove commas and spaces
    currFullRequest=re.split(',| \'',currFullRequest)
    currFullRequest=[float(iNum) for iNum in currFullRequest]
    currentSphere=wmaPyTools.roiTools.createSphere(currFullRequest[3], currFullRequest[0:3], mniTemplate, supress=False)
    nib.save(currentSphere,os.path.join(MNI_Dir,'ROIS','sphere_'+str(sphereIterator+1)+'.nii.gz'))

planeRequests=config['planes']
#split at the split char
planeRequests=planeRequests.split(';')

if '' in planeRequests:
    planeRequests.remove('')

for planeIterator,iPlaneRequests in enumerate(planeRequests):
    currFullRequest=iPlaneRequests
    #split at the =
    requestComponents=currFullRequest.split('=')
    #remove whitespace
    requestComponents=[iComponents.strip() for iComponents in requestComponents]
    currentPlane=wmaPyTools.roiTools.makePlanarROI(mniTemplate, float(requestComponents[1]), requestComponents[0])
    nib.save(currentSphere,os.path.join(MNI_Dir,'ROIS','plane_'+str(planeIterator+1)+'.nii.gz'))

print('Plane and sphere ROI creaton complete')

    