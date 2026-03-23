import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('eight running')
@cli.command()
def start(): click.echo('eight started')
if __name__ == '__main__': cli()
