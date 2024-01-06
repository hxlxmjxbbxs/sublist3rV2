from setuptools import setup, find_packages

setup(
    name='Sublist3r_v2',
    version='2.0',
    python_requires='>=2.7, <4',
    install_requires=[
        'dnspython>=2.1.0', 
        'requests>=2.25.1', 
        'argparse>=1.4.0'
    ],
    packages=find_packages() + ['.'],
    include_package_data=True,
    url='https://github.com/hxlxmjxbbxs/SUBLIST3R_V2.0',
    license='GPL-2.0',
    author='Halim Jabbes',
    author_email='halim.jabbes@pm.me',
    description='Enhanced Subdomains enumeration tool for penetration testers',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: GNU General Public License v2',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Security',
    ],
    keywords='subdomain dns penetration testing security enumeration',
    entry_points={
        'console_scripts': [
            'sublist3r_v2 = sublist3r:interactive',
        ],
    },
)
