import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def monitor(): subprocess.run(['iotop'])
if __name__ == '__main__': cli()
