import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('jetbrains running')
@cli.command()
def start(): click.echo('jetbrains started')
if __name__ == '__main__': cli()
