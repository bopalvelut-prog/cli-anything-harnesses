import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def dev(): subprocess.run(['keystone', 'dev'])
@cli.command()
def build(): subprocess.run(['keystone', 'build'])
if __name__ == '__main__': cli()
