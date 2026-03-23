import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('responsible running')
@cli.command()
def start(): click.echo('responsible started')
if __name__ == '__main__': cli()
