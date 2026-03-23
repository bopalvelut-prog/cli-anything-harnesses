from setuptools import setup
setup(
    name='cli-anything-k8s',
    version='1.0.0',
    packages=['cli_anything.k8s'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-k8s=cli_anything.k8s:cli']},
)
