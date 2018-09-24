# SynthText for (English + Japanese)
Code for generating synthetic text images as described in ["Synthetic Data for Text Localisation in Natural Images", Ankush Gupta, Andrea Vedaldi, Andrew Zisserman, CVPR 2016](http://www.robots.ox.ac.uk/~vgg/data/scenetext/) with support for japanese characters

## TODO

Add support for chinese

## Output samples


**Synthetic Japanese Text Samples 1**

![Japanese example 1](results/sample1.png "Synthetic Japanese Text Samples 1")


**Synthetic Japanese Text Samples 2**

![Japanese example 2](results/sample2.png "Synthetic Japanese Text Samples 2")


**Synthetic Japanese Text Samples 3**

![Japanese example 3](results/sample3.png "Synthetic Japanese Text Samples 3")


**Synthetic Japanese Text Samples 4**

![Japanese example 4](results/sample4.png "Synthetic Japanese Text Samples 4")


The library is written in Python. The main dependencies are:

```
pygame, opencv (version 3.3), PIL (Image), numpy, matplotlib, h5py, scipy
```

## The main differences

1. Use opencv 3.3 instead of opencv 2.4
2. Use nltk to parse language (eng, jpn)

## How to use this source

### Preparation

Put your text data and font as follow

```
data
├── dset.h5
├── fonts
│   ├── fontlist.txt                        : your font list
│   ├── ubuntu
│   ├── ubuntucondensed
│   ├── ubuntujapanese                      : your japanese font
│   └── ubuntumono
├── models
│   ├── char_freq.cp
│   ├── colors_new.cp
│   └── font_px2pt.cp
└── newsgroup
    └── newsgroup.txt                       : your text source
```

### Install dependencies

```
# For japanese
sudo apt-get install libmecab2 libmecab-dev mecab mecab-ipadic mecab-ipadic-utf8 mecab-utils
```

### Generate font model and char model
```
python invert_font_size.py
python update_freq.py

mv char_freq.cp data/models/
mv font_px2pt.cp data/models/
```

### Then go to next

# SynthText
Code for generating synthetic text images as described in ["Synthetic Data for Text Localisation in Natural Images", Ankush Gupta, Andrea Vedaldi, Andrew Zisserman, CVPR 2016](http://www.robots.ox.ac.uk/~vgg/data/scenetext/).


**Synthetic Scene-Text Image Samples**
![Synthetic Scene-Text Samples](samples.png "Synthetic Samples")

### Generating samples

```
python gen.py --viz --lang ENG/JPN
```

This will download a data file (~56M) to the `data` directory. This data file includes:

  - **dset.h5**: This is a sample h5 file which contains a set of 5 images along with their depth and segmentation information. Note, this is just given as an example; you are encouraged to add more images (along with their depth and segmentation information) to this database for your own use.
  - **data/fonts**: three sample fonts (add more fonts to this folder and then update `fonts/fontlist.txt` with their paths).
  - **data/newsgroup**: Text-source (from the News Group dataset). This can be subsituted with any text file. Look inside `text_utils.py` to see how the text inside this file is used by the renderer.
  - **data/models/colors_new.cp**: Color-model (foreground/background text color model), learnt from the IIIT-5K word dataset.
  - **data/models**: Other cPickle files (**char\_freq.cp**: frequency of each character in the text dataset; **font\_px2pt.cp**: conversion from pt to px for various fonts: If you add a new font, make sure that the corresponding model is present in this file, if not you can add it by adapting `invert_font_size.py`).

This script will generate random scene-text image samples and store them in an h5 file in `results/SynthText.h5`. If the `--viz` option is specified, the generated output will be visualized as the script is being run; omit the `--viz` option to turn-off the visualizations. If you want to visualize the results stored in  `results/SynthText.h5` later, run:

```
python visualize_results.py
```
### Pre-generated Dataset
A dataset with approximately 800000 synthetic scene-text images generated with this code can be found [here](http://www.robots.ox.ac.uk/~vgg/data/scenetext/).

### Adding New Images
Segmentation and depth-maps are required to use new images as background. Sample scripts for obtaining these are available [here](https://github.com/ankush-me/SynthText/tree/master/prep_scripts).

* `predict_depth.m` MATLAB script to regress a depth mask for a given RGB image; uses the network of [Liu etal.](https://bitbucket.org/fayao/dcnf-fcsp/) However, more recent works (e.g., [this](https://github.com/iro-cp/FCRN-DepthPrediction)) might give better results.
* `run_ucm.m` and `floodFill.py` for getting segmentation masks using [gPb-UCM](https://github.com/jponttuset/mcg).

For an explanation of the fields in `dset.h5` (e.g.: `seg`,`area`,`label`), please check this [comment](https://github.com/ankush-me/SynthText/issues/5#issuecomment-274490044).

### Pre-processed Background Images
The 8,000 background images used in the paper, along with their segmentation and depth masks, have been uploaded here:
`http://zeus.robots.ox.ac.uk/textspot/static/db/<filename>`, where, `<filename>` can be:

- `imnames.cp` [180K]: names of filtered files, i.e., those files which do not contain text
- `bg_img.tar.gz` [8.9G]: compressed image files (more than 8000, so only use the filtered ones in imnames.cp)
- `depth.h5` [15G]: depth maps
- `seg.h5` [6.9G]: segmentation maps

Note: I do not own the copyright to these images.

### Generating Samples with Text in non-Latin (English) Scripts
@JarveeLee has modified the pipeline for generating samples with Chinese text [here](https://github.com/JarveeLee/SynthText_Chinese_version).
@gachiemchiep has modified the pipeline for generating samples with Japanese text [here](https://github.com/gachiemchiep/SynthText).


### Further Information
Please refer to the paper for more information, or contact me (email address in the paper).

