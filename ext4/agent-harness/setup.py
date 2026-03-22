from setuptools import setup
setup(
    name='cli-anything-ext4',
    version='1.0.0',
    packages=['cli_anything.ext4'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ext4=cli_anything.ext4:cli']},
)
