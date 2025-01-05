from setuptools import find_packages, setup

package_name = 'py_fibonacci_action'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='fransk',
    maintainer_email='kouwenhoven.frans@gmail.com',
    description='Server for the custom fibonacci action',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'server = py_fibonacci_action.fibonacci_action_server:main',
        ],
    },
)
