# Cell-virulence-Detection-using-Image-Processing
Designed an automated tool to find the thickness of multiple cell capsules from images using morphological operations to generate plots of cell size vs capsular thickness, simplifying detection of virulence in yeast cells for mycologists

The thickness of the capsule is correlated with the virulence of the yeast cell. The approach of image analysis and classification is relatively new in the field of yeast genomics. By enhancing the image before segmentation, the proposed algorithm should overcome the traditional poor performance of threshold based segmentation methods under noisy environments. To achieve this goal, the appropriate filters will have to be applied, then segmentation is performed and then each segmented image is processed in such a way that only features from single cells are extracted.

Traditional methods were based on manual measurement of capsule thickness in the image. By pre-processing the images, applying filters and extracting the boundaries by finding contours, the algorithm gives us a graph from which the capsule thickness can be easily found.
