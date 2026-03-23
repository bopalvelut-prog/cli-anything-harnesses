import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('chest running')
@cli.command()
def start(): click.echo('chest started')
if __name__ == '__main__': cli()
