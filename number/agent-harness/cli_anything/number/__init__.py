import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('number running')
@cli.command()
def start(): click.echo('number started')
if __name__ == '__main__': cli()
