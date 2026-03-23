import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('protein running')
@cli.command()
def start(): click.echo('protein started')
if __name__ == '__main__': cli()
