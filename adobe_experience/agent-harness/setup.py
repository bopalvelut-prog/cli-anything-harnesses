from setuptools import setup
setup(
    name='cli-anything-adobe_experience',
    version='1.0.0',
    packages=['cli_anything.adobe_experience'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-adobe_experience=cli_anything.adobe_experience:cli']},
)
