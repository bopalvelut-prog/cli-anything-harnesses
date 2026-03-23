import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('nuget running')
@cli.command()
def start(): click.echo('nuget started')
if __name__ == '__main__': cli()
