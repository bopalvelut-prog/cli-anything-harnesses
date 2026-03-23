import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('defend running')
@cli.command()
def start(): click.echo('defend started')
if __name__ == '__main__': cli()
