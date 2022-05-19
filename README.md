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
