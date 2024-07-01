from setuptools import setup, find_packages

setup(
    name='quadratic_solver',
    version='0.1.0',
    description='A simple Python project to solve quadratic equations',
    author='Hamza',
    author_email='hamzajad44@gmail.com',
    url='https://github.com/00casio/quadratic.git',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={
        'dev': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'solve_quadratic=quadratic_solver:solve',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
