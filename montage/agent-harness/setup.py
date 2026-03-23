from setuptools import setup
setup(
    name='cli-anything-montage',
    version='1.0.0',
    packages=['cli_anything.montage'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-montage=cli_anything.montage:cli']},
)
