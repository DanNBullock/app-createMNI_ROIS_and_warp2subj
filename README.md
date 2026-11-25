<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Creates spherical and planar ROIs from MNI coordinates and warps them to a subject's T1 space with ANTs SyN registration, outputting an ROIs directory.**

Builds sphere ROIs (x, y, z, radius) and planar ROIs (axis = coordinate) on the MNI152 1 mm template with wma_pyTools, registers the subject T1 to MNI with antsRegistration (rigid, affine and SyN, using the brain masks), and applies the inverse transform with nearest-label interpolation to bring each ROI into subject space. Use it to define coordinate-based ROIs for tractography segmentation. It needs a T1 and a brain mask of the same subject.

| | |
|---|---|
| 📥 **Inputs** | `neuro/anat/t1w` · `neuro/mask` |
| 📤 **Outputs** | `neuro/rois` |
| 🐳 **Container** | `brainlife/ants:2.2.0` |
| ⚙️ **Resources** | 10 GB memory · 1 h walltime |
| 🔗 **Run it** | [doi.org/10.25663/brainlife.app.629](https://doi.org/10.25663/brainlife.app.629) |

#### 📥 Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `AnatomicalT1` | `neuro/anat/t1w` | yes | Subject T1-weighted image used as the registration target space for the ROIs. |
| `brainMask` | `neuro/mask` (brain) | yes | Brain mask of the subject T1, used to restrict the registration. Must be in the same space as the T1. |

#### 📤 Outputs

| Output | Datatype | Description |
|---|---|---|
| `output` | `neuro/rois` | The requested spherical and planar ROIs, contained within a directory named "rois". |

<details>
<summary><b>⚙️ Parameters</b> (2)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `spheres` | string |  | Any number of sphere requests, with each request delimited by a semicolon (;). Within each request, the first three (3) numbers correspond to the X, Y, and Z coordinates of the sphere centroid. The final (fourth) number corresponds to the sphere radius. Coordinates can be delimited by commas (,) or spaces ( ). |
| `planes` | string |  | Any number of planar requests, with each request delimited by a semicolon (;). Within each request, the first value is a letter (x, y, or z) corresponding to the planar slice the ROI should correspond to. In this way, x will return a sagittal slice, y will return a coronal slice, and z will return a transverse slice. The value following the equals (=) symbol corresponds to the spatial coordinate that the plane should occur at along the specified axis. |

</details>

📚 **References used by this App:**
- Avesani P, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. Sci Data 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

<!-- brainlife-app:end -->

[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.444-blue.svg)](https://doi.org/10.25663/bl.app.444)

## Production Info

### Author
[Dan Bullock](https://github.com/DanNBullock/) ([bullo092@umn.edu](mailto:bullo092@umn.edu))

### PI
[Sarah Heilbronner](https://med.umn.edu/bio/department-of-neuroscience/sarah-heilbronner) (heilb028@umn.edu)

### Funding Information

[![NIH-NIBIB-1T32EB031512-01](https://img.shields.io/badge/NIH_NIBIB-1T32EB031512--01-blue.svg)](https://reporter.nih.gov/project-details/10205698)
[![NIMH-5P50MH119569-02](https://img.shields.io/badge/NIMH-5P50MH119569--02-blue.svg)](https://reporter.nih.gov/project-details/10123009)
[![NIMH-5R01MH118257-04](https://img.shields.io/badge/NIMH-5R01MH118257--04-blue.svg)](https://reporter.nih.gov/project-details/10122991)
[![NIDA-1P30DA048742-01A1](https://img.shields.io/badge/NIDA-1P30DA048742--01A1-blue.svg)](https://reporter.nih.gov/project-details/10025457)

- [Dan Bullock](https://github.com/DanNBullock/)'s work is supported by the following sources:
    - The University of Minnesota’s Neuroimaging Postdoctoral Fellowship Program, College of Science and Engineering's, and the Medical School's NIH funded T32 Neuroimaging Training Grant. NOGA: [1T32EB031512-01](https://reporter.nih.gov/project-details/10205698) 

- [Sarah Heilbronner](https://med.umn.edu/bio/department-of-neuroscience/sarah-heilbronner)'s work is supported by the following sources:
    - The University of Minnesota’s Neurosciences' and Medical School's NIMH grant for the investigation of "Neural Basis of Psychopathology, Addictions and Sleep Disorders Study Section[NPAS]". NOGA: [5P50MH119569-02-04](https://reporter.nih.gov/project-details/10123009) 
    - The University of Minnesota’s Neurosciences' Translational Neurophysiology grant. NOGA: [5R01MH118257-04](https://reporter.nih.gov/project-details/10122991)
    - The University of Minnesota’s Neurosciences' Addiction Connectome grant. NOGA: [1P30DA048742-01A1](https://reporter.nih.gov/project-details/10025457)

### Copyright info
Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)


### Citations
We ask that you the following articles when publishing papers that used data, code or other resources created by the brainlife.io community.

1. Avesani, P., McPherson, B., Hayashi, S. et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. Sci Data 6, 69 (2019). [https://doi.org/10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

2.  [mni citation]


## Running the App 

### On Brainlife.io

You can submit this App online at [https://doi.org/10.25663/bl.app.444](https://doi.org/10.25663/bl.app.444) via the "Execute" tab.

### Running Locally (on your machine)

1. git clone this repo.
2. Inside the cloned directory, create `config.json` with something like the following content with paths to your input files.

```json
{
  "t1": "t1.nii.gz"
}
```

3. Launch the App by executing `main`

```bash
./main
```

### Sample Datasets

If you don't have your own input file, you can download sample datasets from Brainlife.io, or you can use [Brainlife CLI](https://github.com/brain-life/cli).

```
npm install -g brainlife
bl login
mkdir input
bl dataset download 5a0f0fad2c214c9ba8624376#5a050966eec2b300611abff2 && mv 5a0f0fad2c214c9ba8624376#5a050966eec2b300611abff2 .
```

## Output

All output file (a resampled T1w NIFTI-1 file) will be generated inside the current working directory (pwd), inside a specifc directory called:

```
out_dir
```

### Dependencies

This App only requires DIPY.org to run. 
