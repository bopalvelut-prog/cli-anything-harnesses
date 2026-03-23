import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mutt running')
@cli.command()
def start(): click.echo('mutt started')
if __name__ == '__main__': cli()
