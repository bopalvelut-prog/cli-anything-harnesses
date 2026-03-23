from setuptools import setup
setup(
    name='cli-anything-cloudinary',
    version='1.0.0',
    packages=['cli_anything.cloudinary'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cloudinary=cli_anything.cloudinary:cli']},
)
