import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('relationship running')
@cli.command()
def start(): click.echo('relationship started')
if __name__ == '__main__': cli()
