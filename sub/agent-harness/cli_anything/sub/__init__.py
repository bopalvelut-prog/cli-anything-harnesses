import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sub running')
@cli.command()
def start(): click.echo('sub started')
if __name__ == '__main__': cli()
