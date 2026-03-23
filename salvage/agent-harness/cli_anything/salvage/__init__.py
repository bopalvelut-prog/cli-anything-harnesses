import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('salvage running')
@cli.command()
def start(): click.echo('salvage started')
if __name__ == '__main__': cli()
