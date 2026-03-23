from setuptools import setup
setup(
    name='cli-anything-lineageos',
    version='1.0.0',
    packages=['cli_anything.lineageos'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lineageos=cli_anything.lineageos:cli']},
)
