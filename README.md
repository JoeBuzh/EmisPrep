# EmisPrep
A Toolkit to Adjust Pollute Emission Data for Multi Air Quality Model.

## 1.config
+ No use.

## 2.input (Four Air Quality Pattern)
+ input data interface
+ cmaq -> daily update
+ naqp -> softlink
+ osam -> softlink
+ wrfc -> timestamp

## 3.output
+ output data interface
+ ${output_dir}/${model_name}

## 4.pre_analysis
+ xarray test in jupyter

## 5.src
+ links
    - link class
        - baselink
        - cmaqlink
        - naqplink
        - osamlink
        - wrfclink
        - cmaxlink
    - utils 
    - cfg
        - configs
    - main
        + main link process

## Tools
+ python3.7
    - xarray
    - os
    - datetime
