#  Density Multiple Random Projection Trees - DMRPT

This repository publishes the datasets used in the Approximate Nearest Neighbors Search with Random Projection Trees and Density-Based Kernel paper.

## Data

The `data/` folder contains the serialized dataset dumps used in the paper. Current files:

- `S_Gausian.dump` — Pickle dump containing the Gaussian synthetic dataset used in experiments.
- `S_Uniform.dump` — Pickle dump containing the Uniform synthetic dataset used in experiments.

### Format

The files are Python pickle dumps. They may contain numpy arrays, lists, dictionaries or custom objects. Use the `load_data.py` script at the repository root to inspect their contents.

### Loading

From the repository root run:

```powershell
python load_data.py data/S_Gausian.dump data/S_Uniform.dump
```

### Notes

- The dataset files are provided as-is for reproducibility of the experiments in the paper.
- Inspect before using: untrusted pickle files can execute code when loaded. Only load them in a trusted environment.

## Citation

If you use this paper or data in your work, please cite:

TODO: Add the citation information for the paper once available.

## Acknowledgments

Funded by the European Union - NextGenerationEU through Greece 2.0—National Recovery and Resilience Plan, under the call ”Flag-ship actions in interdisciplinary scientific fields with a special focus on the productive fabric” (ID16618), project name ”Bridging big omic, genetic and medical data for Precision Medicine implementation in Greece” (project code TAEDR-0539180).

## License

See `LICENSE` at the repository root for licensing information.

---

For any inquiries or issues related to this repository, please contact [Panagiotis Anagnostou](mailto:panagno@uth.gr), or create an issue in the repository.
