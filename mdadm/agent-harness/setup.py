from setuptools import setup
setup(
    name='cli-anything-mdadm',
    version='1.0.0',
    packages=['cli_anything.mdadm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mdadm=cli_anything.mdadm:cli']},
)
