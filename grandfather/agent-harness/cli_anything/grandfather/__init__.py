import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('grandfather running')
@cli.command()
def start(): click.echo('grandfather started')
if __name__ == '__main__': cli()
