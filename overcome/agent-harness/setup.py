from setuptools import setup
setup(
    name='cli-anything-overcome',
    version='1.0.0',
    packages=['cli_anything.overcome'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-overcome=cli_anything.overcome:cli']},
)
