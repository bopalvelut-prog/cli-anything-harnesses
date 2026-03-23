from setuptools import setup
setup(
    name='cli-anything-kubespray',
    version='1.0.0',
    packages=['cli_anything.kubespray'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kubespray=cli_anything.kubespray:cli']},
)
