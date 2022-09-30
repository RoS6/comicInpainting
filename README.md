# comicInpainting

### Introduction:
   It's always very annoying when we try to read manga in different languages. With google translate, we could only get poor orientated translated words with grey background. In order to translate the manga as well as avoiding the occlusion of the content of the manga pictures behind the words, I used the deepfill v2 to inpaint the background of the selected part, so that the picture under the words are recovered with least effection to the overall manga page. 

   A U-Net model could help automatically recognise the area of the words. With the combination of the U-Net and the deepFill v2, we could automatically remove, and infill the removed area where the words appears. 

### Features:
   * Used deepfill v2 to inpaint the removed part of words. 
   * Use google api to recognise the words in different languages in selected area. Allow user edit the recognised word before translation.
   * Developing a U-Net to recognise the area contains word automatically. 

### Citation:
   * Applied DeepFill v2: https://github.com/JiahuiYu/generative_inpainting.git 
   * Pretrained model of inpainting obtained from DeepFill v2.

### Demo:

https://user-images.githubusercontent.com/38854438/193233656-81c36188-7e53-43b2-9009-8e4c09c37932.mp4

