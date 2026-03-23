from setuptools import setup
setup(
    name='cli-anything-containerd',
    version='1.0.0',
    packages=['cli_anything.containerd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-containerd=cli_anything.containerd:cli']},
)
