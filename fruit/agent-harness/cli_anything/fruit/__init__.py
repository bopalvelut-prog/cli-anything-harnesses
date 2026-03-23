import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('fruit running')
@cli.command()
def start(): click.echo('fruit started')
if __name__ == '__main__': cli()
