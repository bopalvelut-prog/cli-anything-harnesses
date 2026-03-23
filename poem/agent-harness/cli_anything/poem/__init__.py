import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('poem running')
@cli.command()
def start(): click.echo('poem started')
if __name__ == '__main__': cli()
