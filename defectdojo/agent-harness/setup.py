from setuptools import setup
setup(
    name='cli-anything-defectdojo',
    version='1.0.0',
    packages=['cli_anything.defectdojo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-defectdojo=cli_anything.defectdojo:cli']},
)
