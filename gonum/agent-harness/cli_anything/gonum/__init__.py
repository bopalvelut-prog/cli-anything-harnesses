import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('gonum running')
@cli.command()
def start(): click.echo('gonum started')
if __name__ == '__main__': cli()
