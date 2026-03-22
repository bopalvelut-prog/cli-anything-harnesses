import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def login(): subprocess.run(['wandb', 'login'])
@cli.command()
def sweep(): subprocess.run(['wandb', 'agent'])
if __name__ == '__main__': cli()
