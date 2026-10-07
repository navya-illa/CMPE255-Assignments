# CMPE 255 Short Story: Soil Moisture and Machine Learning

This project presents the 2026 arXiv survey **[A Survey on Data-Driven Models for Soil Moisture Regression and Classification](https://arxiv.org/pdf/2606.18316)** by Ilektra Tsimpidi, George Georgoulas, Vidya Sumathy, and George Nikolakopoulos.

The project translates the survey into an original Medium article, a technical slide presentation, and a presentation script. It focuses on how machine-learning models combine ground sensors, satellites, weather data, soil properties, terrain, and historical observations to estimate or classify soil moisture.

## Project overview

Soil moisture is important for drought monitoring, flood forecasting, irrigation, agriculture, and water-resource management. It varies across location, time, soil depth, vegetation, and weather conditions. Because direct sensors provide limited spatial coverage, data-driven models combine ground observations with remote-sensing and environmental data.

The survey organizes the literature into five model families:

1. Statistical time-series models, including ARIMA and SARIMA
2. Geostatistical methods, including Kriging, IDW, GWR, and Co-Kriging
3. Classical machine-learning models, including Random Forest, XGBR, ANN, and SVM
4. Deep-learning models, including LSTM, CNN, GCCL, transformers, and physics-guided LSTM
5. Probabilistic and Bayesian models, including Bayesian inverse models, hierarchical Bayesian models, GPR-RU, and SGPR

## Technical focus

The project covers two prediction targets:

- **Regression:** continuous soil-moisture estimation, temporal forecasting, multi-depth prediction, gap filling, and spatial downscaling
- **Classification:** moisture states such as dry, moderate, or wet for drought monitoring and irrigation support

The presentation also explains why validation must match deployment. Temporal holdouts, spatial blocking, and leave-one-station-out validation are more informative than random cross-validation when observations are correlated across time, space, or sensor stations.

## Reported results highlighted from the survey

The project uses the survey’s reported results with their original task and data context:

- Ordinary Co-Kriging reported **R² values from 0.944 to 0.992** for quarterly and monthly analyses.
- SMRFR combined ISMN, ERA5-Land, MODIS, soil, and topographic variables to estimate five depth layers daily at 9 km resolution from 2000–2023.
- XGBR-GA combined Sentinel-1, Sentinel-2, and an ALOS digital surface model and reported **R² = 0.891** and **RMSE = 0.879%**.
- An SVM drought-classification study reported **AUC = 0.8166**.
- An LSTM daily forecasting study reported **R² = 0.87** and **RMSE = 0.046**.
- GCCL using SMAP Level 4 grids reported **RMSE values from 0.018 to 0.038 m³/m³** for one- to seven-day forecasts and up to **14.3% lower error** than ConvLSTM.
- A 1D CNN for 6–24 inch moisture classification reported **testing accuracy = 0.67** and **AUC = 0.85**.
- PHYs-LSTM using ERA5-Land increased R² by **20.7%** and reduced RMSE by **8.2%** compared with a conventional LSTM baseline.

These results come from different cited studies and are not a single shared leaderboard. Their inputs, targets, units, regions, depths, forecast horizons, and validation designs must be considered before comparing them.

## Published links

- **Medium article:** [How Machine Learning Reads the Moisture Beneath Our Feet](https://medium.com/@9navya9/how-machine-learning-reads-the-moisture-beneath-our-feet-f3fa2096adaf)
- **SlideShare deck:** To be added after publication
- **Presentation video:** To be added after recording and upload
- **GitHub assignment directory:** To be added after the final links are uploaded

## Repository contents

```text
.
├── README.md
├── SUBMISSION-CHECKLIST.md
├── A-Survey-on-Data-Driven-Models-for-Soil-Moisture-Regression-and-Classification.pdf
├── article/
│   ├── medium-article.md
│   └── assets/
│       ├── figure-01-spatial-variation.png
│       ├── figure-02-data-pipeline.png
│       └── figure-03-model-taxonomy-source.png
├── slides/
│   ├── slide-deck-content.md
│   └── presentation-script.md
└── output/
    └── Soil-Moisture-2026-Brown-Technical-Deck-v6.pptx
```

## How to use this project

1. Read the source survey and the Medium article for the narrative explanation.
2. Open the PowerPoint deck for the technical presentation.
3. Use the presentation script while recording the presentation.
4. Publish the deck on SlideShare and add the URL above.
5. Record the 10–15-minute presentation, upload the video to the GitHub assignment directory, and add its URL above.
6. Submit the GitHub, Medium, and SlideShare links required by the assignment.

## Citation

Tsimpidi, I., Georgoulas, G., Sumathy, V., and Nikolakopoulos, G. “A Survey on Data-Driven Models for Soil Moisture Regression and Classification.” arXiv:2606.18316, 2026. [https://arxiv.org/pdf/2606.18316](https://arxiv.org/pdf/2606.18316)
