import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('between running')
@cli.command()
def start(): click.echo('between started')
if __name__ == '__main__': cli()
