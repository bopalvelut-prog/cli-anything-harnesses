from setuptools import setup
setup(
    name='cli-anything-teamcity',
    version='1.0.0',
    packages=['cli_anything.teamcity'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-teamcity=cli_anything.teamcity:cli']},
)
