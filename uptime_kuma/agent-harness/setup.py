from setuptools import setup
setup(
    name='cli-anything-uptime_kuma',
    version='1.0.0',
    packages=['cli_anything.uptime_kuma'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-uptime_kuma=cli_anything.uptime_kuma:cli']},
)
