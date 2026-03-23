import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dinner running')
@cli.command()
def start(): click.echo('dinner started')
if __name__ == '__main__': cli()
