from setuptools import setup
setup(
    name='cli-anything-acuity',
    version='1.0.0',
    packages=['cli_anything.acuity'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-acuity=cli_anything.acuity:cli']},
)
