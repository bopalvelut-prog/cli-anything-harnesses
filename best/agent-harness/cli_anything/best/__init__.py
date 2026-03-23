import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('best running')
@cli.command()
def start(): click.echo('best started')
if __name__ == '__main__': cli()
