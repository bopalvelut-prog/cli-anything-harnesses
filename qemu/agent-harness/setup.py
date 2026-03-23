from setuptools import setup
setup(
    name='cli-anything-qemu',
    version='1.0.0',
    packages=['cli_anything.qemu'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-qemu=cli_anything.qemu:cli']},
)
