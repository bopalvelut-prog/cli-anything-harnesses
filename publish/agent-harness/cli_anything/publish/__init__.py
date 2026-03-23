import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('publish running')
@cli.command()
def start(): click.echo('publish started')
if __name__ == '__main__': cli()
