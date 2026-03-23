from setuptools import setup
setup(
    name='cli-anything-firecracker',
    version='1.0.0',
    packages=['cli_anything.firecracker'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-firecracker=cli_anything.firecracker:cli']},
)
