import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('parse running')
@cli.command()
def start(): click.echo('parse started')
if __name__ == '__main__': cli()
