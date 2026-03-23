import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('translate running')
@cli.command()
def start(): click.echo('translate started')
if __name__ == '__main__': cli()
