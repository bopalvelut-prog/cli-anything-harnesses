from setuptools import setup
setup(
    name='cli-anything-predict',
    version='1.0.0',
    packages=['cli_anything.predict'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-predict=cli_anything.predict:cli']},
)
