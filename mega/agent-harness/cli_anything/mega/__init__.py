import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def login(): click.echo('MEGA login')
@cli.command()
def ls(): click.echo('MEGA files')
if __name__ == '__main__': cli()
