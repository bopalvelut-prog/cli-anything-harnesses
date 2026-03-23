import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wedding running')
@cli.command()
def start(): click.echo('wedding started')
if __name__ == '__main__': cli()
