from setuptools import setup
setup(
    name='cli-anything-adobe_analytics',
    version='1.0.0',
    packages=['cli_anything.adobe_analytics'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-adobe_analytics=cli_anything.adobe_analytics:cli']},
)
