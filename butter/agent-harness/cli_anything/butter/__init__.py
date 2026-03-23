import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('butter running')
@cli.command()
def start(): click.echo('butter started')
if __name__ == '__main__': cli()
