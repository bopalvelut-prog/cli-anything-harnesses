from setuptools import setup
setup(
    name='cli-anything-psutil',
    version='1.0.0',
    packages=['cli_anything.psutil'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-psutil=cli_anything.psutil:cli']},
)
