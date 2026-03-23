import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('reality running')
@cli.command()
def start(): click.echo('reality started')
if __name__ == '__main__': cli()
