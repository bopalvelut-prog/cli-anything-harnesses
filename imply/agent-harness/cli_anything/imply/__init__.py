import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('imply running')
@cli.command()
def start(): click.echo('imply started')
if __name__ == '__main__': cli()
