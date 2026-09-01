# Teaching a Neural Network to Recognize Natural Scenes: From a Custom CNN to Explainable Transfer Learning

When a person sees a photograph of a forest or a city street, recognition feels immediate. A computer receives only a grid of pixel values. It must learn which visual patterns separate trees from buildings, glaciers from mountains, and coastlines from other landscapes.

In this project, I used chatbot-assisted coding to build an end-to-end deep-learning workflow for natural-scene classification. I compared a custom convolutional neural network with an ImageNet-pretrained MobileNetV2 model, fine-tuned the stronger approach, analyzed its errors, and used Grad-CAM to inspect the image regions influencing difficult predictions.

The final model achieved **90.27% test accuracy** and **90.48% macro-F1** across six classes. More importantly, its failures revealed where visual categories overlap and why aggregate accuracy is only the beginning of model evaluation.

## The dataset and the question

I used the Intel Image Classification dataset from Kaggle. It contains six categories: buildings, forest, glacier, mountain, sea, and street.

The working data was divided into 11,228 training images, 2,806 validation images, and 3,000 untouched test images. The classes were reasonably balanced, so accuracy was useful, but I also calculated precision, recall, and macro-F1 to give each category equal importance.

**Insert `class-distribution.png` here.**

**Insert `sample-images.png` here.**

The objective was to answer three questions:

1. How well can a CNN trained from scratch recognize these scenes?
2. How much does transfer learning improve generalization?
3. What can the model's errors and Grad-CAM maps teach us about its behavior?

## Following CRISP-DM for computer vision

I organized the project using CRISP-DM: Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, and Deployment.

The business framing was intentionally broader than maximizing a leaderboard score. Scene recognition can support photo organization, visual search, and content indexing, but a deployed system also needs reliable confidence estimates, interpretable failure analysis, and monitoring for unfamiliar inputs.

During data understanding, I audited the folder structure, counted images by class and split, verified label names, and checked that the test set remained separate from training decisions.

For preparation, every image was resized to 150 × 150 pixels. Training-only augmentation introduced horizontal flips, small rotations, zoom, and contrast variation. These transformations encouraged the model to learn scene structure instead of memorizing exact training images.

**Insert `augmentation-examples.png` here.**

The test dataset was loaded without shuffling. This small implementation detail preserved the alignment between file paths, true labels, and predictions during error analysis.

## Baseline: a custom convolutional neural network

The baseline was a CNN built from scratch with four convolutional blocks. Each block combined convolution, batch normalization, and max pooling. Global average pooling and dropout reduced overfitting before the six-class softmax output.

The custom CNN achieved **80.10% test accuracy**. Its learning curves showed genuine learning, but validation performance fluctuated and remained substantially below the training curve. That gap suggested limited generalization and motivated transfer learning.

**Insert `custom-cnn-learning-curves.png` here.**

## Transfer learning with MobileNetV2

Instead of asking a new model to learn every visual feature from scratch, transfer learning begins with representations learned from a much larger dataset. I loaded MobileNetV2 with ImageNet weights, removed its original classification head, and attached a new global-average-pooling, dropout, and six-class softmax head.

The first stage froze the pretrained feature extractor and trained only 7,686 new parameters. I then unfroze the final 30 MobileNetV2 layers, kept batch-normalization layers frozen for stability, and fine-tuned approximately 1.5 million parameters using a learning rate of 0.00001.

Training ran on two NVIDIA T4 GPUs using TensorFlow's `MirroredStrategy`. Early stopping restored the most useful weights, while learning-rate reduction allowed smaller adjustments when validation loss stopped improving.

The saved, fully rerun notebook produced the following test results:

| Model | Test accuracy | Test loss |
|---|---:|---:|
| Custom CNN | 80.10% | 0.5698 |
| Fine-tuned MobileNetV2 | **90.27%** | **0.2487** |

**Insert `final-model-comparison.png` here.**

Transfer learning improved test accuracy by **10.17 percentage points**. This is not simply the result of a larger model. It reflects the value of reusable edge, texture, shape, and object representations learned from diverse images.

## Looking beyond accuracy

The final model's macro precision was 90.43%, macro recall was 90.63%, and macro-F1 was 90.48%. Forest was the easiest class, reaching 98.95% F1. Glacier and mountain were the hardest, with F1 scores of 83.15% and 84.24%.

The confusion matrix explained why. The largest directional errors were:

- 69 mountain images classified as glacier
- 63 glacier images classified as mountain
- 49 street images classified as buildings

**Insert `confusion-matrices.png` here.**

These mistakes are visually plausible. Mountain and glacier photographs often share snow, exposed rock, distant peaks, and similar horizons. Streets and buildings frequently occur in the same urban image, so the correct label may depend on which part of the scene dominates.

## The value of confident mistakes

I examined the model's most confident incorrect predictions. Several exceeded 99% confidence.

**Insert `misclassified-images.png` here.**

This is an important warning: softmax confidence is not the same as correctness. A classifier can be highly certain when an image contains features strongly associated with the wrong category. A deployed system should therefore monitor calibration and consider deferring low-confidence or unusual cases to a human reviewer.

The error gallery also raises a dataset question. Some images legitimately contain multiple concepts. A photograph dominated by buildings may be labeled street, while a snowy mountain scene could reasonably resemble a glacier. Error analysis should examine label ambiguity rather than assuming every disagreement is purely a model failure.

## Explaining predictions with Grad-CAM

Grad-CAM produces a heatmap showing spatial regions that most influenced a convolutional model's selected prediction. I applied it to six highly confident errors.

**Insert `gradcam-explanations.png` here.**

The model often emphasized recognizable content: towers and facades for buildings, horizons and water for sea, and snowy rock formations for glacier. These maps made the mistakes easier to understand. For example, when a mountain was predicted as glacier, the strongest activation often covered its snow-covered region.

Grad-CAM must be interpreted cautiously. It shows sensitivity within the model, not human-like reasoning, causal proof, or a guarantee that the highlighted area is semantically correct.

## What an actual deployment would require

A lightweight application could accept an uploaded photograph, resize and preprocess it, and return the six class probabilities. The trained `.keras` model is already preserved as an artifact.

Production readiness would require more than serving predictions. I would monitor:

- Input drift and changing image characteristics
- Confidence calibration
- Class-specific precision and recall
- Frequency of low-confidence predictions
- Performance on images outside the six known classes
- Latency, memory use, and model-version provenance

The system should expose uncertainty and avoid forcing every unfamiliar image into a known category. An out-of-distribution or rejection mechanism would be a valuable next improvement.

## How AI assistance changed the workflow

ChatGPT/Codex assisted with planning the CRISP-DM stages, generating TensorFlow code, diagnosing disabled GPU and internet settings, building the custom CNN and MobileNetV2 workflow, interpreting metrics, and structuring the final report.

AI assistance accelerated iteration, but verification remained essential. Every code block was executed in Kaggle, errors were corrected using observed traces, and final claims were reconciled against exported CSV and JSON results. The complete notebook, prompts, model files, figures, and metrics are preserved in the GitHub repository.

One subtle lesson came from reproducibility. The interactive training session reached 90.83% test accuracy, while the clean saved rerun reached 90.27%. Small differences can remain even with a fixed random seed when training across multiple GPUs. I therefore used the clean rerun's 90.27% result everywhere in the final report.

## Conclusion

The project demonstrated that transfer learning can make a decisive difference on a moderate-sized image dataset. MobileNetV2 improved test accuracy by more than ten percentage points over the custom CNN while supporting detailed class-level and spatial error analysis.

The most valuable outcome was not a single accuracy number. It was a reproducible workflow connecting data preparation, model design, evaluation, explainability, and deployment considerations. A useful deep-learning project should show not only what the model gets right, but also where it fails, why those failures are plausible, and how its behavior would be monitored beyond the notebook.
