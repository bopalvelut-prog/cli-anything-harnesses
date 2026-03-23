import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cherry running')
@cli.command()
def start(): click.echo('cherry started')
if __name__ == '__main__': cli()
