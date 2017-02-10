# Generate bibliography from LaTeX manuscript using ADS bibcodes

This Python script parses the LaTeX files in the current folder for citations in the ADS BibTeX format, e.g. ` \citep{2017ApJ...835L..32H}`. It then queries ADS and generates a *bibliography.bib*.

## Usage

- Execute the Python code in the same folder as your LaTeX manuscript (compatible with Python 2 and 3)
- The script lists the bibcodes it found and their (un)successfull retrieval from ADS
- Finally, the script creates a new file *bibliography.bib*. If the file already exists, it is overwritten!
- If you use this regularly, you can add it to your LaTeX build process

## Features
- Handles multiple citations, e.g. `\cite{2017ApJ...835L..32H, 2016A&A...591A..67H}`
- Handles mixed citations, e.g. `\citet{2017ApJ...835L..32H, hippke2016a}` (but only ADS bibcodes will end up in the bibliography)


## Alternatives
- Manually collect your references
- Download your online ADS library, if it is well-maintained (mine is not...)
- There is a [Perl script](https://github.com/chanchikwan/adsbib) available that appears to do the same task (but apparently without being able to handle multiple citations)
- The Python package [ADSBibTeX](https://pypi.python.org/pypi/ADSBibTeX/1.0.9) does a similar task, but requires a separate list of references, and your ADS API-Key.
