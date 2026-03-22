from setuptools import setup
setup(
    name='cli-anything-grafana',
    version='1.0.0',
    packages=['cli_anything.grafana'],
    install_requires=['click', 'requests'],
    entry_points={'console_scripts': ['cli-anything-grafana=cli_anything.grafana:cli']},
)
