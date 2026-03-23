import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('history running')
@cli.command()
def start(): click.echo('history started')
if __name__ == '__main__': cli()
