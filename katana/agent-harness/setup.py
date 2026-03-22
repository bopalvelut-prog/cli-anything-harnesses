from setuptools import setup
setup(
    name='cli-anything-katana',
    version='1.0.0',
    packages=['cli_anything.katana'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-katana=cli_anything.katana:cli']},
)
