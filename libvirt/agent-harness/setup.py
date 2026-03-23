from setuptools import setup
setup(
    name='cli-anything-libvirt',
    version='1.0.0',
    packages=['cli_anything.libvirt'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-libvirt=cli_anything.libvirt:cli']},
)
