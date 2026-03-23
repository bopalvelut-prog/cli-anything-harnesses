import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('blazor running')
@cli.command()
def start(): click.echo('blazor started')
if __name__ == '__main__': cli()
