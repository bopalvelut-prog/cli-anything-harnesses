import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dad running')
@cli.command()
def start(): click.echo('dad started')
if __name__ == '__main__': cli()
