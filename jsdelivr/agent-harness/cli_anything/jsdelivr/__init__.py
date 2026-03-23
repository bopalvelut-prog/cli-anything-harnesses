import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('jsdelivr running')
@cli.command()
def start(): click.echo('jsdelivr started')
if __name__ == '__main__': cli()
