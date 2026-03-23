import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('stamina running')
@cli.command()
def start(): click.echo('stamina started')
if __name__ == '__main__': cli()
