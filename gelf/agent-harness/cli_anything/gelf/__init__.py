import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('gelf running')
@cli.command()
def start(): click.echo('gelf started')
if __name__ == '__main__': cli()
