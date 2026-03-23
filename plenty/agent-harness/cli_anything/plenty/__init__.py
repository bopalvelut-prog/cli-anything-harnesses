import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('plenty running')
@cli.command()
def start(): click.echo('plenty started')
if __name__ == '__main__': cli()
