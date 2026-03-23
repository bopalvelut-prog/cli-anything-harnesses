import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('region running')
@cli.command()
def start(): click.echo('region started')
if __name__ == '__main__': cli()
