import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('hero running')
@cli.command()
def start(): click.echo('hero started')
if __name__ == '__main__': cli()
