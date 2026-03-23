import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dotnet running')
@cli.command()
def start(): click.echo('dotnet started')
if __name__ == '__main__': cli()
