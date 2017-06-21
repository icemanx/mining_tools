#!/bin/bash

export DISPLAY=:0

/usr/bin/nvidia-settings -a '[gpu:0]/GPUMemoryTransferRateOffset[3]=1100'
/usr/bin/nvidia-settings -a '[gpu:0]/GPUFanControlState=1'
/usr/bin/nvidia-settings -a '[fan:0]/GPUTargetFanSpeed=60'

/usr/bin/nvidia-settings -a '[gpu:1]/GPUMemoryTransferRateOffset[3]=1100'
/usr/bin/nvidia-settings -a '[gpu:1]/GPUFanControlState=1'
/usr/bin/nvidia-settings -a '[fan:1]/GPUTargetFanSpeed=60'

/usr/bin/nvidia-settings -a '[gpu:2]/GPUMemoryTransferRateOffset[3]=1100'
/usr/bin/nvidia-settings -a '[gpu:2]/GPUFanControlState=1'
/usr/bin/nvidia-settings -a '[fan:2]/GPUTargetFanSpeed=60'

/usr/bin/nvidia-settings -a '[gpu:3]/GPUMemoryTransferRateOffset[3]=1100'
/usr/bin/nvidia-settings -a '[gpu:3]/GPUFanControlState=1'
/usr/bin/nvidia-settings -a '[fan:3]/GPUTargetFanSpeed=60'
