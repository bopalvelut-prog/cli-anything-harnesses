from setuptools import setup
setup(
    name='cli-anything-intel_tbb',
    version='1.0.0',
    packages=['cli_anything.intel_tbb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-intel_tbb=cli_anything.intel_tbb:cli']},
)
