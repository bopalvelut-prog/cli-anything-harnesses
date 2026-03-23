import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('reset running')
@cli.command()
def start(): click.echo('reset started')
if __name__ == '__main__': cli()
