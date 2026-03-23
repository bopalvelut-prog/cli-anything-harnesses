from setuptools import setup
setup(
    name='cli-anything-openvino',
    version='1.0.0',
    packages=['cli_anything.openvino'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-openvino=cli_anything.openvino:cli']},
)
