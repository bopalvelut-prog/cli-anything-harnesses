import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('piano running')
@cli.command()
def start(): click.echo('piano started')
if __name__ == '__main__': cli()
