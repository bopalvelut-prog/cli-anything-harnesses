from setuptools import setup
setup(
    name='cli-anything-nuclei',
    version='1.0.0',
    packages=['cli_anything.nuclei'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nuclei=cli_anything.nuclei:cli']},
)
