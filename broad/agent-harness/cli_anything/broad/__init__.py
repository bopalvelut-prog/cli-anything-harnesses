import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('broad running')
@cli.command()
def start(): click.echo('broad started')
if __name__ == '__main__': cli()
