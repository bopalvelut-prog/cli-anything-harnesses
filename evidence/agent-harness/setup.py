from setuptools import setup
setup(
    name='cli-anything-evidence',
    version='1.0.0',
    packages=['cli_anything.evidence'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-evidence=cli_anything.evidence:cli']},
)
