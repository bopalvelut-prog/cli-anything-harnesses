import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bdd running')
@cli.command()
def start(): click.echo('bdd started')
if __name__ == '__main__': cli()
