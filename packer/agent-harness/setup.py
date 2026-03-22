from setuptools import setup
setup(
    name='cli-anything-packer',
    version='1.0.0',
    packages=['cli_anything.packer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-packer=cli_anything.packer:cli']},
)
