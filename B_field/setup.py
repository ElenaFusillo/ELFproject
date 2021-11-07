from setuptools import find_packages, setup

setup(
    name='B_field',
    version='0.1.0.dev1',
    description='Evaluation of effective magnetic induction B in a given point (xp, yp),due to single or double triad of cables.',
    author='E. Fusillo',
    author_email= 'elena.fusillo@studio.unibo.it',
    license='Creative Commons Zero v1.0 Universal',
    classifiers=['Development Status :: 3 - Alpha',
                'Intended Audience :: Technicians',
                'Topic :: Electromagnetic fields evaluation :: Extremely Low Frequencies (ELF)',
                'License :: Creative Commons Zero v1.0 Universal',
                'Programming Language :: Python :: 3.9.7'],
    keywords='ELF magnetic induction B',
    packages=find_packages(include=['B_field', 'B_field.*']),
    #install_requires=["required_package", ],
    entry_points={
        'console_scripts': [
            'B_field=B_field.__main__:main',
        ],
    })
