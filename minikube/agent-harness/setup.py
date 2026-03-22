from setuptools import setup
setup(
    name='cli-anything-minikube',
    version='1.0.0',
    packages=['cli_anything.minikube'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-minikube=cli_anything.minikube:cli']},
)
