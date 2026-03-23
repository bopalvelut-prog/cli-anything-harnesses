import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('liberal running')
@cli.command()
def start(): click.echo('liberal started')
if __name__ == '__main__': cli()
