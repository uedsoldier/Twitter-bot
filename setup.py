import os
import sys
import subprocess
from setuptools import setup, Command

class BootstrapCommand(Command):
    """
    Custom command to create a venv and install requirements.
    Usage: python setup.py bootstrap [--activate]
    """
    description = 'Create a virtual environment and install requirements.'
    user_options = [
        ('activate', None, 'Activate the venv in a new shell after setup'),
    ]

    def initialize_options(self):
        self.activate = False

    def finalize_options(self):
        pass

    def run(self):
        venv_dir = 'venv'
        python_exe = sys.executable
        # Create venv if it doesn't exist
        if not os.path.isdir(venv_dir):
            print(f'Creating virtual environment in {venv_dir}...')
            subprocess.check_call([python_exe, '-m', 'venv', venv_dir])
        else:
            print(f'Virtual environment already exists in {venv_dir}.')
        # Install requirements
        pip_exe = os.path.join(venv_dir, 'Scripts' if os.name == 'nt' else 'bin', 'pip')
        print('Installing requirements...')
        subprocess.check_call([pip_exe, 'install', '-r', 'requirements.txt'])
        print('Setup complete. To activate the venv:')
        if os.name == 'nt':
            activate_cmd = r'venv\Scripts\activate'
            print(f'  {activate_cmd}')
        else:
            activate_cmd = 'source venv/bin/activate'
            print(f'  {activate_cmd}')
        # Optionally activate in a new shell
        if self.activate:
            print('Launching a new shell with the venv activated...')
            if os.name == 'nt':
                subprocess.call(['cmd.exe', '/K', activate_cmd])
            else:
                subprocess.call([os.environ.get('SHELL', '/bin/bash'), '-i', '-c', activate_cmd])

# You can add more custom commands below, e.g., for testing or cleaning:
# class TestCommand(Command): ...
# class CleanCommand(Command): ...

setup(
    name='Twitter-Bot',
    version='0.1.0',
    description='Twitter bot for posting messages based on basic events.',
    packages=[],  # Add your packages here
    cmdclass={
        'bootstrap': BootstrapCommand,
        # 'test': TestCommand,
        # 'clean': CleanCommand,
    },
)