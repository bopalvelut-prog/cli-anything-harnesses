from setuptools import setup
setup(
    name='cli-anything-kubescape',
    version='1.0.0',
    packages=['cli_anything.kubescape'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kubescape=cli_anything.kubescape:cli']},
)
