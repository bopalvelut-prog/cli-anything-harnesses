import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('delombok running')
@cli.command()
def start(): click.echo('delombok started')
if __name__ == '__main__': cli()
