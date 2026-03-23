from setuptools import setup
setup(
    name='cli-anything-airsonic',
    version='1.0.0',
    packages=['cli_anything.airsonic'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-airsonic=cli_anything.airsonic:cli']},
)
