from setuptools import setup
setup(
    name='cli-anything-study_v2',
    version='1.0.0',
    packages=['cli_anything.study_v2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-study_v2=cli_anything.study_v2:cli']},
)
