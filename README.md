<h1 align="center">Create MNI coordinate-based ROIS and warp to subject space</h1>

<p align="center">
  Creates spherical and planar ROIs from MNI coordinates and warps them to a subject's T1 space with ANTs SyN registration, outputting an ROIs directory.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.629"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.629-blue.svg" alt="Run on brainlife.io"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-see_LICENSE-lightgrey.svg" alt="License"></a>
</p>

## At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Creates spherical and planar ROIs from MNI coordinates and warps them to a subject's T1 space with ANTs SyN registration, outputting an ROIs directory.**

Builds sphere ROIs (x, y, z, radius) and planar ROIs (axis = coordinate) on the MNI152 1 mm template with wma_pyTools, registers the subject T1 to MNI with antsRegistration (rigid, affine and SyN, using the brain masks), and applies the inverse transform with nearest-label interpolation to bring each ROI into subject space. Use it to define coordinate-based ROIs for tractography segmentation. It needs a T1 and a brain mask of the same subject.

| | |
|---|---|
| **Inputs** | `neuro/anat/t1w` · `neuro/mask` |
| **Outputs** | `neuro/rois` |
| **Container** | `brainlife/ants:2.2.0` |
| **Resources** | 10 GB memory · 1 h walltime |
| **Run it** | [doi.org/10.25663/brainlife.app.629](https://doi.org/10.25663/brainlife.app.629) |

#### Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `AnatomicalT1` | `neuro/anat/t1w` | yes | Subject T1-weighted image used as the registration target space for the ROIs. |
| `brainMask` | `neuro/mask` (brain) | yes | Brain mask of the subject T1, used to restrict the registration. Must be in the same space as the T1. |

#### Outputs

| Output | Datatype | Description |
|---|---|---|
| `output` | `neuro/rois` | The requested spherical and planar ROIs, contained within a directory named "rois". |

<details>
<summary><b>Parameters</b> (2)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `spheres` | string |  | Any number of sphere requests, with each request delimited by a semicolon (;). Within each request, the first three (3) numbers correspond to the X, Y, and Z coordinates of the sphere centroid. The final (fourth) number corresponds to the sphere radius. Coordinates can be delimited by commas (,) or spaces ( ). |
| `planes` | string |  | Any number of planar requests, with each request delimited by a semicolon (;). Within each request, the first value is a letter (x, y, or z) corresponding to the planar slice the ROI should correspond to. In this way, x will return a sagittal slice, y will return a coronal slice, and z will return a transverse slice. The value following the equals (=) symbol corresponds to the spatial coordinate that the plane should occur at along the specified axis. |

</details>

<!-- brainlife-app:end -->

## Running the App

### On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.629](https://doi.org/10.25663/brainlife.app.629), choose `neuro/anat/t1w`, `neuro/mask` from your project, set the parameters and press **Execute**. The results are saved to your project as `neuro/rois`.

### Locally

You need [Singularity/Apptainer](https://apptainer.org/) (the App runs in `brainlife/ants:2.2.0`), [`jq`](https://jqlang.github.io/jq/).

1. Clone this repository.
2. Create `config.json` with the paths to your inputs and the parameters:

   ```json
   {
       "t1": "/path/to/AnatomicalT1/t1",
       "mask": "/path/to/brainMask/mask",
       "spheres": "",
       "planes": ""
   }
   ```

3. Run `./main`.

## PI

[Sarah Heilbronner](https://med.umn.edu/bio/department-of-neuroscience/sarah-heilbronner) (heilb028@umn.edu)

## Copyright info

Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)

## Sample Datasets

If you don't have your own input file, you can download sample datasets from Brainlife.io, or you can use [Brainlife CLI](https://github.com/brainlife/cli).

```
npm install -g brainlife
bl login
mkdir input
bl dataset download 5a0f0fad2c214c9ba8624376#5a050966eec2b300611abff2 && mv 5a0f0fad2c214c9ba8624376#5a050966eec2b300611abff2 .
```

## Citing

If you use this App, please cite it, the software it builds on and brainlife.io:

- Create MNI coordinate-based ROIS and warp to subject space. brainlife.io App. [doi:10.25663/brainlife.app.629](https://doi.org/10.25663/brainlife.app.629)
- [mni citation]
- Garyfallidis et al. Dipy, a library for the analysis of diffusion MRI data. *Frontiers in Neuroinformatics* 8 (2014). [doi:10.3389/fninf.2014.00008](https://doi.org/10.3389/fninf.2014.00008)
- Avants et al. A reproducible evaluation of ANTs similarity metric performance in brain image registration. *NeuroImage* 54:2033-2044 (2011). [doi:10.1016/j.neuroimage.2010.09.025](https://doi.org/10.1016/j.neuroimage.2010.09.025)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Authors

[Dan Bullock](https://github.com/DanNBullock/)

## Funding

[![Wellcome-226486/Z/22/Z](https://img.shields.io/badge/Wellcome-226486%2FZ%2F22%2FZ-purple.svg)](https://wellcome.org/)
[![NIH-NINDS-U24NS140384](https://img.shields.io/badge/NIH_NINDS-U24NS140384-green.svg)](https://reporter.nih.gov/project-details/11261037)
[![NIH-NINDS-UM1NS132207](https://img.shields.io/badge/NIH_NINDS-UM1NS132207-green.svg)](https://reporter.nih.gov/project-details/11411328)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://reporter.nih.gov/project-details/10262925)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://reporter.nih.gov/project-details/10428625)
[![NIH-NIMH-R01MH126699](https://img.shields.io/badge/NIH_NIMH-R01MH126699-green.svg)](https://reporter.nih.gov/project-details/10460628)
[![NIH-NIDCD-R01DC020088](https://img.shields.io/badge/NIH_NIDCD-R01DC020088-green.svg)](https://reporter.nih.gov/project-details/11140284)
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-2203524](https://img.shields.io/badge/NSF_BCS-2203524-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2203524)
[![NSF-IIS-1636893](https://img.shields.io/badge/NSF_IIS-1636893-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-OAC-2148729](https://img.shields.io/badge/NSF_OAC-2148729-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148729)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NSF-IIS-2148700](https://img.shields.io/badge/NSF_IIS-2148700-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148700)
[![NSF-OAC-1916518](https://img.shields.io/badge/NSF_OAC-1916518-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1916518)

<sub>brainlife.io, which runs this App, is publicly funded by Wellcome, the U.S. National Institutes of Health and the U.S. National Science Foundation; acknowledging that support helps keep it running.</sub>

## License

See [LICENSE](LICENSE).
