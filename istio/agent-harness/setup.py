from setuptools import setup
setup(
    name='cli-anything-istio',
    version='1.0.0',
    packages=['cli_anything.istio'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-istio=cli_anything.istio:cli']},
)
