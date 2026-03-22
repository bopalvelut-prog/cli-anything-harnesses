from setuptools import setup
setup(
    name='cli-anything-kubeflow',
    version='1.0.0',
    packages=['cli_anything.kubeflow'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kubeflow=cli_anything.kubeflow:cli']},
)
