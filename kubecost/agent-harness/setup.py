from setuptools import setup
setup(
    name='cli-anything-kubecost',
    version='1.0.0',
    packages=['cli_anything.kubecost'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kubecost=cli_anything.kubecost:cli']},
)
