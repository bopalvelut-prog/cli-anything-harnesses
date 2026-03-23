import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('peer running')
@cli.command()
def start(): click.echo('peer started')
if __name__ == '__main__': cli()
