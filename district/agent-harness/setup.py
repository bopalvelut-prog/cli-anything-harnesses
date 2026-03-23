from setuptools import setup
setup(
    name='cli-anything-district',
    version='1.0.0',
    packages=['cli_anything.district'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-district=cli_anything.district:cli']},
)
