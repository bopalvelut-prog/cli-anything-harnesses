import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('slide running')
@cli.command()
def start(): click.echo('slide started')
if __name__ == '__main__': cli()
