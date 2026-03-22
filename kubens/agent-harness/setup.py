from setuptools import setup
setup(
    name='cli-anything-kubens',
    version='1.0.0',
    packages=['cli_anything.kubens'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kubens=cli_anything.kubens:cli']},
)
