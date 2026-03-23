import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('truly running')
@cli.command()
def start(): click.echo('truly started')
if __name__ == '__main__': cli()
