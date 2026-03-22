import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): subprocess.run(['ghost', 'start'])
@cli.command()
def stop(): subprocess.run(['ghost', 'stop'])
@cli.command()
def status(): subprocess.run(['ghost', 'status'])
if __name__ == '__main__': cli()
