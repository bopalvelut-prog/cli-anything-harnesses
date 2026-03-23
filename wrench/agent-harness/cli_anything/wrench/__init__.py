import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wrench running')
@cli.command()
def start(): click.echo('wrench started')
if __name__ == '__main__': cli()
