import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('circuit running')
@cli.command()
def start(): click.echo('circuit started')
if __name__ == '__main__': cli()
