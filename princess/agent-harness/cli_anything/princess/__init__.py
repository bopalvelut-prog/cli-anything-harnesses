import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('princess running')
@cli.command()
def start(): click.echo('princess started')
if __name__ == '__main__': cli()
