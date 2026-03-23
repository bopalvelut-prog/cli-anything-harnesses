import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('method running')
@cli.command()
def start(): click.echo('method started')
if __name__ == '__main__': cli()
