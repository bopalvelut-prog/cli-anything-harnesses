import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('chakra running')
@cli.command()
def start(): click.echo('chakra started')
if __name__ == '__main__': cli()
