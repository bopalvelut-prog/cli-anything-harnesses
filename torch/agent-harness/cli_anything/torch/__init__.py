import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('torch running')
@cli.command()
def start(): click.echo('torch started')
if __name__ == '__main__': cli()
