import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('white running')
@cli.command()
def start(): click.echo('white started')
if __name__ == '__main__': cli()
