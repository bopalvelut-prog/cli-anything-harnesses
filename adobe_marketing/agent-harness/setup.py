from setuptools import setup
setup(
    name='cli-anything-adobe_marketing',
    version='1.0.0',
    packages=['cli_anything.adobe_marketing'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-adobe_marketing=cli_anything.adobe_marketing:cli']},
)
