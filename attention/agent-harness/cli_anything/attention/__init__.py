import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('attention running')
@cli.command()
def start(): click.echo('attention started')
if __name__ == '__main__': cli()
