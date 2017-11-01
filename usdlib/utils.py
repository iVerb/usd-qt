#
# Copyright 2017 Luma Pictures
#
# Licensed under the Apache License, Version 2.0 (the "Apache License")
# with the following modification you may not use this file except in
# compliance with the Apache License and the following modification to it:
# Section 6. Trademarks. is deleted and replaced with:
#
# 6. Trademarks. This License does not grant permission to use the trade
#    names, trademarks, service marks, or product names of the Licensor
#    and its affiliates, except as required to comply with Section 4(c) of
#    the License and to reproduce the content of the NOTICE file.
#
# You may obtain a copy of the Apache License at
#
#     http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the Apache License with the above modification is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the Apache License for the specific
# language governing permissions and limitations under the Apache License.
#
from pxr import Usd, Sdf
from typing import Dict, Iterator, List, NamedTuple, Optional, Tuple, Union


def getAssetName(prim):
    '''
    Return the prim's asset name as stored in assetInfo metadata

    Parameters
    ----------
    prim : Usd.Prim

    Returns
    -------
    Optional[str]
    '''
    assetInfo = prim.GetAssetInfo()
    if assetInfo and 'name' in assetInfo:
        return assetInfo['name']


def getAllSubLayers(layer):
    '''
    Recursively gather a layer's sublayers and sublayer's sublayers.
    
    Parameters
    ----------
    layer : Sdf.Layer
    
    Returns
    -------
    Set[Sdf.Layer]
    '''
    allSubLayers = set()

    def collect(currentLayer):
        allSubLayers.add(currentLayer)
        for subLayer in currentLayer.subLayerPaths:
            collect(Sdf.Layer.FindOrOpen(subLayer))

    collect(layer)
    return allSubLayers
