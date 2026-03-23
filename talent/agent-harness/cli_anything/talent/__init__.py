import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('talent running')
@cli.command()
def start(): click.echo('talent started')
if __name__ == '__main__': cli()
