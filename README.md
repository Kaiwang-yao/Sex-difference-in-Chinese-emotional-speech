
# Acoustic Feature Extraction and Analysis for Mandarin Emotional Speech

This repository contains the Python scripts used in the study:

Sex Differences in the Production of Emotional Speech Among Chinese Speakers, submitted to Journal of Acoustical Society of America.

## Overview

This project analyzes sex differences in emotional speech production in Mandarin Chinese using:

- The Emotional Speech Database (ESD): [https://github.com/HLTSingapore/Emotional-Speech-Data] (https://github.com/HLTSingapore/Emotional-Speech-Data) 
- The extended GeMAPS feature set  
- Feature extraction via openSMILE  
- Statistical analysis using R packages (e.g., `lmerTest`, `emmeans`, `effectsize`)

## Repository Contents

- `extract_features.py`: Python script for extracting acoustic features using openSMILE, adapted from:  
  > Anonymous. (2022). “在Python上用openSMILE提取IS09和eGeMAPS特征集” [Python code]. CSDN Blog. https://blog.csdn.net/weixin_42103947/article/details/126989553 (Accessed 2024-07-01)
- `config/gemaps_eGeMAPSv02.conf`: Configuration file for GeMAPS  
- `README.md`: This file

## Requirements

- Python 3.12.7 with:  
  - openSMILE 3.0.2  
  - numpy
- R 4.4.2 with the following libraries:  
  - `lmerTest`  
  - `emmeans`  
  - `effectsize`  
  - `ggplot2`

## How to Use

1. Download the ESD dataset from: https://github.com/HLTSingapore/Emotional-Speech-Data

2. Download openSMILE from: https://github.com/audeering/opensmile


3. Extract GeMAPS features from the samples using openSMILE with the code provided in the following link: https://blog.csdn.net/weixin_42103947/article/details/126989553, which is adapted in our extract_feature.py.
Modify the input and output paths as needed.

4. Compile the extracted data into one csv. file.

5. Open RStudio to perform PCA and linear mixed model analysis.

## Citation

If you use this code or the methodology in your own research, please cite:
-Ben-Shachar, M. S., Lüdecke, D., & Makowski, D. (2020). effectsize: Estimation of effect size indices and standardized parameters. Journal of Open Source Software, 5(56), 2815.
-Kuznetsova, A., Brockhoff, P. B., & Christensen, R. H. (2017). lmerTest package: tests in linear mixed effects models. Journal of statistical software, 82, 1-26.
-Lenth, R. V. (2023). emmeans: Estimated marginal means, aka least-squares means (Version 1.8.8) [R package]. https://CRAN.R-project.org/package=emmeans
-Wickham, H. (2016). ggplot2: Elegant graphics for data analysis. Springer.
-Anonymous, “在Python上用openSMILE提取IS09和eGeMAPS特征集.” CSDN Blog, 22 September 2022, https://blog.csdn.net/weixin_42103947/article/details/126989553 . Accessed 1 July 2024.

## Contact

For questions or collaboration inquiries, please contact:  
Xiaojing Yao, Kaijun Wang  
Jinan University
No. 601, Huangpu Avenue West,
Tianhe District,
Guangzhou, Guangdong Province,
510632,
P. R. China



